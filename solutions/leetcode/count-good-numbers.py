class Solution:

    def countGoodNumbers(self, n: int) -> int:
        def countGood(x: int,power: int) -> int:
            if power == 0:
                return 1  
            elif power % 2 == 0:
                return countGood(x * x % MOD,power // 2)
            return x * countGood(x*x % MOD,(power - 1)//2) % MOD

        MOD = 10 ** 9 + 7
        return 5 ** (n % 2) * countGood(4 * 5,n // 2) % MOD