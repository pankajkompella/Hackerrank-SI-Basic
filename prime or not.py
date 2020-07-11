'''
Given a positive integer - N. Check whether the number is prime or not.

Input Format

Input contains positive integer - N.

Constraints

1 <= N <= 109

Output Format

Print "Yes" if the number is prime, "No" otherwise.

Sample Input 0

11
Sample Output 0

Yes
Explanation 0

Self Explanatory
'''

# mod=1000000007
n=int(input())
# n=n%mod
# def prime(n):
#     if n<=1:
#         print('No')
#     else:
#         for i in range(2,int((n)**(1/2))):
#             if n%i==0:
#                 return('No')
#             else:
#                 return('Yes')
# print(prime(n))

if n > 1:
    for i in range(2,int((n)**(1/2))):
        if (n % i) == 0:
            print("No")
            break
    else:
        print("Yes")
else:
    print("No")
