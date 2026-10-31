class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        side = sum(matchsticks) / 4
        if side != int(side):
            return False

        matchsticks.sort()

        def dfs(sum_so_far, used, sides_done, start):

            if len(used) == len(matchsticks):
                return sum_so_far == side and sides_done == 3
            
            if sum_so_far == side:
                return dfs(0, used, sides_done + 1, 0)
            
            if sum_so_far > side:
                return False
            
            i = start
            acc = set()
            prev = -1
            while i < len(matchsticks) and matchsticks[i] + sum_so_far <= side:
                if i not in used and matchsticks[i] != prev:
                    used.add(i)
                    acc.add(dfs(sum_so_far + matchsticks[i], used, sides_done, i+1))
                    used.remove(i)
                    prev = matchsticks[i]
                i += 1
            
            return any(acc)

        return dfs(0, set(), 0, 0)