if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_list = list(arr)
    maxOne = maxTwo = float('-inf')
    for num in arr_list:
        if num > maxOne:
            maxTwo = maxOne
            maxOne = num
        elif num > maxTwo and num != maxOne:
            maxTwo = num
    print(maxTwo)
    
    