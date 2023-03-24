class Solution:
    # 53. 最大子数组和 
    # 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
    # 输出：6
    # 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
    def maxSubArray(self, nums) -> int:
        if len(nums) < 1:
            return 0
        
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
        res = max(dp)
        return res
    
    # 139. 单词拆分
    # 输入: s = "leetcode", wordDict = ["leet", "code"]
    # 输出: true
    # 解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
    def wordBreak(self, s: str, wordDict) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        for j in range(1, n+1):  # 先遍历背包，因为顺序影响结果
            for word in wordDict:  # 再遍历物品
                if j >= len(word):
                    if s[j-len(word): j] == word and dp[j-len(word)]:
                        dp[j] = True
        print(dp)
        return dp[n]
    
    # 198. 打家劫舍 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
    # 输入：[1,2,3,1]
    # 输出：4
    # 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。 偷窃到的最高金额 = 1 + 3 = 4 。
    def rob(self, nums) -> int:
        n = len(nums)
        if n < 1:
            return 0

        dp = [0] * (n+2)
        for i in range(2, n+2):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-2])
        # print(dp)
        return dp[-1]

    # 213. 打家劫舍 II 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
    # 输入：nums = [2,3,2]
    # 输出：3
    # 解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
    def rob(self, nums) -> int:
        n = len(nums)
        if n < 1:
            return 0
        if n < 4:
            return max(nums)
        
        def get_result(nums):
            n = len(nums)
            dp = [0] * (n+2)
            for i in range(2, n+2):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i-2])
            return dp[-1]

        result1 = get_result(nums[1:])
        result2 = get_result(nums[:-1])
        return max(result1, result2)

    # 279. 完全平方数
    # 输入：n = 12
    # 输出：3 
    # 解释：12 = 4 + 4 + 4
    def numSquares(self, n: int) -> int:
        dp = [n+1] * (n+1)
        dp[0] = 0
        c = int(pow(n, 0.5)) + 1

        for i in range(c):
            coin = i*i
            for j in range(coin, n+1):
                dp[j] = min(dp[j], dp[j-coin] + 1)
        print(dp)
        return -1 if dp[n] == n+1 else dp[n]

    # 300. 最长递增子序列
    # 输入：nums = [10,9,2,5,3,7,101,18]
    # 输出：4
    # 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
    def lengthOfLIS_dp1(self, nums) -> int:
        n = len(nums)
        if n < 2:
            return n

        dp = [1] * n
        for i in range(n)[::-1]:
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
    
    # 322. 零钱兑换 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。你可以认为每种硬币的数量是无限的
    # 输入：coins = [1, 2, 5], amount = 11
    # 输出：3 
    # 解释：11 = 5 + 5 + 1
    def coinChange2(self, coins, amount: int) -> int:
        if len(coins) < 1 or amount < 0:
            return -1
        if amount == 0:
            return 0
        
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if i-coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i-coin] + 1)
        return -1 if dp[amount] == amount+1 else dp[amount]
                
    def coinChange(self, coins, amount: int) -> int:
        if len(coins) < 1 or amount < 0:
            return -1
        if amount == 0:
            return 0
        
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin] + 1)
        return -1 if dp[amount] == amount+1 else dp[amount]
    
    # 343. 整数拆分 给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。
    # 输入: n = 10
    # 输出: 36
    # 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
    def integerBreak(self, n: int) -> int:
        if n < 2:
            return 0
        if n == 2:
            return 1

        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 0
        dp[2] = 1

        for i in range(3, n+1):
            for j in range(1, i):
                # dp[i] = max(dp[i], j*dp[i-j])
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
        print(dp)
        return dp[n]
    
    # 377. 组合总和 Ⅳ 给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。
    # 输入：nums = [1,2,3], target = 4
    # 输出：7
    # 解释：
    # 所有可能的组合为：
    # (1, 1, 1, 1)
    # (1, 1, 2)
    # (1, 2, 1)
    # (1, 3)
    # (2, 1, 1)
    # (2, 2)
    # (3, 1)
    # 请注意，顺序不同的序列被视作不同的组合。
    def combinationSum4(self, nums, target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1

        for j in range(1, target+1):
            for num in nums:
                if j - num>=0:
                    dp[j] += dp[j-num]
        # print(dp)
        return dp[target]

    # 416. 分割等和子集
    # 输入：nums = [1,5,11,5]
    # 输出：true
    # 解释：数组可以分割成 [1, 5, 5] 和 [11] 。
    def canPartition(self, nums) -> bool:
        n = len(nums)
        if n < 2:
            return False

        target = sum(nums) // 2
        if 2 * target != sum(nums):
            return False

        dp = [0] * (target + 1)
        for i in range(len(nums)):
            for j in range(target, nums[i]-1, -1):
                dp[j] = max(dp[j], dp[j-nums[i]] + nums[i])
        # print(dp)
        return dp[target] == target

    # 474. 一和零
    # 输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
    # 输出：4
    # 解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
    # 其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。
    def findMaxForm(self, strs, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]	# 默认初始化0
        # 遍历物品
        for str in strs:
            ones = str.count('1')
            zeros = str.count('0')
            # 遍历背包容量且从后向前遍历！
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        return dp[m][n]

    # 494. 目标和
    # 输入：nums = [1,1,1,1,1], target = 3
    # 输出：5
    # 解释：一共有 5 种方法让最终目标和为 3 。
    # -1 + 1 + 1 + 1 + 1 = 3
    # +1 - 1 + 1 + 1 + 1 = 3
    # +1 + 1 - 1 + 1 + 1 = 3
    # +1 + 1 + 1 - 1 + 1 = 3
    # +1 + 1 + 1 + 1 - 1 = 3
    def findTargetSumWays(self, nums, target: int) -> int:
        sums = sum(nums)
        # !!! abs(target) > sums
        if abs(target) > sums or (sums + target) % 2 == 1: return 0

        left = (sums + target) // 2
        
        dp = [0] * (left + 1)
        dp[0] = 1

        for i in range(len(nums)):
            for j in range(left, nums[i]-1, -1):
                dp[j] += dp[j-nums[i]]
        # print(dp)
        return dp[-1]

    # 516. 最长回文子序列
    # 输入：s = "bbbab"
    # 输出：4
    # 解释：一个可能的最长回文子序列为 "bbbb" 。
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n
        
        dp = [[0 for i in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n)[::-1]:
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        # print(dp)
        return dp[0][n-1]

    # 518. 零钱兑换 II
    # 输入：amount = 5, coins = [1, 2, 5]
    # 输出：4
    # 解释：有四种方式可以凑成总金额：
    # 5=5
    # 5=2+2+1
    # 5=2+1+1+1
    # 5=1+1+1+1+1
    def change(self, amount: int, coins) -> int:

        dp = [0] * (amount+1)
        dp[0] = 1
        for coin in coins:
            for j in range(coin, amount+1):
                dp[j] += dp[j-coin]
        print(dp)
        return dp[amount]

    # 583. 两个字符串的删除操作
    # 输入: word1 = "sea", word2 = "eat"
    # 输出: 2
    # 解释: 第一步将 "sea" 变为 "ea" ，第二步将 "eat "变为 "ea"
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m + n < 2:
            return m + n
        
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
                    # dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 2)
        # print(dp)
        return dp[-1][-1]
    
    # 647. 回文子串
    # 输入：s = "abc"
    # 输出：3
    # 解释：三个回文子串: "a", "b", "c"
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n
        
        dp = [[0 for i in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if j - i == 1:
                    dp[i][j] = 1 if s[i] == s[j] else 0
                else:
                    dp[i][j] = dp[i+1][j-1] and 1 if s[i] == s[j] else 0
        # print(dp)
        return sum([sum(i) for i in dp])

    # 718. 最长重复子数组
    # 输入：nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
    # 输出：3
    # 解释：长度最长的公共子数组是 [3,2,1] 。
    def findLength(self, nums1, nums2) -> int:
        m, n = len(nums1), len(nums2)
        if m + n < 2:
            return 0
        
        dp = [[0]*(n+1) for j in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
        # print(dp)
        return max([max(dp[i]) for i in range(m+1)])

    # 1049. 最后一块石头的重量 II
    # 输入：stones = [2,7,4,1,8,1]
    # 输出：1
    # 解释：
    # 组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
    # 组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
    # 组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
    # 组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。
    def lastStoneWeightII(self, stones) -> int:
        n = len(stones)
        if n < 1:
            return 0
        if n == 1:
            return stones[0]

        target = sum(stones) // 2
        dp = [0] * (target + 1)
        for i in range(len(stones)):
            for j in range(target, stones[i]-1, -1):
                dp[j] = max(dp[j], dp[j-stones[i]] + stones[i])
        # print(dp)
        return sum(stones) - dp[target] - dp[target]

    # 1143. 最长公共子序列
    # 输入：text1 = "abcde", text2 = "ace" 
    # 输出：3  
    # 解释：最长公共子序列是 "ace" ，它的长度为 3 。
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        if m + n < 2:
            return 0

        dp = [[0]*(n+1) for i in range(m + 1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max([dp[i-1][j], dp[i][j-1]])
        # print(dp)
        return dp[-1][-1]
    
    # 1218. 最长定差子序列
    # 输入：arr = [1,2,3,4], difference = 1
    # 输出：4
    # 解释：最长的等差子序列是 [1,2,3,4]。
    def longestSubsequence_dp(self, arr, difference: int) -> int:
        m = len(arr)
        if m < 2:
            return m
        
        dp = [1] * m
        for i in range(m)[::-1]:
            for j in range(i+1, m):
                if arr[i] + difference == arr[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
    
    
