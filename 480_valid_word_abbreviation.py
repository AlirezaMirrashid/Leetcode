# LeetCode 408: Valid Word Abbreviation
# Problem Link: https://leetcode.com/problems/valid-word-abbreviation/
#
# Description:
# A string can be abbreviated by replacing non-adjacent, non-empty substrings with their lengths.
# The lengths should not have leading zeros.
#
# Given a string `word` and an abbreviation `abbr`, return whether the string matches the given abbreviation.
#
# Example 1:
# Input: word = "internationalization", abbr = "i12iz4n"
# Output: True
#
# Example 2:
# Input: word = "apple", abbr = "a2e"
# Output: False
#
# Constraints:
# - 1 <= word.length <= 20
# - word consists of only lowercase English letters.
# - 1 <= abbr.length <= 10
# - abbr consists of lowercase English letters and digits.
# - All the integers in abbr will fit in a 32-bit integer.

def valid_abbreviation(word: str, abbr: str) -> bool:
    """
    Determines whether a given abbreviation `abbr` correctly represents the word `word`.

    This function iterates through both the word and the abbreviation simultaneously, handling:
    - Letter-by-letter matches.
    - Numeric abbreviations (ensuring no leading zeros).

    Parameters:
        word (str): The original word.
        abbr (str): The abbreviation to validate.

    Returns:
        bool: True if `abbr` is a valid abbreviation of `word`, False otherwise.
    """

    word_index, abbr_index = 0, 0  # Pointers for word and abbreviation

    while word_index < len(word) and abbr_index < len(abbr):
        # If characters match, move both pointers forward
        if word[word_index] == abbr[abbr_index]:
            word_index += 1
            abbr_index += 1
            continue

        # If the abbreviation starts with a non-matching letter, return False
        if not abbr[abbr_index].isdigit():
            return False

        # Handle numeric values in abbreviation
        if abbr[abbr_index] == '0':  # Leading zeros are not allowed
            return False

        num = 0
        while abbr_index < len(abbr) and abbr[abbr_index].isdigit():
            num = num * 10 + int(abbr[abbr_index])
            abbr_index += 1

        word_index += num  # Move forward in `word` by `num` positions

    # The abbreviation is valid if both pointers reach the end
    return word_index == len(word) and abbr_index == len(abbr)


# Example Test Cases
print(valid_abbreviation("internationalization", "i12iz4n"))  # Expected: True
print(valid_abbreviation("apple", "a2e"))  # Expected: False

# Complexity Analysis:
# - Time Complexity: O(n), where n is the length of `abbr`. We process each character in `abbr` once.
# - Space Complexity: O(1), as only a few integer variables are used.

