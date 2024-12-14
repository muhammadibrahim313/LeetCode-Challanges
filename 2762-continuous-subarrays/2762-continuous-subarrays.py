from heapq import heappush, heappop
from typing import List

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        count = 0
        left = 0
        right = 0
        max_heap = []  # To store elements as negative for max heap
        min_heap = []  # To store elements for min heap
        
        while right < len(nums):
            heappush(max_heap, (-nums[right], right))  # Push negated value for max heap
            heappush(min_heap, (nums[right], right))  # Push actual value for min heap
            
            # Shrink window if difference exceeds 2
            while max_heap and min_heap and (-max_heap[0][0]) - min_heap[0][0] > 2:
                left += 1
                # Remove elements outside the window
                while max_heap and max_heap[0][1] < left:
                    heappop(max_heap)
                while min_heap and min_heap[0][1] < left:  # Fix: was `max_heap[0][1]`
                    heappop(min_heap)
            
            # Count all subarrays ending at `right`
            count += (right - left + 1)
            right += 1
        
        return count
