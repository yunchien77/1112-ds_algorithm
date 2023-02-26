# HW1 將十進位數字轉換成二進位與16進位

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
  
  ![](https://github.com/yunchien77/ds_algorithm/blob/main/hw1/exeresult/234.png)
  
  - 輸入數字317


  - 輸入數字55
