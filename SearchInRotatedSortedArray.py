class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(l,h):
            while l<=h:
                mid = (l+h) // 2
                if target == nums[mid]:
                    return mid
                elif target > nums[mid]:
                    l = mid + 1
                elif target < nums[mid]:
                    h = mid - 1
            return -1
        
        minIdx = nums.index(min(nums))
        
        bs1 = bs(0,minIdx-1)
        bs2 = bs(minIdx,len(nums)-1)
        
        if bs1 == bs2 == -1:
            return -1
        else:
            return max(bs1,bs2)
