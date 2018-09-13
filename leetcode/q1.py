nums = [2,7,11,15]

target = 9

# fn1

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        aa = self.getnum(nums, target)
        if aa != None:
            return [nums.index(aa[0]),nums.index(aa[1],nums.index(aa[0]))]
        return None


    def getnum(self,nums, target):
        list2 = nums[:]
        list2.remove(list2[0])
        res = []
        if len(list2)<1:
            return None
        for a in (x for x in list2):
            if a + nums[0] == target:
                res = [nums[0],a]
                break
        if len(res)>0:
            return res
        return self.getnum(list2,target)
        


test = Solution()

print(test.twoSum(nums,target))


# fn2
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in xrange(len(nums) - 1):
            for j in xrange(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# fn3

"""
由于题目说了有且只有唯一解，可以考虑两遍扫描求解：第一遍扫描原数组，将所有的数重新存放到一个dict中，该dict以原数组中的值为键，原数组中的下标为值；
第二遍扫描原数组，对于每个数nums[i]查看target-nums[i]是否在dict中，若在则可得到结果。 
当然，上面两遍扫描是不必要的，一遍即可，详见代码。
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        keys = {}
        for i in xrange(len(nums)):
            if target - nums[i] in keys:
                return [keys[target - nums[i]], i]
            if nums[i] not in keys:
                keys[nums[i]] = i