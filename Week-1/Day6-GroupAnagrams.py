"""
Day 6 - Group Anagrams
Leetcode Easy Problem

Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
  All inputs will be in lowercase.
  The order of your output does not matter.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        base_anagrams = {}
        output = []
        
        for index, string in enumerate(strs):
            sortedString = ''.join(sorted(list(string)))
            if sortedString in base_anagrams:
                base_anagrams[sortedString].append(string)
            else:
                base_anagrams[sortedString] = [string]
                
        for anagram_list in base_anagrams.values():
            output.append(anagram_list)
            
        return output
