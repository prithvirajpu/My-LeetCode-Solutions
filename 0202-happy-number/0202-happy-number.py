class Solution:
    def isHappy(self, n: int) -> bool:
        def next_val(n):
            total=0
            while n>0:
                n,digit=divmod(n,10)
                total+=digit**2
            return total
        slow=n
        fast=next_val(n)
        while slow!=1 and fast!=slow:
            slow=next_val(slow)
            fast=next_val(next_val(fast))
        return fast==1