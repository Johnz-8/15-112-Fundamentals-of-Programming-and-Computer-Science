# CS Academy Homework Catalog

| Homework | Video-Guided | Lecture-Guided | Unguided |
|---|---|---|---|
| [Homework 1](#homework-1) | 7 | 7 | 7 |
| [Homework 2](#homework-2) | 4 | 10 | 7 |
| [Homework 3](#homework-3) | 2 | 8 | 8 |
| [Homework 4](#homework-4) | 1 | 9 | 5 |
| [Homework 5](#homework-5) | 5 | 11 | 7 |
| [Homework 8](#homework-8) | 2 | 8 | 10 |
| [Homework 9](#homework-9) | 3 | 4 | 8 |
| [Homework 10](#homework-10) | 8 | 4 | 9 |

---

## Homework 1

**Total: 21 pts**

### Video-Guided Exercises (7 pts)

| Points | Exercises |
|---|---|
| 1 pt each | getKthDigit, setKthDigit, digitCount, closestEven |
| 3 pts each | rectanglesOverlap |

### Lecture-Guided Exercises (7 pts)

| Points | Exercises |
|---|---|
| 1 pt each | distance, dotsOverlap, nthFibonacciNumber |
| 2 pts each | getGreen, numberOfSteps |

### Unguided Exercises (7 pts)

| Points | Exercises |
|---|---|
| 1 pt each | triangleArea (Heron's Formula), numberOfBricks, getInRange |
| 2 pts each | isGray, isDuplicatedNumber |

---

## Homework 2

**Total: 21 pts**

### Video-Guided Exercises (4 pts)

| Points | Exercises |
|---|---|
| 1 pt each | reverseNumber, mostFrequentDigit, hasConsecutiveDigits, nthHappyPrime |

### Lecture-Guided Exercises (10 pts)

| Points | Exercises |
|---|---|
| 1 pt each | isPrime, nthPrime, occursIn |
| 2 pts each | isRotation, carrylessAdd |
| 3 pts each | findZeroWithBisection |

### Unguided Exercises (7 pts)

| Points | Exercises |
|---|---|
| 2 pts each | stepsToReach495, nthLeftTruncatablePrime |
| 3 pts each | longestDigitRun |

---

## Homework 3

**Total: 18 pts**

### Video-Guided Exercises (2 pts)

| Points | Exercises |
|---|---|
| 1 pt each | encodeCaesarCipher + decodeCaesarCipher, topScorer |

### Lecture-Guided Exercises (8 pts)

| Points | Exercises |
|---|---|
| 1 pt each | rotateString |
| 2 pts each | hasBalancedParentheses, encodeSubstitutionCipher + decodeSubstitutionCipher |
| 3 pts each | evalPolynomial |

### Unguided Exercises (8 pts)

| Points | Exercises |
|---|---|
| 1 pt each | areAnagrams |
| 2 pts each | longestSubpalindrome, isWordLadder |
| 3 pts each | solvesCryptarithm |

---

## Homework 4

**Total: 15 pts (+3 bonus)**

### Video-Guided Exercises (1 pt)

| Points | Exercises |
|---|---|
| 1 pt each | removeEvens (mutating and nonmutating) |

### Lecture-Guided Exercises (9 pts)

| Points | Exercises |
|---|---|
| 1 pt each | removeRepeats (mutating and nonmutating) |
| 2 pts each | lookAndSay + inverseLookAndSay, multiplyPolynomials |
| **4 pts each** | **runSimpleProgram** ⭐ |

> ⭐ **runSimpleProgram is the only 4-point exercise in the catalog.**
>
> `runSimpleProgram(program, args)` is an interpreter for a tiny assembly-like language. It runs a legal program with the given `args` and returns the result. Translating the program into Python is not allowed. The interpreter keeps track of the local variables and the current line number, and steps through the program one line at a time until it reaches an `RTN` statement. The function must be non-destructive.
>
> **Expressions**
>
> | Syntax | Meaning |
> |---|---|
> | `123` | A non-negative integer literal |
> | `A[N]` | Argument `args[N]` (read-only) |
> | `L[N]` | Local variable N; unassigned locals are `0` |
> | `+ x y` / `- x y` | Prefix addition or subtraction; each operand is a literal, `A[N]`, or `L[N]` |
>
> **Statements** (one per line; leading and trailing whitespace is ignored)
>
> | Syntax | Meaning |
> |---|---|
> | `! comment` | Ignored |
> | `L[N] expr` | Assign `expr` to local N, e.g. `L5 - L2 42` sets L5 to L2 − 42 |
> | `label:` | Lowercase jump target; otherwise ignored |
> | `JMP label` | Always jump to `label` |
> | `JMP+ expr label` | Jump only if `expr` is positive |
> | `JMP0 expr label` | Jump only if `expr` is 0 |
> | `RTN expr` | Return `expr` |
>
> Syntax and runtime errors are not tested. Examples are a missing label, a missing argument, or assigning to an argument.

### Unguided Exercises (5 pts)

| Points | Exercises |
|---|---|
| 1 pt each | isNearlySorted |
| 2 pts each | rotateList (mutating and nonmutating), isClique |

### Bonus (Optional) Exercises (+3 pts)

| Points | Exercises |
|---|---|
| 3 pts each | firstNAcceptedValues |

---

## Homework 5

**Total: 23 pts**

### Video-Guided Exercises (5 pts)

| Points | Exercises |
|---|---|
| 1 pt each | removeRowAndCol (mutating and nonmutating) |
| 2 pts each | isLatinSquare, isLegalSudoku |

### Lecture-Guided Exercises (11 pts)

| Points | Exercises |
|---|---|
| 1 pt each | wordSearch |
| 2 pts each | betterWordSearch1, nQueensChecker |
| 3 pts each | isKingsTour, isBoxy |

### Unguided Exercises (7 pts)

| Points | Exercises |
|---|---|
| 1 pt each | isRectangular |
| 2 pts each | betterWordSearch2, insertRowAndCol (mutating and nonmutating), matrixMultiply |

---

## Homework 8

**Total: 20 pts**

### Video-Guided Exercises (2 pts)

| Points | Exercises |
|---|---|
| 1 pt each | repeats, mostCommonName |

### Lecture-Guided Exercises (8 pts)

| Points | Exercises |
|---|---|
| 1 pt each | containsPythagoreanTriple |
| 2 pts each | countMap, friendsOfFriends |
| 3 pts each | mostCommonLetterPairs |

### Unguided Exercises (10 pts)

| Points | Exercises |
|---|---|
| 1 pt each | invertDictionary |
| 2 pts each | makeSpeciesDictionary, getPairSum, matchPeople |
| 3 pts each | flightTimesMap |

---

## Homework 9

**Total: 15 pts**

### Video-Guided Exercises (3 pts)

| Points | Exercises |
|---|---|
| 1 pt each | Dog, Car, Angle |

### Lecture-Guided Exercises (4 pts)

| Points | Exercises |
|---|---|
| 2 pts each | Song and Album, Number Guessing Game |

### Unguided Exercises (8 pts)

| Points | Exercises |
|---|---|
| 1 pt each | Rectangle, Duration |
| 2 pts each | Word Guessing Game, Polynomial, Semester and Transcript Classes |

---

## Homework 10

**Total: 21 pts**

### Video-Guided Exercises (8 pts)

| Points | Exercises |
|---|---|
| 1 pt each | reverseList, flatten |
| 2 pts each | getTreePreorder, getCourse, powerSet |

### Lecture-Guided Exercises (4 pts)

| Points | Exercises |
|---|---|
| 1 pt each | getTreeLeaves, isAlmostPalindrome |
| 2 pts each | hasSublistSum |

### Unguided Exercises (9 pts)

| Points | Exercises |
|---|---|
| 2 pts each | evalExpressionTree, permutations, interleave |
| 3 pts each | digitCountMapInRange |
