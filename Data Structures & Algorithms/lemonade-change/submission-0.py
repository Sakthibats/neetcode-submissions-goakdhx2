class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        index = 0
        for b in bills:
            if b == 5:
                five += 1
            if b == 10:
                ten += 1 
            print(f'The customer now is paying bill {bills[index]}')
            index += 1
            print(f'The number of 5 bills are {five}, 10 bills are {ten}')    
            change = b - 5
            print(f'The change right now is {change}')
            if change == 5:
                if five > 0:
                    five -= 1
                else:
                    return False
            elif change == 15:
                if five > 0 and ten > 0:
                    five, ten = five - 1, ten - 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
            print(f'The number of 5 bills are {five}, 10 bills are {ten}')
        return True