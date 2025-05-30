def FindDigitPowerSum(n):
    num=0
    for i,digit in enumerate(str(n)):
        num += int(digit) **(i+1)
    return num
n = int(input())
print(FindDigitPowerSum(n))