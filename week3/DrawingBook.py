def pageCount(n, p):
 return min (p // 2, ((n//2) - (p//2)))

if __name__ == '__main__':
 n = int(input().strip())

 p = int(input().strip())

 result = pageCount(n, p)

 print(result)
