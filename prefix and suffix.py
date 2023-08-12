#YET TO BE DONE

'''
Given a string, compute the length of longest prefix string which is same as the suffix of the string, the length of the prefix or suffix string must be less than the given input string.

Input Format

Input contains a string - S.

Constraints

1 <= len(S) <= 100

Output Format

Print length of longest prefix string which is same as suffix of the string.

Sample Input 0

smartintsmart
Sample Output 0

5
Explanation 0

Self Explanatory
'''
s = input().strip()

length = 0
i = 1
n = len(s)
lps = [0] * n

while i < n:
    if s[i] == s[length]:
        length += 1
        lps[i] = length
        i += 1
    else:
        if length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

result = lps[-1]
print(result)
