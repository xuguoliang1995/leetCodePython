"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

"""


def longestPalindrome(s: str) -> str:
    '''
    :param str:
    :return str:
    '''
    maximum = ""
    temp = ""
    # abcba
    for index in range(len(s)):
        if len(maximum) >= len(s) - index:
            break
        for index2 in range(index + len(maximum), len(s) + 1):
            fw = s[index: index2]
            bw = fw[::-1]
            if fw == bw:
                temp = fw
                if (len(temp)) > len(maximum):
                    maximum = temp
    return maximum
