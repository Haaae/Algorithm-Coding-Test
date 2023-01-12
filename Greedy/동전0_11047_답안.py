p,*o = open(0)
# open(0) : https://www.acmicpc.net/board/view/80793

# Asterisk(*) : https://mingrammer.com/understanding-the-asterisk-of-python/
k = int(p[2:]) # [2:]로 k 값에 접근하는 이유는 p == '10 4200'와 같은 str이기 때문이다.
c = 0
for i in map(int,o[::-1]):
    c += k // i
    k = k % i
print(c)