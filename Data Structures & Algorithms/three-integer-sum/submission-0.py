class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # -4 -1 -1 0 1 2
        # store result triplets in a set at first to deduplicate, convert to list at the end
        # sort nums
        # for loop. for each i, set j to i+1 and k to the final index (len-1)
        # do the following in a while j<k
        # if the sum of the three is < 0, increment j, otherwise decrement k.
        # each time the sum is 0, add to result set, and do j+=1 and k-=1.
        
        sorted_nums = list(sorted(nums))
        result = set() # convert to list later
        n = len(nums)

        for i in range(n):
            a = sorted_nums[i]

            j = i+1
            k = n-1

            while j < k:
                b = sorted_nums[j]
                c = sorted_nums[k]
                sum_ = a + b + c
                if sum_ > 0:
                    k -= 1
                elif sum_ < 0:
                    j += 1
                else:
                    result.add((a, b, c))
                    j += 1
                    k -= 1
        
        return [list(triplet) for triplet in result]