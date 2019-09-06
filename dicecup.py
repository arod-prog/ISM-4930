n,m = map(int,input().split())

if n == m:
    print(n+1)
else:
    num_one = min(n,m)
    num_two = max(n,m)
    real_total_one = num_one+1
    real_total_two = num_two+2
    
    for i in range(real_total_one, real_total_two):
          print(i)