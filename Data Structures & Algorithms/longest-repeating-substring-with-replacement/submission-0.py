class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = [0]*26
        start = 0
        maxx = 0
        for ind, item in enumerate(s):
            index = ord(item)-65
            chars[index] += 1
            max_index = chars.index(max(chars))
            currlen = ind - start + 1
            print(chr(max_index+65), max_index, s[start: ind+1], currlen)
            if (currlen - chars[max_index]) <=k:
                pass
            else:
                start_index = ord(s[start])-65
                chars[start_index] -= 1
                start +=1
                currlen -=1
            maxx = max(maxx, currlen)
        return maxx




        