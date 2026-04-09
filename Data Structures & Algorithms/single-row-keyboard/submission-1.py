class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        dic= {}
        for ind, item in enumerate(keyboard):
            dic[item] = ind
        start = 0
        summ = 0
        for i in range(len(word)):
            target = dic[word[i]]
            # print(target, )
            summ += abs(target-start)
            start = target
        return summ
