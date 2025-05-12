"""
🔵 LeetCode 824: Goat Latin

You are given a string `sentence` that consists of words separated by spaces. Each word contains only uppercase 
and lowercase letters. The task is to convert the sentence into "Goat Latin" following these rules:

1. If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u', in either case), append "ma" to the end of the word.
   For example, "apple" becomes "applema".
2. If a word begins with a consonant, remove the first letter, append it to the end, and then add "ma".
   For example, "goat" becomes "oatgma".
3. Append one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
   That is, the first word gets "a", the second gets "aa", the third gets "aaa", and so on.

Return the final sentence representing the conversion to Goat Latin.

-----------------------------------
Example 1:
Input: sentence = "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
Explanation:
    - "I" starts with a vowel, so it becomes "I" + "ma" + "a" = "Imaa".
    - "speak" starts with a consonant, so it becomes "peak" + "s" + "ma" + "aa" = "peaksmaaa".
    - "Goat" becomes "oatGma" + "aaa" = "oatGmaaaa".
    - "Latin" becomes "atinLma" + "aaaaa" = "atinLmaaaaa".

Example 2:
Input: sentence = "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"

-----------------------------------
Constraints:
    - 1 <= sentence.length <= 150
    - sentence consists of English letters and spaces.
    - sentence has no leading or trailing spaces.
    - All the words in sentence are separated by a single space.
"""

def toGoatLatin(sentence: str) -> str:
    """
    Converts the input sentence to Goat Latin.

    Approach:
      - Split the sentence into words.
      - For each word, check if the first character is a vowel.
        * If yes, append "ma" to the word.
        * If no, remove the first character, append it to the end, and then add "ma".
      - Append a number of 'a' characters equal to the word's index (starting at 1) to the end of each word.
      - Join the transformed words with a space and return the resulting string.

    Time Complexity: O(n), where n is the total number of characters in the sentence.
    Space Complexity: O(n), for storing the split words and the resulting transformed words.

    Args:
        sentence (str): The input sentence to convert.
    
    Returns:
        str: The sentence converted into Goat Latin.
    """
    vowels = set("aeiouAEIOU")
    words = sentence.split()
    result = []
    
    for i, word in enumerate(words, 1):
        # Check if the first letter is a vowel
        if word[0] in vowels:
            transformed = word + "ma"
        else:
            transformed = word[1:] + word[0] + "ma"
        
        # Append i copies of "a" (word index starts at 1)
        transformed += "a" * i
        result.append(transformed)
    
    return " ".join(result)

# Sample Test Cases
if __name__ == "__main__":
    # Example 1:
    sentence1 = "I speak Goat Latin"
    print("Example 1 Output:", toGoatLatin(sentence1))
    # Expected: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
    
    # Example 2:
    sentence2 = "The quick brown fox jumped over the lazy dog"
    print("Example 2 Output:", toGoatLatin(sentence2))
    # Expected: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"

# ------------------------------------------------
# ✅ Time Complexity: O(n), where n is the total number of characters in the sentence.
# ✅ Space Complexity: O(n), for storing the split words and the resulting transformed words.
