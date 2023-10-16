class Solution:
    def helper(self, n: int):
        res = ""
        if n % 3 == 0:
            res = res + "Fizz"
        if n % 5 == 0:
            res = res + "Buzz"
        if len(res) == 0:
            return str(n)
        return res

    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(n):
            result.append(self.helper(i+1))
        return result
