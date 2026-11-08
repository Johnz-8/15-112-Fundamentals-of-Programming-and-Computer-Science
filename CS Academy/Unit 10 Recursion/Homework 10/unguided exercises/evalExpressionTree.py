from cmu_cpcs_utils import testFunction, Tree

def evalExpressionTree(tree):
    if tree.isLeaf():
        return tree.value
    else:
        if tree.value=='+':
            result=0
            for child in tree.children:
                result+=evalExpressionTree(child)
        elif tree.value=='*':
            result=1
            for child in tree.children:
                result*=evalExpressionTree(child)
        return result
            

@testFunction
def testEvalExpressionTree():
    '''
             ┌─── 1 
    ─── + ───┤
             └─── 2
    '''
    t1 = Tree('+', 
              Tree(1),
              Tree(2)
             )
    # 1 + 2 = 3
    assert(evalExpressionTree(t1) == 3) 

    '''
             ┌─── 2 
             │
    ─── * ───┼─── 3 
             │
             └─── 4
    '''
    t2 = Tree('*', 
              Tree(2),
              Tree(3),
              Tree(4)
             )
    # 2 * 3 * 4 = 24
    assert(evalExpressionTree(t2) == 24) 

    '''
             ┌─── 1 
             │
    ─── + ───┤         ┌─── 2 
             └─── * ───┤
                       └─── 3 
    '''
    t3 = Tree('+', 
              Tree(1),
              Tree('*', 
                   Tree(2),
                   Tree(3)
                  )
             )
    # 1 + (2 * 3) = 7                    
    assert(evalExpressionTree(t3) == 7) 

    '''
             ┌─── 1 
             │
             │         ┌─── 2 
             ├─── * ───┤
             │         └─── 3 
             │
    ─── + ───┤         ┌─── 4 
             │         │
             │         ├─── 5 
             └─── * ───┤
                       │         ┌─── 9 
                       └─── + ───┤
                                 └─── 1 
    '''
    t4 = Tree('+', 
              Tree(1),
              Tree('*', 
                   Tree(2),
                   Tree(3)
                  ),
              Tree('*', 
                   Tree(4),
                   Tree(5),
                   Tree('+', 
                        Tree(9),
                        Tree(1)
                       )
                  )
             )
    # 1 + (2 * 3) + (4 * 5 * (9 + 1)) = 207
    assert(evalExpressionTree(t4) == 207)

    '''
    ─── 0
    '''
    t5 = Tree(0)
    assert(evalExpressionTree(t5) == 0)

def main():
    testEvalExpressionTree()

main()
