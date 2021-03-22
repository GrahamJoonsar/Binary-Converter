binaryNum = input("Binary number: ")
decimalNum = 0

for i in range(len(binaryNum) - 1, 0, -1):
    decimalNum += binaryNum[i] * (2 ** i)

print(decimalNum)
