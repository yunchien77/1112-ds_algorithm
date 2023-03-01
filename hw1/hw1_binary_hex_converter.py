#十進位轉二進位
def decimal_to_binary(decimalNum):
    binaryNum = ""
    while decimalNum >= 1:
        binaryNum = str(decimalNum % 2) + binaryNum
        decimalNum //= 2
    return binaryNum

#二進位轉十六進位
def binary_to_hex(binaryNum):
    hex_digits = "0123456789ABCDEF"  #十六進位換算表
    hexNum = ""
    #補齊4的倍數個0
    while len(binaryNum) % 4 != 0:
        binaryNum = "0" + binaryNum
    #每4位二進制數字作為一組轉換為十六進制數字
    for i in range(0, len(binaryNum), 4):
        hex_index = 0
        for j in range(4):  # j = 0~3
            hex_index += int(binaryNum[i+j]) * 2**(3-j)
        hexNum += hex_digits[hex_index]
    return hexNum


def main():
    while(1):
        decimalNum = int(input("Enter a decimal number(0~255): "))
        #判斷輸入的數字是否在有效範圍
        if decimalNum < 0 or decimalNum > 255:
            print("The number is out of range\nPlease enter again\n")
            continue
        break
    
    binaryNum = decimal_to_binary(decimalNum)
    hexNum = binary_to_hex(binaryNum)
    print("Binary number: ", binaryNum)
    print("Hexadecimal number: ", hexNum)

if __name__ == '__main__':
    main()
