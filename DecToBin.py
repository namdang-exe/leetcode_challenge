def decToBin(dec: int) -> str:
    # recursive
    
    # example: 20
    # 20/ 2 = 10, rem = 0
    # 10/ 2 = 5, 0
    # 5 / 2 = 2, 1
    # 2/2 = 1, 0
    # 1/2 = 0, 1
    def recursion(num: int, result: str) -> str:
        # base case
        if num == 0: return result
        result = str(num % 2) + result # add in front of the result
        return recursion(num//2, result)
    
    return recursion(dec, "")


def result(num):
    return bin(num)


num = 233
print(decToBin(num))
print("The result is: ")
print(result(num))
