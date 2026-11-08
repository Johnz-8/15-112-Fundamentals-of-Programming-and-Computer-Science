from cmu_cpcs_utils import testFunction

def runSimpleProgram(program, args):
    unstructuredLines=program.splitlines()
    lines=[v.strip() for v in unstructuredLines]
    line=0
    localVars=[]
    while True:
        terms=lines[line].split(' ')
        if lines[line].startswith('!') or lines[line].endswith(':'):
            line+=1
            continue
        elif terms[0]=='RTN':
            return evalExpr(terms[1:], args, localVars)
        elif terms[0].startswith('L'):
            result=evalExpr(terms[1:], args, localVars)
            N=int(terms[0][1:])
            setLocalVar(localVars, N, result)
        elif terms[0]=='JMP+':
            if evalExpr(terms[1:-1],args,localVars)>0:
                line=lines.index(terms[-1]+':')
        elif terms[0]=='JMP0':
            if evalExpr(terms[1:-1],args,localVars)==0:
                line=lines.index(terms[-1]+':')
        elif terms[0]=='JMP':
                line=lines.index(terms[-1]+':')
        line+=1

def getLocalVar(localVars, N):
    while len(localVars)<= N:
        localVars.append(0)
    return localVars[N]

def setLocalVar(localVars, N, result):
    while len(localVars)<= N:
        localVars.append(0)
    localVars[N]=result

def evalExpr(expr, args, localVars):
        if len(expr)==1:
            if expr[0].isdigit():
                return int(expr[0])
        if expr[0].startswith('A'):
            N=int(expr[0][1:])
            return args[N]
        if expr[0].startswith('L'):
            N=int(expr[0][1:])
            return getLocalVar(localVars, N)
        if expr[0]=='+':
            operand1=evalExpr([expr[1]],args,localVars)
            operand2=evalExpr([expr[2]],args,localVars)
            return operand1+operand2
        if expr[0]=='-':
            operand1=evalExpr([expr[1]],args,localVars)
            operand2=evalExpr([expr[2]],args,localVars)
            return operand1-operand2            

@testFunction
def testRunSimpleProgram():
    largest = """! largest: Returns max(A0, A1)
                  L0 - A0 A1
                  JMP+ L0 a0
                  RTN A1
                  a0:
                  RTN A0"""
    assert(runSimpleProgram(largest, [5, 6]) == 6)
    assert(runSimpleProgram(largest, [6, 5]) == 6)

    sumToN = """! SumToN: Returns 1 + ... + A0
                ! L0 is a counter, L1 is the result
                L0 0
                L1 0
                loop:
                L2 - L0 A0
                JMP0 L2 done
                L0 + L0 1
                L1 + L1 L0
                JMP loop
                done:
                RTN L1"""
    assert(runSimpleProgram(sumToN, [5]) == 1+2+3+4+5)
    assert(runSimpleProgram(sumToN, [10]) == 10*11//2)

def main():
    testRunSimpleProgram()

main()
