class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fin = []
        relist = sorted([(position[i], speed[i]) for i in range(len(speed))], key=lambda x: x[0])
        durations = [(target-item[0])/item[1] for item in relist]
        while durations:
            curr = durations.pop()
            if not fin:
                fin.append(curr)
            elif curr>fin[-1]:
                fin.append(curr)

        return len(fin)
