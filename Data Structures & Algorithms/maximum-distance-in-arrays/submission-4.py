class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        smallest = arrays[0][0]
        largest = arrays[1][-1]
        if (arrays[1][-1] -arrays[0][0]) > (arrays[0][-1] -arrays[1][0]):
            largest = arrays[1][-1]
            smallest = arrays[0][0]
        else:
            largest = arrays[0][-1]
            smallest = arrays[1][0]
        for i in range(2, len(arrays)):
            small, large = arrays[i][0], arrays[i][-1]
            if small<smallest and large>largest:
                if (smallest-small)>(large-largest):
                    smallest = small
                else:
                    largest = large
            else:
                smallest = min(smallest, small)
                largest = max(largest, large)
        print(largest, smallest)
        return largest -smallest

            
        