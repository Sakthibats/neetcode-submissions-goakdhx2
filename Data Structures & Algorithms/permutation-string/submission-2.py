class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        corrchars = [0]*26
        currchars = [0]*26
        for i in range(len(s1)):
            items1 = s1[i]
            charind = ord(items1)-97
            corrchars[charind] += 1
            items2 = s2[i]
            charind = ord(items2)-97
            currchars[charind] += 1
        if currchars==corrchars:
            return True
        for index, item in enumerate(s2[:-len(s1)]):
            currchars[ord(item)-97] -= 1
            currchars[ord(s2[index+len(s1)])-97] += 1
            if currchars==corrchars:
                return True
        return False

            


        