# Given a string s, return all possible palindrome substrings of s. A palindrome reads the same backward as forward.

def find_all_palindromic_substrings(s: str) -> list[str]:
    result = set()

    def expand_array_center(left: int, right: int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            result.add(s[left:right+1])
            left -= 1
            right += 1

    for i in range(0, len(s)):
        expand_array_center(i, i)  # odd length palindromes
        expand_array_center(i, i+1)  # even length palindromes

    return list(result)

