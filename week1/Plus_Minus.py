def plusMinus(arr):
   
    # To know the size of the array
    total = len(arr)
    # To count how many positives, negatives, and zeros there are
    positive_count = 0
    for x in arr:
        if x > 0:
            positive_count = positive_count + 1
    

    negative_count = 0
    for x in arr:
        if x < 0:
            negative_count = negative_count + 1
    
    
    zero_count = 0
    for x in arr:
        if x == 0:
            zero_count = zero_count + 1
    
    # To calculate the proportions by total
    positive_ratio = positive_count/total
    negative_ratio = negative_count/total
    zero_ratio = zero_count/total
    # To show the results of the ratios with 6 decimal places
    print(f'{positive_ratio: .6f}')
    print(f'{negative_ratio: .6f}')
    print(f'{zero_ratio: .6f}')
