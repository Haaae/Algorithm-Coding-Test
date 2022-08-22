n, k = list(map(int, input().split()))

# 동전 종류를 담을 list
coin = []

# 동전 종류 입력. 오름차순
for i in range(n) :
    coin.append(int(input()))

coin_count = 0

while k > 0 :
    price = coin.pop()  # 현재 coin 중 가장 비싼 coin을 pop
    
    if price <= k :
        coin_count += k // price
        k %= price

print(coin_count)