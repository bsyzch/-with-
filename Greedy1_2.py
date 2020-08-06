n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first=data[n-1]
second=data[n-2]

count=0

count = (m-(m//(k+1)))*first + (m//(k+1))*second

print(count)