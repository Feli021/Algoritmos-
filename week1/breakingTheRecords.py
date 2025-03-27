def breakingRecords(scores):
    max_record = min_record = scores[0]
    max_count = min_count = 0
    for score in scores[1:]:  
        if score > max_record:
            max_record = score
            max_count += 1
        elif score < min_record:
            min_record = score
            min_count += 1
    return max_count, min_count

if __name__ == '__main__':
    n = int(input().strip())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    print(' '.join(map(str, result)))

