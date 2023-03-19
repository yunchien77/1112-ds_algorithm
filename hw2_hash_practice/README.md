# HW2 統計字串出現頻率
## language: Python
* ### 程式碼
```python
def main():
    #開啟txt檔
    with open('hw2_data.txt', 'r') as file:
        #讀取所有行
        lines = file.readlines()
    
    #初始化word_counts(empty dictionary)，用來記錄每個英文單字出現的次數
    word_counts = {}
    
    #遍歷每一行
    for word in lines:
        #去除換行符號(\n)
        word = word.strip()
        
        #若這個字母(key)已出現過，則將其出現次數(value)加1
        if word in word_counts:
            word_counts[word] += 1
            
        #若為第一次出現，則在字典中新增這個單字(key)並將其出現次數(value)設為1
        else:
            word_counts[word] = 1
    
    #計算總共有多少個不重複的英文字
    numOfWords = len(word_counts)
    print(f"Here are {numOfWords} non-repeated English words\n")
    
    #輸出每個單字出現的次數
    for word, count in sorted(word_counts.items()):
        print("{:<6} appears {:<3} times".format(word, count))


if __name__ == '__main__':
    main()
```

* ### 執行結果
  ![](https://github.com/yunchien77/ds_algorithm/blob/main/hw2_hash_practice/exeresult.png)
  
