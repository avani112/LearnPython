class Solution:
    def threeSumZero(self, nums: List[int]) -> List[List[int]]:
        rt = []
        if(len(nums) < 3):
            return []
        nums.sort()
        for i in range(len(nums)-1):
            if not(i>0 and nums[i] == nums[i-1]):
                tar = - nums[i]
                hi = len(nums)-1
                l = i+1
                while l < hi:
                    tg = nums[hi] + nums[l]
                    if tg < tar:
                        l+=1
                    elif tg > tar:
                        hi-=1
                    else:
                        rt.append([nums[i] , nums[l] ,nums[hi]])
                        hi -=1
                        l+=1
                        while hi >l and nums[hi+1] == nums[hi]:
                            hi -=1
                        while  hi >l and nums[l-1] == nums[l]:
                            l +=1
        return rt