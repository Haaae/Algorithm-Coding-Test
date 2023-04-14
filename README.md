# Algorithm-Coding-Test

## 다시 풀어봐야 하는 문제

### 그리디
[백준 - 보석 도둑](https://github.com/Haaae/Algorithm-Coding-Test/blob/master/Greedy/%EB%B3%B4%EC%84%9D%20%EB%8F%84%EB%91%91-%EB%B0%B1%EC%A4%80.py)

### 구현
[프로그래머스 - 자물쇠와 열쇠. 카카오 공채](https://github.com/Haaae/Algorithm-Coding-Test/blob/master/implementation/%EC%9E%90%EB%AC%BC%EC%87%A0%EC%99%80_%EC%97%B4%EC%87%A0_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4.py)

[프로그래머스 - 문자열 압축. 카카오 공채](https://github.com/Haaae/Algorithm-Coding-Test/blob/master/implementation/%EB%AC%B8%EC%9E%90%EC%97%B4_%EC%95%95%EC%B6%95_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4.py)

[백준 - 문자열 압축. 삼성 sw 역량테스트](https://github.com/Haaae/Algorithm-Coding-Test/blob/master/implementation/%EB%B1%80_%EB%B0%B1%EC%A4%80.py)

[프로그래머스 - 기둥과 보. 카카오 공채](https://github.com/Haaae/Algorithm-Coding-Test/blob/master/implementation/%EA%B8%B0%EB%91%A5%EA%B3%BC_%EB%B3%B4.py)

[프로그래머스 - 외벽 점검. 카카오 공채](https://github.com/Haaae/Algorithm-Coding-Test/blob/main/implementation/%EC%99%B8%EB%B2%BD%20%EC%A0%90%EA%B2%80.py)

[백준 - 인구 이동. 삼성 sw 역량테스트](https://github.com/Haaae/Algorithm-Coding-Test/blob/master/DFS-BFS/%EC%9D%B8%EA%B5%AC%20%EC%9D%B4%EB%8F%99.py)

### BFS, DFS

[프로그래머스 - 블록 이동하기. 카카오 공채](https://github.com/Haaae/Algorithm-Coding-Test/blob/master/DFS-BFS/%EB%B8%94%EB%A1%9D%20%EC%9D%B4%EB%8F%99%ED%95%98%EA%B8%B0.py)

### Sort

[프로그래머스 - 실패율. 카카오 공채](https://github.com/Haaae/Algorithm-Coding-Test/blob/master/sort/%EC%8B%A4%ED%8C%A8%EC%9C%A8.py)

[백준 - 카드 정렬하기.](https://github.com/Haaae/Algorithm-Coding-Test/blob/master/sort/%EC%B9%B4%EB%93%9C%20%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0.py)


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

- python heapq.heapfiy(iter: iterable)는 내부적으로 binary tree를 사용하므로 인자의 요소를 정렬시키지 않는다.

```
import heapq

a = [100, 2, 8, 8, 6, 6, 56, 5, 6, 3, 2, 1]
heapq.heapify(a)
print(a)

# 결과: [1, 2, 6, 5, 2, 8, 56, 8, 6, 3, 6, 100]
```

- 파이썬은 빈 리스트를 False로 인식한다.

```
a = []
if not a :
   print("Empty!")
결과: Empty!
```

- 리스트 내 숫자의 중간값 구하기

```
numbers = [1, 2, 3, 4, 5]
length = len(numbers)

print(numbers[(length - 1) // 2])
결과: 3(index: 2)
```