class Solution():
    def findDisappearedNumber(self, nums):
        size = len(nums)
        print(size)
        missing = list()
        j = 1
        nums.sort() # <<-----------------[1 2 2 4 6 6 7]
        for i in nums:
            print(i)
            if i != j:
                missing.append(j)
            del i
            j = j+1
            
        return missing

nums = [4, 6, 2, 6, 7, 2, 1]
print(Solution().findDisappearedNumber(nums))
# output: [3, 5]
