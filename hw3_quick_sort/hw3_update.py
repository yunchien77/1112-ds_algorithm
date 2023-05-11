def quickSort(arr, left, right):
    if(left >= right): 
        return arr   #base case

    i = left              #left pointer(左指標)
    j = right             #right pointer(右指標)
    print('\x1b[35m' + f'left pointer index = {i}')
    print(f'right pointer index = {j}' + '\x1b[0m')  
    
    pivot = arr[left]     #standard(基準點)
    print('\x1b[36m' + f'pivot = {pivot}' + '\x1b[0m')
    
    while(i != j):    #left and right ponter are not on the same location 
        #從右向左找第一個小於基準點的數
        while(i < j and arr[j] >= pivot): 
            j -= 1
        #從左向右找第一個大於基準點的數
        while(i < j and arr[i] <= pivot): 
            i += 1
            
        print('\x1b[36m' + f'left pointer index = {i}')
        print(f'right pointer index = {j}' + '\x1b[0m')  
            
        if(i < j):   #直到右指標找到比基準點小的數值，左指標找到比基準點大的數值，將兩數值交換位置
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
    
        print("array:", end=" ");
        print(' '.join(map(str, arr)), end="\n\n")
   
        
    arr[left] = arr[i]
    arr[i] = pivot
    
    #recursive function
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
    
    print()
    
    #quick sort
    quickSort(arr, 0, size-1);

    print("Sorted array:");
    print(' '.join(map(str, arr)))
    
if __name__ == '__main__':
    main()