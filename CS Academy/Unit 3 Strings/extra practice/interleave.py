from cmu_cpcs_utils import testFunction

def interleave(s1, s2):
    result=''
    length=min(len(s1),len(s2))
    for i in range(length):
        result+=s1[i]
        result+=s2[i]
    if len(s1)>len(s2):
        result+=s1[len(s2):]
    if len(s2)>len(s1):
        result+=s2[len(s1):]
    return result

@testFunction
def testInterleave():
    assert(interleave('pto', 'yhn') == 'python')
    assert(interleave('ab', 'xyz?') == 'axbyz?')
    assert(interleave('a', 'b') == 'ab')
    assert(interleave('xyz', 'a b') == 'xay zb')
    assert(interleave('', 'cpcs1') == 'cpcs1')
    assert(interleave('cpcs1', '') == 'cpcs1')
    assert(interleave('', '') == '')

def main():
    testInterleave()

main()
