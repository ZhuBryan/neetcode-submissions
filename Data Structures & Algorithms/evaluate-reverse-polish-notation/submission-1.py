class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for el in tokens:
            if el == "+":
                nums.append(nums.pop() + nums.pop())
            elif el == "-":
                nums.append(- (nums.pop() - nums.pop()))
            elif el == "*":
                nums.append(nums.pop() * nums.pop())
            elif el == "/":
                d = nums.pop()
                n = nums.pop()
                nums.append(int(n/d))
            else: 
                nums.append(int(el))
        return nums.pop()