# /usr/bin/env python3
# encoding: utf-8

class Soultion:
    def LengthOfLongestSubstring(self, s):
        '''
        :param s:
        :return int :
        '''
        str_list = []
        max_length = 0
        # abca [bcadjcd]
        for x in s:
            if x in str_list:
                str_list = str_list[str_list.index(x) + 1:]
            str_list.append(x)
            max_length = max(max_length, len(str_list))
        return max_length
