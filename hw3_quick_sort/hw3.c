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

