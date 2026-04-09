class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        count=0
        temp = ""
        for i in abbr:
            if i.isdigit():
                temp+=i
                if temp[0]=="0":
                    return False
                if (count+int(temp))> len(word):
                    return False
            else:
                if temp!="":
                    count += int(temp)
                    temp=""
                print(count)
                if count>=len(word):
                    return False
                if word[count]!= i:
                    return False
                count+=1
            # print(count, i)
        return True

        