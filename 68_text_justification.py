"""
🔵 LeetCode 68. Text Justification

Given an array of words and a maximum width `maxWidth`, format the text so that each line is exactly `maxWidth` characters long and fully justified.

Rules:
- Use a greedy approach to fit as many words per line as possible.
- Distribute extra spaces evenly between words. If uneven, more spaces go to the left.
- The last line is left-justified.

-----------------------------------
Example 1:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]

Example 3:
Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

-----------------------------------
Constraints:
- 1 <= words.length <= 300
- 1 <= words[i].length <= 20
- 1 <= maxWidth <= 100
- words[i].length <= maxWidth
"""

from typing import List

def full_justify(words: List[str], maxWidth: int) -> List[str]:
    """
    ✅ Greedy and Space Distribution

    Idea:
    - Group words into lines with as many as can fit.
    - For each line, distribute spaces evenly.
    - Handle the last line separately (left-justified).

    Time Complexity: O(n), where n is the total number of characters.
    Space Complexity: O(1), excluding output.
    """
    result = []
    i = 0
    while i < len(words):
        # Determine how many words fit in the current line
        line_len = len(words[i])
        j = i + 1
        while j < len(words) and line_len + len(words[j]) + (j - i) <= maxWidth:
            line_len += len(words[j])
            j += 1
        
        # Collect words[i:j]
        line_words = words[i:j]
        num_words = j - i
        spaces_to_distribute = maxWidth - line_len

        # Last line or line with single word: left-justify
        if j == len(words) or num_words == 1:
            line = ' '.join(line_words)
            line += ' ' * (maxWidth - len(line))
        else:
            # Distribute spaces
            space_slots = num_words - 1
            even_spaces = spaces_to_distribute // space_slots
            extra_spaces = spaces_to_distribute % space_slots

            line = ""
            for k in range(space_slots):
                line += line_words[k]
                line += ' ' * (even_spaces + (1 if k < extra_spaces else 0))
            line += line_words[-1]  # last word

        result.append(line)
        i = j
    return result


# ✅ Sample Test Cases
if __name__ == "__main__":
    words1 = ["This", "is", "an", "example", "of", "text", "justification."]
    print("Output:\n", "\n".join(full_justify(words1, 16)))

    words2 = ["What","must","be","acknowledgment","shall","be"]
    print("Output:\n", "\n".join(full_justify(words2, 16)))

    words3 = ["Science","is","what","we","understand","well","enough","to","explain","to","a",
              "computer.","Art","is","everything","else","we","do"]
    print("Output:\n", "\n".join(full_justify(words3, 20)))
