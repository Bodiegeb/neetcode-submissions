from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answers=[]
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while j<k:
                c = nums[j] + nums[k]
                if(nums[i] + c == 0):
                    current=[nums[i],nums[j],nums[k]]
                    if(current not in answers):
                        answers.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                elif c < -nums[i]:
                    j+=1
                else:
                    k-=1
        return answers

        