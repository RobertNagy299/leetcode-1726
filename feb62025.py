# 1726. Tuple with same product - Medium
# Solved after using the two hints. Beats 90.05%. Runtime: 307ms
# Worst case time complexity: 0.5*O(n^2)
from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4 :
            return 0
        productsFrequency = {}
        answer = 0
        for i in range(n):
            for j in range(i+1, n):
                product = nums[i] * nums[j]
                if product in productsFrequency:
                    productsFrequency[product] += 1
                else:
                    productsFrequency[product] = 1
        
        
        for item in productsFrequency.items():
            if item[1] > 1:
                answer += 8 * ((item[1] * (item[1] - 1)) // 2)


        return answer



s = Solution()
nums = [2,3,4,6]
print(s.tupleSameProduct(nums))   

print("Next case")
nums = [1,2,4,5,10]
print(s.tupleSameProduct(nums))   
