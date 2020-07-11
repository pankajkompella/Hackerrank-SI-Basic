#ONLY 10 OUT OF 11 TEST CASES PASSED

'''
Given a number - N, reverse the number.

Input Format

Input contains a integer - N.

Constraints

-1018<= N <= 1018

Output Format

Print the reversed number.

Sample Input 0

1344
Sample Output 0

4431
Explanation 0

Self Explanatory.
'''

def reverseint(n):
    sign = n//abs(n)
    n = abs(n)
    return int(str(n)[::-1])*sign
n=int(input())
print(reverseint(n))
