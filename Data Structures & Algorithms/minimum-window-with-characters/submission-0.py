class Solution:
    def minWindow(self, s: str, t: str) -> str:
                    
        if len(t)>len(s):
            return ""
        slide = len(t)
        arr = [0]*52
        current = [0]*52
        fin = set()
        for i in t:
            if i.islower():
                arr[ord(i)-97+26] +=1
                fin.add(ord(i)-97+26)
            else:
                arr[ord(i)-65] += 1
                fin.add(ord(i)-65)
        fin = list(fin)

        def same(curr):
            for i in fin:
                if curr[i]<arr[i]:
                    return False
            return True
        
        windowsize = len(t)
        while windowsize<=len(s):
            curr = [0]*52
            for i in range(windowsize):
                item = s[i]
                if item.islower():
                    curr[ord(item)-97+26] +=1
                else:
                    curr[ord(item)-65] += 1
            if same(curr):
                return s[:windowsize]
            for i in range(0, len(s)-windowsize):
                front, back = s[i], s[i+windowsize]
                if front.islower():
                    curr[ord(front)-97+26] -=1
                else:
                    curr[ord(front)-65] -= 1
                if back.islower():
                    curr[ord(back)-97+26] +=1
                else:
                    curr[ord(back)-65] += 1
                
                if same(curr):
                    return s[i+1:i+windowsize+1]
            windowsize+=1
        return ""