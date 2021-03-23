def convertBtoD(binaryNum, mode):
    binaryNum = str(binaryNum)
    decimalNum = 0
    power = 0

    for i in range(len(binaryNum) -1, -1, -1):
        decimalNum += int(binaryNum[i]) * (2 ** power)
        power += 1

    if mode == "print":
        print(decimalNum)
    if mode == "return":
        return decimalNum

def convertDtoB(integerNum, mode):
    binaryNum = ""
    integerNum = int(integerNum)

    while integerNum != 0:
        string = str(integerNum % 2)
        binaryNum += string
        integerNum = integerNum // 2

    if mode == "print":
        print(binaryNum[::-1])
    if mode == "return":
        return binaryNum[::-1]
    

if __name__ == "__main__":
    print("Binary to Integer: 1\nInteger to Binary: 2")
    choice = input(">>> ")
    if choice == "1":
        bNum = input("Binary Number: ")
        convertBtoD(bNum, "print")
    elif choice == "2":
        iNum = input("Integer Number: ")
        convertDtoB(iNum, "print")
    input("Press enter to exit ")

