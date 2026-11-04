"""Conway's Game of Life: a 2D-list data structure with a cmu_graphics UI.

The grid is a 2D list of ints; cells outside the grid count as empty.
    DEAD = 0           - empty cell
    ALIVE = 1          - prey, following Conway's rules
    DEAD_PREDATOR = 2  - predator corpse, shown for one generation (empty)
    PREDATOR = 3       - live predator

A parallel 2D list of zones shapes the prey's environment:
    Normal  - standard rules, but births follow the season's birth chance
    Fertile - dead cells are born with 2 or 3 neighbors, in any season
    Toxic   - no births, and live cells need exactly 3 neighbors to survive
Seasons cycle every SEASON_LENGTH generations, and each generation has a
small chance of a disaster that wipes out a square region.

Predators are stationary. Each generation a predator eats one random prey
within HUNT_RADIUS, or goes hungry. It dies after more than HUNGER_LIMIT
hungry generations, at PREDATOR_LIFESPAN, or with more than three predator
neighbors (competition). A predator breeds only in a generation it ate
and survived, into a random empty neighbor. Prey die of old age once
they pass PREY_LIFESPAN.
Prey count only prey neighbors; predators don't care about zones.

Each generation: predators hunt, die and breed; prey follow Conway's rules;
live cells age; then a disaster may strike.

Controls:
    Left click / drag  - paint with the current brush (a click on a
                         matching cell toggles it off)
    Right drag         - fill a rectangle with the current brush
    Z                  - cycle brush: cells, predator, fertile, toxic, eraser
    Space              - play or pause
    S                  - advance one generation (while paused)
    C                  - clear the cells (with their ages and hunger),
                         reset the generation count and pause
    X                  - clear the zones
    Up / Down          - speed up / slow down
"""

from cmu_graphics import *

# Imported after cmu_graphics, whose star import exports its own `random`.
import random

# Cell values. Zones live in their own grid, so they need no values here.
DEAD = 0           # Empty cell.
ALIVE = 1          # Live prey.
DEAD_PREDATOR = 2  # Corpse, shown for one generation.
PREDATOR = 3       # Live predator.

# Zone types, stored in a 2D list parallel to the grid.
NORMAL, FERTILE, TOXIC = 0, 1, 2

# Environment settings.
SEASONS = (('Spring', 1.0), ('Summer', 0.8), ('Autumn', 0.5),
           ('Winter', 0.2))  # (name, birth chance in normal zones)
SEASON_LENGTH = 20      # Generations per season.
DISASTER_CHANCE = 0.02  # Chance per generation that a disaster strikes.
DISASTER_RADIUS = 4     # Half-width of the square a disaster wipes out.

# Predator and lifespan settings.
HUNT_RADIUS = 2         # How far (in cells) a predator can reach prey.
HUNGER_LIMIT = 5        # Generations a predator survives without eating.
PREY_LIFESPAN = 60      # Age at which prey die of old age.
PREDATOR_LIFESPAN = 40  # Age at which predators die of old age.

# Brushes as (name, layer, value): layer is 'cells' or 'zones'.
BRUSHES = (('Cells', 'cells', ALIVE), ('Predator', 'cells', PREDATOR),
           ('Fertile', 'zones', FERTILE), ('Toxic', 'zones', TOXIC),
           ('Eraser', 'zones', NORMAL))

# Layout and speed settings for the UI.
MAX_BOARD_SIZE = 600    # Largest board side length in pixels.
MIN_WINDOW_WIDTH = 460  # Keeps the header text readable on narrow grids.
HEADER_HEIGHT = 96      # Space above the board for status text.
MARGIN = 10
MIN_SPEED, MAX_SPEED = 1, 50
DISASTER_SHOW_STEPS = 5  # Generations the disaster marker stays visible.


# Data structure: functions on a 2D list

def make_grid(rows, cols, fill=DEAD):
    """Return a rows x cols grid with every cell set to fill."""
    grid = []
    for _ in range(rows):
        grid.append([fill] * cols)
    return grid


def in_bounds(grid, row, col):
    """Return True if (row, col) lies inside the grid."""
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


def toggle_cell(grid, row, col, value=ALIVE):
    """Set the cell to value, or to DEAD if it already holds value."""
    if grid[row][col] == value:
        grid[row][col] = DEAD
    else:
        grid[row][col] = value


def clear_grid(grid, fill=DEAD):
    """Set every cell in the grid to fill."""
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            grid[row][col] = fill


def live_count(grid, value=ALIVE):
    """Return the number of cells equal to value (live prey by default)."""
    count = 0
    for row in grid:
        count += row.count(value)
    return count


def count_live_neighbors(grid, row, col, value=ALIVE):
    """Count cells equal to value among the eight neighbors of (row, col)."""
    # Clamp the 3x3 window to the grid instead of bounds-checking each cell.
    count = 0
    for n_row in range(max(row - 1, 0), min(row + 2, len(grid))):
        for n_col in range(max(col - 1, 0), min(col + 2, len(grid[0]))):
            # Skip the center cell itself; only count its neighbors.
            if (n_row, n_col) != (row, col) and grid[n_row][n_col] == value:
                count += 1
    return count


def cells_near(grid, row, col, radius, values):
    """Return (row, col) tuples within radius whose value is in values.

    The square window is clamped to the grid and excludes the cell itself.
    predator_phase uses it to find prey to hunt and empty spots to breed into.
    """
    found = []
    # Clamp the window so it doesn't go out of bounds.
    for n_row in range(max(row - radius, 0),
                       min(row + radius + 1, len(grid))):
        for n_col in range(max(col - radius, 0),
                           min(col + radius + 1, len(grid[0]))):
            # Skip the center cell itself.
            if (n_row, n_col) != (row, col) and grid[n_row][n_col] in values:
                found.append((n_row, n_col))
    return found


def current_season(generation):
    """Return the (name, birth chance) season for a generation."""
    # Cycles through the four seasons.
    return SEASONS[(generation // SEASON_LENGTH) % len(SEASONS)]


def predator_phase(grid, ages, hunger):
    """Return a new grid after predators hunt, die and breed.

    Updates ages and hunger in place, and clears last generation's corpses.
    1) Each predator eats one random prey within HUNT_RADIUS, or goes hungry.
    2) Predators die if starved, too old, or with more than three predator
       neighbors on the starting grid; they leave a DEAD_PREDATOR corpse.
    3) Predators that ate and survived breed into a random empty neighbor.
    """
    rows, cols = len(grid), len(grid[0])
    new_grid = make_grid(rows, cols)
    predators = []
    # Copy the grid minus old corpses, and collect predator positions.
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != DEAD_PREDATOR:
                new_grid[row][col] = grid[row][col]
            if grid[row][col] == PREDATOR:
                predators.append((row, col))

    # 1) Hunt: eat one random prey in range, or get hungrier.
    fed = []
    for row, col in predators:
        prey = cells_near(new_grid, row, col, HUNT_RADIUS, (ALIVE,))
        if prey:
            prey_row, prey_col = random.choice(prey)
            new_grid[prey_row][prey_col] = DEAD
            ages[prey_row][prey_col] = 0
            hunger[row][col] = 0
            fed.append((row, col))
        else:
            hunger[row][col] += 1

    # 2) Die: starvation, old age, or overcrowding (checked on the old grid).
    for row, col in predators:
        if (hunger[row][col] > HUNGER_LIMIT
                or ages[row][col] >= PREDATOR_LIFESPAN
                or count_live_neighbors(grid, row, col, PREDATOR) > 3):
            new_grid[row][col] = DEAD_PREDATOR
            ages[row][col] = 0
            hunger[row][col] = 0

    # 3) Breed: surviving fed predators spawn into a random empty neighbor.
    for row, col in fed:
        if new_grid[row][col] == PREDATOR:
            spots = cells_near(new_grid, row, col, 1, (DEAD, DEAD_PREDATOR))
            if spots:
                child_row, child_col = random.choice(spots)
                new_grid[child_row][child_col] = PREDATOR
                ages[child_row][child_col] = 0
                hunger[child_row][child_col] = 0
    return new_grid


def next_generation(grid, zones, birth_chance):
    """Return a new grid with prey one generation ahead.

    Prey count only prey neighbors. Live prey survive with 3 neighbors,
    or 2 unless their zone is toxic. Empty cells (DEAD or DEAD_PREDATOR)
    are born with 2 or 3 neighbors in fertile zones, with exactly 3 in
    normal zones (if a birth_chance roll succeeds), and never in toxic
    zones. Predators are copied unchanged, and corpses stay unless prey
    are born there.
    """
    rows, cols = len(grid), len(grid[0])
    new_grid = make_grid(rows, cols)
    for row in range(rows):
        for col in range(cols):
            cell = grid[row][col]
            if cell == PREDATOR:
                # Prey can't be born on a live predator.
                new_grid[row][col] = PREDATOR
                continue
            neighbors = count_live_neighbors(grid, row, col)
            zone = zones[row][col]
            # Survival rule for live prey, then birth rules by zone.
            if cell == ALIVE:
                lives = neighbors == 3 or (neighbors == 2 and zone != TOXIC)
            elif zone == FERTILE:
                lives = neighbors == 2 or neighbors == 3
            elif zone == NORMAL:
                lives = neighbors == 3 and random.random() < birth_chance
            else:
                lives = False
            if lives:
                new_grid[row][col] = ALIVE
            elif cell == DEAD_PREDATOR:
                new_grid[row][col] = DEAD_PREDATOR
    return new_grid


def age_cells(grid, ages, hunger):
    """Age live cells by one generation and kill prey past PREY_LIFESPAN.

    Also resets age and hunger on cells they no longer apply to.
    """
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            cell = grid[row][col]
            if cell == ALIVE or cell == PREDATOR:
                ages[row][col] += 1
            # '>' so prey, like predators, are visible for the full lifespan.
            if cell == ALIVE and ages[row][col] > PREY_LIFESPAN:
                grid[row][col] = cell = DEAD
            if cell != ALIVE and cell != PREDATOR:
                ages[row][col] = 0
            if cell != PREDATOR:
                hunger[row][col] = 0


def disaster_area(grid, row, col):
    """Return (top, bottom, left, right) of the disaster square, clamped.

    bottom and right are exclusive, like range().
    """
    # Clamp each edge so the square doesn't go out of bounds.
    return (max(row - DISASTER_RADIUS, 0),
            min(row + DISASTER_RADIUS + 1, len(grid)),
            max(col - DISASTER_RADIUS, 0),
            min(col + DISASTER_RADIUS + 1, len(grid[0])))


def rect_area(start, end):
    """Return (top, bottom, left, right) of the rectangle spanning two
    (row, col) corners, given in any order.

    bottom and right are exclusive, like range().
    """
    top, bottom = sorted((start[0], end[0]))
    left, right = sorted((start[1], end[1]))
    return (top, bottom + 1, left, right + 1)


def maybe_disaster(grid, ages, hunger):
    """With DISASTER_CHANCE, wipe a random square; return center or None."""
    if random.random() >= DISASTER_CHANCE:
        return None
    center = (random.randrange(len(grid)), random.randrange(len(grid[0])))
    top, bottom, left, right = disaster_area(grid, center[0], center[1])
    for row in range(top, bottom):
        for col in range(left, right):
            grid[row][col] = DEAD
            ages[row][col] = 0
            hunger[row][col] = 0
    return center


def step_generation(grid, ages, hunger, zones, birth_chance):
    """Advance one generation; return (new grid, disaster center or None).

    Order: 1) predators hunt, die and breed, and old corpses are cleared;
    2) prey follow Conway's rules with zones and the season's birth chance;
    3) live cells age and old prey die; 4) a disaster may strike.
    ages and hunger are updated in place.
    """
    grid = predator_phase(grid, ages, hunger)
    grid = next_generation(grid, zones, birth_chance)
    age_cells(grid, ages, hunger)
    center = maybe_disaster(grid, ages, hunger)
    return (grid, center)

# cmu_graphics UI

def onAppStart(app, rows, cols):
    # rows and cols are forwarded from the runApp call in main().
    app.grid = make_grid(rows, cols)
    app.ages = make_grid(rows, cols, 0)    # Generations each cell has lived.
    app.hunger = make_grid(rows, cols, 0)  # Generations since a predator ate.
    app.zones = make_grid(rows, cols, NORMAL)
    app.rows, app.cols = rows, cols
    app.isRunning = False
    app.generation = 0
    app.stepsPerSecond = 5
    app.lastDragCell = None
    app.rectStart = None  # Right-drag rectangle corners, or None.
    app.rectEnd = None
    app.brush = 0  # Index into BRUSHES.
    app.lastDisaster = None
    app.disasterTimer = 0
    # Worst case: a zone rect per cell, a cell rect per cell (prey,
    # predators and corpses can alternate), plus grid lines, background,
    # labels, the disaster outline and the rectangle-brush preview.
    # Raise the default 2500-shape cap.
    app.setMaxShapeCount(2 * rows * cols + rows + cols + 20)
    updateLayout(app)


def onResize(app):
    # cmu_graphics windows are resizable; refit the board to the new size.
    updateLayout(app)


def updateLayout(app):
    """Fit square cells to the window and center the board horizontally."""
    availWidth = app.width - 2 * MARGIN
    availHeight = app.height - HEADER_HEIGHT - MARGIN
    # The tighter dimension sets the size so cells stay square.
    app.cellSize = max(min(availWidth / app.cols, availHeight / app.rows), 1)
    app.boardLeft = (app.width - app.cols * app.cellSize) / 2


def getCell(app, x, y):
    """Return the (row, col) under pixel (x, y), or None if off the board."""
    if x < app.boardLeft or y < HEADER_HEIGHT:
        return None
    row = int((y - HEADER_HEIGHT) // app.cellSize)
    col = int((x - app.boardLeft) // app.cellSize)
    if in_bounds(app.grid, row, col):
        return (row, col)
    return None


def getClampedCell(app, x, y):
    """Return the (row, col) nearest pixel (x, y), clamped to the board."""
    row = int((y - HEADER_HEIGHT) // app.cellSize)
    col = int((x - app.boardLeft) // app.cellSize)
    return (min(max(row, 0), app.rows - 1), min(max(col, 0), app.cols - 1))


def advance(app):
    """Move the simulation forward one generation."""
    birthChance = current_season(app.generation)[1]
    app.grid, disaster = step_generation(app.grid, app.ages, app.hunger,
                                         app.zones, birthChance)
    if disaster is not None:
        app.lastDisaster = disaster
        app.disasterTimer = DISASTER_SHOW_STEPS
    elif app.disasterTimer > 0:
        app.disasterTimer -= 1
    app.generation += 1


def paint(app, cell, isPress):
    """Apply the current brush to a cell: zone brushes paint zones, cell
    brushes toggle on press and paint on drag, resetting age and hunger."""
    row, col = cell
    app.lastDragCell = cell
    _, layer, value = BRUSHES[app.brush]
    if layer == 'zones':
        app.zones[row][col] = value
    else:
        if not isPress and app.grid[row][col] == value:
            return  # Dragging over an existing cell keeps its age and hunger.
        if isPress:
            toggle_cell(app.grid, row, col, value)
        else:
            app.grid[row][col] = value
        app.ages[row][col] = 0
        app.hunger[row][col] = 0


def fillRect(app, start, end):
    """Paint every cell in the rectangle between two corners with the
    current brush, using drag semantics so existing cells aren't toggled
    off."""
    top, bottom, left, right = rect_area(start, end)
    for row in range(top, bottom):
        for col in range(left, right):
            paint(app, (row, col), False)
    # paint() records each cell; don't let a later left drag skip the last.
    app.lastDragCell = None


def onMousePress(app, mouseX, mouseY, button):
    # button: 0 = left (line brush), 2 = right (rectangle brush).
    cell = getCell(app, mouseX, mouseY)
    if cell is None:
        return
    if button == 0:
        paint(app, cell, True)
    elif button == 2:
        app.rectStart = app.rectEnd = cell


def onMouseDrag(app, mouseX, mouseY, buttons):
    # buttons lists every held button, e.g. [0], [2] or [0, 2].
    if 0 in buttons:
        # Skip the cell already handled so a drag doesn't re-toggle it.
        cell = getCell(app, mouseX, mouseY)
        if cell is not None and cell != app.lastDragCell:
            paint(app, cell, False)
    if 2 in buttons and app.rectStart is not None:
        app.rectEnd = getClampedCell(app, mouseX, mouseY)


def onMouseRelease(app, mouseX, mouseY, button):
    # End a left drag, or commit the right-drag rectangle.
    if button == 0:
        app.lastDragCell = None
    elif button == 2 and app.rectStart is not None:
        # Drag events are throttled, so take the corner from the release.
        app.rectEnd = getClampedCell(app, mouseX, mouseY)
        fillRect(app, app.rectStart, app.rectEnd)
        app.rectStart = app.rectEnd = None


def onKeyPress(app, key):
    # Keyboard controls; see the module docstring for the full list.
    if key == 'space':
        app.isRunning = not app.isRunning
    elif key == 's' and not app.isRunning:
        advance(app)
    elif key == 'c':
        clear_grid(app.grid)
        clear_grid(app.ages, 0)
        clear_grid(app.hunger, 0)
        app.generation = 0
        app.disasterTimer = 0
        app.isRunning = False
    elif key == 'x':
        app.zones = make_grid(app.rows, app.cols, NORMAL)
    elif key == 'z':
        app.brush = (app.brush + 1) % len(BRUSHES)
    elif key == 'up':
        app.stepsPerSecond = min(app.stepsPerSecond + 1, MAX_SPEED)
    elif key == 'down':
        app.stepsPerSecond = max(app.stepsPerSecond - 1, MIN_SPEED)


def onStep(app):
    # Called stepsPerSecond times a second; advance only while running.
    if app.isRunning:
        advance(app)


def redrawAll(app):
    drawHeader(app)
    drawBoard(app)


def drawHeader(app):
    """Draw the status lines (counts, season, brush, speed) and controls."""
    cx = app.width / 2
    season, birthChance = current_season(app.generation)
    drawLabel(f'Generation {app.generation}   Prey {live_count(app.grid)}'
              f'   Predators {live_count(app.grid, PREDATOR)}',
              cx, 14, size=15, bold=True)
    drawLabel(f'{season} (births {int(birthChance * 100)}%)'
              f'   Brush: {BRUSHES[app.brush][0]}'
              f'   Speed {app.stepsPerSecond}/s',
              cx, 32, size=13, bold=True)
    status = 'Running' if app.isRunning else 'Paused'
    color = 'green' if app.isRunning else 'crimson'
    if app.disasterTimer > 0:
        # Status and warning sit on either side of center so they never touch.
        drawLabel(status, cx - 6, 50, size=13, bold=True, fill=color,
                  align='right')
        drawLabel('Disaster!', cx + 6, 50, size=13, bold=True, fill='red',
                  align='left')
    else:
        drawLabel(status, cx, 50, size=13, bold=True, fill=color)
    drawLabel('Left drag: draw   Right drag: rectangle   Z: brush'
              '   Space: play/pause',
              cx, 68, size=11, fill='gray')
    drawLabel('S: step   C: clear cells   X: clear zones   Up/Down: speed',
              cx, 82, size=11, fill='gray')


def drawRuns(app, grid, value, color):
    """Draw one rect per horizontal run of cells equal to value."""
    size = app.cellSize
    for row in range(app.rows):
        col = 0
        while col < app.cols:
            if grid[row][col] == value:
                start = col
                while col < app.cols and grid[row][col] == value:
                    col += 1
                drawRect(app.boardLeft + start * size,
                         HEADER_HEIGHT + row * size,
                         (col - start) * size, size, fill=color)
            else:
                col += 1


def drawBoard(app):
    """Draw the board with as few shapes as possible.

    One white background, one rect per horizontal run of each zone type
    and of each cell type (prey black, predators crimson, corpses
    rosyBrown), and one line per grid line (skipped when cells are under
    6 px), instead of one shape per cell.
    Outlines mark the latest disaster and the rectangle-brush preview.
    """
    size = app.cellSize
    left, top = app.boardLeft, HEADER_HEIGHT
    width, height = app.cols * size, app.rows * size
    drawRect(left, top, width, height, fill='white')
    drawRuns(app, app.zones, FERTILE, 'paleGreen')
    drawRuns(app, app.zones, TOXIC, 'thistle')
    drawRuns(app, app.grid, ALIVE, 'black')
    drawRuns(app, app.grid, PREDATOR, 'crimson')
    drawRuns(app, app.grid, DEAD_PREDATOR, 'rosyBrown')

    # Skip grid lines on tiny cells so the board stays legible.
    if size >= 6:
        for row in range(app.rows + 1):
            y = top + row * size
            drawLine(left, y, left + width, y, fill='lightGray')
        for col in range(app.cols + 1):
            x = left + col * size
            drawLine(x, top, x, top + height, fill='lightGray')

    # Outline the most recent disaster while its marker is active.
    if app.disasterTimer > 0:
        rowTop, rowBottom, colLeft, colRight = disaster_area(
            app.grid, app.lastDisaster[0], app.lastDisaster[1])
        drawRect(left + colLeft * size, top + rowTop * size,
                 (colRight - colLeft) * size, (rowBottom - rowTop) * size,
                 fill=None, border='red', borderWidth=2)

    # Outline the rectangle brush while the right button is held.
    if app.rectStart is not None:
        rowTop, rowBottom, colLeft, colRight = rect_area(app.rectStart,
                                                         app.rectEnd)
        drawRect(left + colLeft * size, top + rowTop * size,
                 (colRight - colLeft) * size, (rowBottom - rowTop) * size,
                 fill=None, border='dodgerBlue', borderWidth=2)


# Entry point

def read_positive_int(prompt):
    """Prompt until the user enters a positive integer."""
    while True:
        text = input(prompt).strip()
        if text.isdigit() and int(text) > 0:
            return int(text)
        print('Please enter a positive integer.')


def main():
    """Ask for the grid size, then open the game window."""
    rows = read_positive_int('Number of rows: ')
    cols = read_positive_int('Number of columns: ')
    # Pick a starting window that fits the board inside MAX_BOARD_SIZE.
    # Cell size is recomputed from the window in updateLayout, so the
    # board grows and shrinks when the user resizes the window.
    cellSize = max(MAX_BOARD_SIZE / max(rows, cols), 1)
    width = max(int(cols * cellSize + 2 * MARGIN), MIN_WINDOW_WIDTH)
    height = int(rows * cellSize + HEADER_HEIGHT + MARGIN)
    runApp(width=width, height=height, rows=rows, cols=cols)


if __name__ == '__main__':
    main()