# Algorithm-Coding-Test

## 다시 풀어봐야 하는 문제

### 구현
[프로그래머스 - 자물쇠와 열쇠. 카카오 공채](https://github.com/Haaae/Algorithm-Coding-Test/blob/master/implementation/%EC%9E%90%EB%AC%BC%EC%87%A0%EC%99%80_%EC%97%B4%EC%87%A0_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4.py)

[프로그래머스 - 문자열 압축. 카카오 공채](https://github.com/Haaae/Algorithm-Coding-Test/blob/master/implementation/%EB%AC%B8%EC%9E%90%EC%97%B4_%EC%95%95%EC%B6%95_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4.py)

[백준 - 문자열 압축. 삼성 sw 역량테스트](https://github.com/Haaae/Algorithm-Coding-Test/blob/master/implementation/%EB%B1%80_%EB%B0%B1%EC%A4%80.py)

[프로그래머스 - 기둥과 보. 카카오 공채](https://github.com/Haaae/Algorithm-Coding-Test/blob/master/implementation/%EA%B8%B0%EB%91%A5%EA%B3%BC_%EB%B3%B4.py)

[프로그래머스 - 외벽 점검. 카카오 공채](https://github.com/Haaae/Algorithm-Coding-Test/blob/main/implementation/%EC%99%B8%EB%B2%BD%20%EC%A0%90%EA%B2%80.py)

## Remind

- iterable 객체 요소 중 추출 개수에 따른 조합 튜플들을 리스트로 반환: from itertools import combinations

```
from itertools import combinations

arr = ['A', 'B', 'C']
nCr = itertools.combinations(arr, 2)
print(list(nCr))

# 결과 : [('A', 'B'), ('A', 'C'), ('B', 'C')]
```

- iterable 객체 요소 중 추출 개수에 따른 순열 조합 튜플들을 리스트로 반환: from itertools import permutations

```
import itertools

arr = ['A', 'B', 'C']
nPr = itertools.permutations(arr, 2)
print(list(nPr))

# 결과 : [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
```


- 2차원 리스트를 90도 우로 회전시키는 함수

```
def rotate_matrix_by_90(matrix) {
    n = len(matrix)
    m = len(matrix[0])
    result = [[0] * n for _ in range(n)]
    
    for i in range(n) :
        for j in range(m) :
            result[j][n - i - 1] = matrix[i][j]
    return result
```