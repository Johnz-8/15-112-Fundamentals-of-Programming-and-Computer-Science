from cmu_cpcs_utils import testFunction, Tree

def getTreeValues(tree):
    if tree.isLeaf():
        return {tree.value}
    else:
        result={tree.value}
        for children in tree.children:
            result |= getTreeValues(children)
        return result

@testFunction
def testGetTreeValues():
    '''
             ┌─── 2 ─────── 4 
    ─── 1 ───┤
             └─── 3 
    '''
    t1 = Tree(1,
              Tree(2,
                   Tree(4)
                  ),
              Tree(3)
             )
    assert(getTreeValues(t1) == { 1, 2, 3, 4 })
    assert(getTreeValues(t1.children[0]) == { 2, 4 })
    assert(getTreeValues(t1.children[1]) == { 3 })
 
    '''
             ┌─── a 
             │
             ├─── -3 
    ─── 4 ───┤
             ├─── True 
             │
             └─── -1
    '''
    t2 = Tree(4,
              Tree('a'),
              Tree(-3),
              Tree(True),
              Tree(-1)
             )
    assert(getTreeValues(t2) == { 4, 'a', -3, True, -1 })

    '''
             ┌─── x 
    ─── 0 ───┤
             └─── x 
    '''
    t3 = Tree(0,
              Tree('x'),
              Tree('x'),
             )
    assert(getTreeValues(t3) == { 0, 'x' })

    '''
    ─── 0
    '''
    t4 = Tree(0)
    assert(getTreeValues(t4) == { 0 })

def main():
    testGetTreeValues()

main()
