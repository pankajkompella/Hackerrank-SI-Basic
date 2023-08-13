#Solved
'''
Print right-angled triangle pattern. See example for more details.

Input Format

First line of input contains a single integer N - the size of the triangle.

Constraints

1 <= N <= 50

Output Format

For the given integer, print the right-angled triangle pattern.

Sample Input 0

5
Sample Output 0

1
2 6
3 7 10
4 8 11 13
5 9 12 14 15
Explanation 0

Self Explanatory
Code:
'''
N = int(input())

for i in range(1, N + 1):
    diff = N - 1
    value = i
    for j in range(1, i + 1):
        print(value, end=" ")

        value += diff
        diff -= 1

    print()


