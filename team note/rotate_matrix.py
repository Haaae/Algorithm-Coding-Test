# 2차원 리스트 90도 회전
def rotate_matrix_by_90(matrix):
    n = len(matrix)
    m = len(matrix[0])
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = matrix[i][j]
    return result