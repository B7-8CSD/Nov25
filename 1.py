"""Given a string S consisting only of opening and closing curly brackets '{' and '}' 
find out the minimum number of reversals required to make a balanced expression.

Input
string S consisting only of { and }.

Output
Print out minimum reversals required to make S balanced. If it cannot be balanced, then print -1.


Examples
Input
}{{}}{{{

Ouput: 3

Input
{{}}}}
output: 1

Input
{{{{}}}}
Output
0

Explanation:
Testcase 1: For the given string }{{}}{{{ since the length is even we just need to count the number of openning brackets('{') suppose denoted by 'm' and closing brackest('}') suppose dentoed by 'n' after removing highlighted ones. After counting compute ceil(m/2) + ceil(n/2).
"""


import unittest

def min_rev(s):
    c1=0
    c2=0
    for i in range(0,len(s)):
        if s[i]=="{":
            c1=c1+1
        else:
            c2=c2+1
    if c1%2==0 and c2%2==0:
        if (c1==c2):
            return 0
        else:
            r=c1/2
            r1=c2/2
            if r<r1:
                return r
            else:
                return r1
    else:
        if c1<c2:
            return c1
        else:
            return c2

# DO NOT TOUCH THE BELOW CODE
class TestCommonWords(unittest.TestCase):

    def test_01(self):
        s="}{{}}{{{"
        output = 3
        self.assertEqual(min_rev(s), output)

    def test_02(self):
        s="{{{{}}}}"
        output = 0
        self.assertEqual(min_rev(s), output)

    def test_03(self):
        s="{{}}}}"
        
        output = 1
        self.assertEqual(min_rev(s), output)


if __name__ == '__main__':
    unittest.main(verbosity=2)


