# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         search_str = s.lower()
#         search_str = ''.join(ch for ch in search_str if ch.isalnum())

#         for i in range(len(search_str)):
#             j = len(search_str) - i - 1

#             if i == j:
#                 return True
            
#             if search_str[i] != search_str[j]:
#                 return False


def isPalindrome(s: str) -> bool:
    search_str = s.lower()
    search_str = ''.join(ch for ch in search_str if ch.isalnum())

    for i in range(len(search_str)):
        j = len(search_str) - i - 1

        if i == j:
            return True
        elif len(search_str) % 2 == 0 and i == (j-1):
            return True
        
        if search_str[i] != search_str[j]:
            return False
        
s = "No lemon, no melon"
search_str = s.lower()
print(search_str)
search_str = ''.join(ch for ch in search_str if ch.isalnum())
print(search_str)
print(len(search_str))
print(isPalindrome(search_str))
