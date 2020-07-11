'''
Given a sentence and a character, count occurrence of the given character in the sentence. All characters in the sentence are lower case.

Input Format

First line of input contains a sentence - S and second line of input contains a lowercase character - ch.

Constraints

1 <= len(S) <= 100
'a' <= ch <= 'z'

Output Format

Print count of the given character in the sentence.

Sample Input 0

You're a good person.
o
Sample Output 0

4
Explanation 0

Self Explanatory
'''

s=str(input())
c=str(input())
cntr=0
for i in s:
    if c==i:
        cntr+=1
    else:
        pass
print(cntr)
