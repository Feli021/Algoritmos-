def separateNumbers(s):
    n = len(s)
    # If string starts with '0', it's invalid per problem statement
    if n == 0 or s[0] == '0':
        return "NO"

    # try all possible sizes of the first number (1 .. n//2)
    for size in range(1, n // 2 + 1):
        first_str = s[:size]
        # skip if first number would have leading zero
        if first_str[0] == '0':
            continue

        first = int(first_str)
        seq = first_str           # build sequence as string, start with the original digits
        next_num = first

        # build sequence until its length >= original string length
        while len(seq) < n:
            next_num += 1
            seq += str(next_num)

        if seq == s:
            return f"YES {first}"

    return "NO"


if __name__ == '__main__':
    q = int(input().strip())
    for _ in range(q):
        s = input().strip()
        print(separateNumbers(s))

        
"""
1 - next_num will be 'first' (stored in seq) plus 1; 
    If first is 99, next_num will be 100 (next_num = first + 1).

    seq = seq + str(next_num) example:
    seq = "98" + "99" -> "9899"; then + "100" -> "9899100"

2 - After the while loop, if seq is exactly equal to the original string s,
    then we can divide s into consecutive numbers starting at first.
"""
