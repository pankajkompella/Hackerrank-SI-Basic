'''
Given an integer - N, the letter 'o' must repeat for N times in the word Go...od.

Input Format

Input contains an integer - N.

Constraints

0 <= N<= 100

Output Format

Print the word Go..od with letter 'o' repeating for N times.

Sample Input 0

4
Sample Output 0

Gooood
Explanation 0

Self Explanatory
'''

n=int(input())
print('G','o'*n,'d', sep='')
