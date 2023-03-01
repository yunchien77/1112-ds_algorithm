# HW1 將十進位數字轉換成二進位與16進位
## language: C
* ### 程式碼
```c
#include <stdio.h>

//convert decimal to binary
void decimalToBinary(int decimalNum) {
    int binaryNum[8];
    int i = 0;
    while (decimalNum > 0) {
        binaryNum[i] = decimalNum % 2;
        decimalNum = decimalNum / 2;
        i++;
    }
    printf("Binary number: ");
    for (int j = i - 1; j >= 0; j--) {
        printf("%d", binaryNum[j]);
    }
    printf("\n");
}

//convert decimal to hexadecimal
void decimalToHexadecimal(int decimalNum) {
    int hexNum[8];
    int i = 0;
    while(decimalNum > 0){
        hexNum[i] = decimalNum % 16;
        decimalNum = decimalNum / 16;
        i++;
    }
    printf("Hexadecimal number: ");
    for(int j = i - 1; j >= 0; j--){
        if (hexNum[j] < 10){
            printf("%d", hexNum[j]);
        } 
        else{
            printf("%c", hexNum[j] + 55);
        }
    }
    printf("\n");
}

int main(){
    int decimalNum;
    while(1){
        printf("Enter a decimal number(0~255): ");
        scanf("%d", &decimalNum);
        if(decimalNum < 0 || decimalNum > 255){
            printf("The number is out of range\nPlease enter again\n");
        }
        else{
            break;
        }
    }
    
    decimalToBinary(decimalNum);
    decimalToHexadecimal(decimalNum);

    return 0;
}
```

* ### 執行結果
  - 輸入數字234
  
    ![](https://github.com/yunchien77/ds_algorithm/blob/main/hw1_binary_hex_converter/exeresult/234.png)
  
  - 輸入數字317和55
  
    ![](https://github.com/yunchien77/ds_algorithm/blob/main/hw1_binary_hex_converter/exeresult/317_and_55.png)
  

## language: Python
* ### 程式碼
```python
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
```

* ### 執行結果
  - 輸入數字234
  
    ![](https://github.com/yunchien77/ds_algorithm/blob/main/hw1_binary_hex_converter/exeresult/234_in_py.png)
  
  - 輸入數字317和55
  
    ![](https://github.com/yunchien77/ds_algorithm/blob/main/hw1_binary_hex_converter/exeresult/317_and_55_in_py.png)
