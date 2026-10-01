class Solution:

    def encode(self, strs: List[str]) -> str:
        #basically we are given a list of strings, we have to make a single string out of all the strings, ie concatenate them
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res


    def decode(self, s: str) -> List[str]:
        #now we have the string res, we need to convert that string into list, back to the orignal list we were given in encode func. I have split each element in the array by "," and added it to the final string in encode func. 
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            #when we encounter "," we add the string to the result list.
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res 