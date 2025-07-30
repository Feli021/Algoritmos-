def rotateLeft(d, arr):
    for _ in range(d):   # I want the command block to repeat 'd' times
        arr.append(arr.pop(0)) # I added what I removed the element at index 0.
    return arr
  
       # for _ in range(n):  This is a repetition structure. It says: Repeat the block inside 'n' times.
       
       # I don't want to access the indexes. I just want to repeat a command block 'n' times.
