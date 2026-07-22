class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = { }
            # Go through each word
        for word in strs:

            # Sort the letters to make a common key
            key = "".join(sorted(word))

            # If this key is new, create an empty list
            if key not in groups:
                groups[key] = []

            # Add the original word to its group
            groups[key].append(word)

        # Return only the grouped words
        return list(groups.values())

