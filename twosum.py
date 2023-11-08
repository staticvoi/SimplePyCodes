# nums=[2,7,11,15]
# target = 9

# nums=[3,2,4]
# target = 6
# index out of bound for this
nums=[3,2,3]
target = 6
def twoSum(nums, target):
    for i in range(len(nums)):
        sum = nums[i]+nums[i+1]
        if sum == target:
            return [i,i+1]
                
# output = twoSum(nums,target)
# print(output)


nums1=[3,2,3]
target1 = 6
def twoSum1(nums, target):
    l=len(nums1)
    
    for i in range(l):
        comp1=map(comp,i)
        comp[target1 - nums1[i]]=i


output1 = twoSum1(nums1,target1)
print(output1)

