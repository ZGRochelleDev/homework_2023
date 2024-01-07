#how to do this in a single for loop?
class Solution:

    def subtractProductAndSum(self, n):

        # convert the int into a string, then a list, so that it's easier to work with
        str_lst = list(str(n))

        # get sum
        prod_total = 1
        sum_total = 0
        for num in str_lst:
            sum_total = sum_total + int(num) 
            prod_total = prod_total * int(num) 

        # get product
        # prod_total = int(str_lst[0])
        # for i in range(1, len(str_lst)):
        #     prod_total = prod_total * int(str_lst[i])

        return prod_total - sum_total

        #iterating through twice
        #possible to do it once?

n = 234
#n = 4421

s = Solution()
ans = s.subtractProductAndSum(n)

print(f"Solution = {ans}")
