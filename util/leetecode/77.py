class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        def backtrack(n, k, startIdx):
            # print('backtrack', n, k, startIdx)
            if len(path) == k:
                # print(n,k,path[:])
                res.append(path[:])
                return
            last_start_idx = n - (k - len(path)) + 1 
            for i in range(startIdx, n + 1):
                path.append(i)
                backtrack(n, k, i + 1)
                path.pop()
            
        backtrack(n, k, 1)
        return res
