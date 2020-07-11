'''
Given a String, compress the given string. See example for more details.

Input Format

Input contains string of lowercase and uppercase characters - S.

Constraints

1 <= len(S) <= 100

Output Format

Print the compressed string.

Sample Input 0

aaaBBBBhhhekkL
Sample Output 0

a3B4h3e1k2L1
Explanation 0

In the given string, a is repeating for 3 times - after compression a3.
Similarly, B is repeating for 4 times - B4
h is repeating for 3 times - h3
e is repeating for 1 times - e1
k is repeating for 2 times - k2
L is repeating for 1 times - L1
'''

string=str(input())
ind = 0
def gen_compressed_str(string):
    global ind
    comp_str = ""
    len_str = len(string)
    while (ind != len_str):
        count = 1

        while ((ind < (len_str-1)) and (string[ind] == string[ind+1])):
            count = count + 1
            ind = ind + 1

        # if (count == 1):
        #     comp_str = comp_str + str(string[ind])
        else:
            comp_str = comp_str + str(string[ind]) + str(count)

        ind += 1

    return comp_str
      
print(gen_compressed_str(string))
