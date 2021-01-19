# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 21:24:13 2021

"""

from itertools import combinations
from typing import List

"""
first_try timeout

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for comb in list(combinations(nums, 3)):
            if sum(comb) == 0 and sorted(comb) not in ans:
                ans.append(sorted(list(comb)))
        return ans
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return ans
        
nums = [1,-1,-1,0]
ret = Solution()
print(ret.threeSum(nums))

"""
브루트 포스는 O(n^3)인 무식한 방법
숫자 하나를 고정시켜 두면 그나마 O(n^2)인 방법으로 풀이가 가능
다른 사람들은 binary search로 풀었던데 그럼 O(nlogn)쯤 될듯?
"""
"""
0을 만들기 위해서는 셋 모두 0이거나 반드시 한 숫자는 음수여야 한다.
숫자 n이 정해졌을 때, 나머지 두 수로 -n 만큼을 만들어야 합은 0이 된다.
두 숫자의 최댓값은 -n/2이고, 최솟값은 -n-nums[-1]이다.
따라서 bisect_left로 최솟값과 최댓값의 범위를 구한 후,
두 숫자가 들어갈 수 있는 범위 내에서 한 숫자를 정한 후 나머지 숫자가 count에 있는지 확인한다.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
      # 예외처리
        # a) length of list less than three
        # b) all poaitive or all negative
        if len(nums) < 3 or min(nums) > 0 or max(nums) < 0:
            return []
        res = []
   
        # Dictionary of numbers and their frequency
        count = collections.Counter(nums)
        
        '''
        # This is what the Counter API does
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        '''
		
		# Sort the list
        nums = sorted(count)
        
        # Find two pairs for negative numbers
        for idx in range(len(nums)):
            
            if idx+1 < len(nums) and nums[idx+1] == nums[idx]:
                continue
                
            num = nums[idx]
            if num > 0:
                break

            # Target for sum of the two pairs
            two_sum = - num

            # Max of the two can't be bigger than half of target
            # Min of the two is when one of them is the max in the list
            num2_min, num2_max = two_sum - nums[-1], two_sum / 2

            # The start of the search is the min index 
            # which can't be less than current index
            # because the list is sorted
            # and the end of the search is the max index
            # which is bigger than min index
            i = bisect_left(nums, num2_min, idx + 1)
            j = bisect_left(nums, num2_max, i)
            
            # Marching through subset of the list
            # to find two numbers with sum equal to target 
            for num2 in nums[i:j]:
                
                # pick the second number and calculate the third
                num3 = two_sum - num2
                
                # if the third exits in the count
                # we have found the answer 
                if num3 in count:
                    res.append((num, num2, num3))
        
        # For edge cases of repeated numbers
        for num in nums:

            if count[num] > 1:

                # Edge case of three zeros
                if num == 0 and count[num] >= 3:
                    res.append((num, num, num))

                # Edge case of repeated number with exited matching in list
                elif num != 0 and 0 - 2 * num in count:
                    res.append((num, num, 0 - 2 * num))

        return res
"""
