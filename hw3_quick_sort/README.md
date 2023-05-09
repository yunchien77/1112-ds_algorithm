# HW1 將十進位數字轉換成二進位與16進位
## language: C
* ### 程式碼
```c
#include <stdio.h>
//declare function
void quickSort(int arr[], int left, int right);

int main(){
    int size;  //declare a viriable to save the length of array
    printf("Please enter a number for a length of array:\n");
    scanf("%d", &size);
    
    int arr[size];  //declare a array for the numbers you want to sort
    printf("Please enter the numbers of array:\n");
    for(int i = 0; i < size; i++){
        scanf("%d", &arr[i]);
    }
    /*
    for(int i = 0; i < size; i++){
        printf("%d ", arr[i]);
    }
    */
    
    //quick sort
    quickSort(arr, 0, size-1);

    //print result
    printf("\nSorted array:\n");
    for(int i = 0; i < size; i++){
        printf("%d ", arr[i]);
    }
    //exit program
    return 0;
}
//definition function
void quickSort(int arr[], int left, int right){
    if(left >= right) return; // base case
    int i = left;   //left pointer(左指標)
    int j = right;  //right pointer(右指標)
    int pivot = arr[left];   //standard(基準點)
    
    while(i != j){  //left and right ponter are not on the same location 
        //若左指標小於右指標且右指標指在陣列的值大於基準點，則右指標左移(從右向左找第一個小於基準點的數)
        while(i < j && arr[j] >= pivot) j--;  
        //若左指標小於右指標且左指標指在陣列的值小於基準點，則左指標右移(從左向右找第一個大於基準點的數)
        while(i < j && arr[i] <= pivot) i++;
        if(i < j){  //直到右指標找到比基準點小的數值，左指標找到比基準點大的數值，將兩樹值交換位置
            int temp = arr[j];  
            arr[j] = arr[i];
            arr[i] = temp;
        }
    }
    arr[left] = arr[i];
    arr[i] = pivot;  
    //recursive function(分別針對左右子陣列繼續做quick sort)
    quickSort(arr, left, i-1);    //left arr
    quickSort(arr, i+1, right);   //right arr
}
```

* ### 執行結果
  > - 輸入長度10

    - 輸入數字33 67 8 13 54 119 3 84 25 41
  
    ![](https://github.com/yunchien77/ds_algorithm/blob/main/hw3_quick_sort/exeresult/hw3_c_result.png)
  
  > - 輸入長度15

    - 輸入數字87 4 7 65 -1 90 3 22 23 71 23 12 77 11 43
  
    ![](https://github.com/yunchien77/ds_algorithm/blob/main/hw3_quick_sort/exeresult/hw3_c_result2.png)
  

## language: Python
* ### 程式碼
```python
def quickSort(arr, left, right):
    if(left >= right): 
        return arr   #base case

    i = left              #left pointer(左指標)
    j = right             #right pointer(右指標)
    pivot = arr[left]     #standard(基準點)
    
    while(i != j):    #left and right ponter are not on the same location 
        #若左指標小於右指標且右指標指在陣列的值大於基準點，則右指標左移(從右向左找第一個小於基準點的數)
        while(i < j and arr[j] >= pivot): 
            j -= 1
        #若左指標小於右指標且左指標指在陣列的值小於基準點，則左指標右移(從左向右找第一個大於基準點的數)
        while(i < j and arr[i] <= pivot): 
            i += 1
        if(i < j):   #直到右指標找到比基準點小的數值，左指標找到比基準點大的數值，將兩樹值交換位置
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp

    arr[left] = arr[i]
    arr[i] = pivot
    
    #recursive function(分別針對左右子陣列繼續做quick sort)
    quickSort(arr, left, i-1)
    quickSort(arr, i+1, right)



def main():
    print("Please enter a number for a length of array:")
    size = int(input())
    
    #讀取多個數字，每個數字以空格隔開
    print("Please enter the numbers of array:")
    input_str = input()
    
    #將輸入string以空白見分成多個string後轉換成list
    input_list = input_str.split()
    
    #將列表中的每個元素轉換成integer
    arr = [int(x) for x in input_list]
    
    #quick sort
    quickSort(arr, 0, size-1);

    print("\nSorted array:");
    print(' '.join(map(str, arr)))
    
if __name__ == '__main__':
    main()
```

* ### 執行結果
  > - 輸入長度10

    - 輸入數字33 67 8 13 54 119 3 84 25 41
  
    ![](https://github.com/yunchien77/ds_algorithm/blob/main/hw3_quick_sort/exeresult/hw3_py_result.png)
  
  > - 輸入長度15

    - 輸入數字87 4 7 65 -1 90 3 22 23 71 23 12 77 11 43
  
    ![](https://github.com/yunchien77/ds_algorithm/blob/main/hw3_quick_sort/exeresult/hw3_py_result2.png)
