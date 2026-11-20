class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0

        num1_int = []
        num2_int = []
        mult = 1
        for i in range(len(num1)-1, -1, -1):
            num1_int.append(int(num1[i])*mult)
            mult*=10
        mult = 1
        for i in range(len(num2)-1, -1, -1):
            num2_int.append(int(num2[i])*mult)
            mult*=10
        
        for num_i in num1_int:
            for num_j in num2_int:
                res += num_i * num_j

        return str(res)