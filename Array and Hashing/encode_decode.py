from typing import List


class Solution:

    # Extra delimiter to ensure that even if a string has a number, it doesnt get included as part of its length calc.
    # e.g - string is '42', so len = 2. Without delim it will be 242, so no way to know the actual length of the string.
    # With delim: we know that 2#42 that len=2 since it is before #.
    def encode(self, strs: List[str]) -> str:
        combined = ''
        for string in strs:
            length = len(string)
            combined += str(length) + '#' + string

        return combined
    
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            num = ''
            while s[i] != '#':
                num += s[i]
                i+= 1
            size = int(num)
            string = s[i+1:(i+1+size)]
            strs.append(string)
            i = i+1+size
        
        return strs



def decode(s: str) -> List[str]:
    strs = []
    i = 0
    while i < len(s):
        print(f'i: {i}')
        num = ''
        while s[i] != '#':
            num += s[i]
            i+= 1
        size = int(num)
        string = s[i+1:(i+1+size)]
        strs.append(string)
        i = i+1+size
    
    print(strs)

def encode(strs: List[str]) -> str:
    combined = ''
    for string in strs:
        length = len(string)
        combined += str(length) + '#' + string
    
    print(combined)
    decode(combined)


strs = ["we","say",":","yes","!@#$%^&*()"]
encode(strs)