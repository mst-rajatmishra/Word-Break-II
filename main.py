from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)  # Convert list to set for O(1) lookups
        memo = {}
        
        def backtrack(start: int) -> List[str]:
            if start in memo:  # Return already computed result
                return memo[start]
            
            if start == len(s):  # Base case: reached the end of the string
                return [""]  # Return a list with an empty string
            
            sentences = []
            
            # Try every possible end index for the substring
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:  # If the substring is a valid word
                    # Recurse to find valid sentences for the rest of the string
                    for sentence in backtrack(end):
                        if sentence:  # If the sentence is not empty
                            sentences.append(word + " " + sentence)
                        else:  # If the sentence is empty, just add the word
                            sentences.append(word)
            
            memo[start] = sentences  # Store the result in the memoization dictionary
            return sentences
        
        return backtrack(0)  # Start backtracking from the beginning of the string

