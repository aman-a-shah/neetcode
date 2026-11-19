class Solution:
    def candy(self, ratings: List[int]) -> int:
        # children
        # higher rating => more candy than neighbour

        # num candies
        # max_candies = longest strictly increasing sequence
        # min_candies = 1

        # [2, 1, 2]
        # [2, 3, 3] -> [0, 1, 1] -> [1, 2, 1] 

        # build out 0's array
        arr = [1] * len(ratings)
        # move up by 1 or reset to 0 based on prev
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                arr[i] = arr[i-1] + 1
        # right to left
        for i in range(len(arr)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                arr[i] = max(arr[i], arr[i+1] + 1)
        return sum(arr)

        # [4, 3, 2, 1] -> [0, -1, -2, -3]