from cmu_cpcs_utils import testFunction, Tree

def getTreeLeaves(tree):
    if tree.isLeaf():
        return {tree.value}
    else:
        result=set()
        for child in tree.children:
            result |= getTreeLeaves(child)
        return result

@testFunction
def testGetTreeLeaves():
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
    assert(getTreeLeaves(t1) == {3, 4})
    assert(getTreeLeaves(t1.children[0]) == {4})
    assert(getTreeLeaves(t1.children[1]) == {3})

    '''
    ─── 1 ─────── a ─────── 3
    '''
    t2 = Tree(1,
              Tree('a',
                   Tree(3)
                  )
             )
    assert(getTreeLeaves(t2) == {3})

    '''
    ─── 1 ─────── True 
    '''
    t3 = Tree(1,
              Tree(True)
             )
    assert(getTreeLeaves(t3) == {True})

    '''
    ─── 0
    '''
    t4 = Tree(0)
    assert(getTreeLeaves(t4) == {0})

def main():
    testGetTreeLeaves()

main()
