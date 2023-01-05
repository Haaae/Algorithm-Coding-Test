RIGHT = 'D'
LEFT = 'L'
APPLE = 2

# 뱀 머리가 몸통에 닿았는지 확인
def check_move(direction, game_map, head_location):
  x, y = direction
  head_x, head_y = head_location
  x, y = head_x + x, head_y + y
  if 0 > x or x > n - 1 or 0 > y or y > n - 1 or game_map[x][y] == 1:
    return False
  return True

n = int(input())

game_map = [[0] * n for _ in range(n)]

total_apple = int(input())

for apple_location in range(total_apple):
  x, y = map(int, input().split())
  game_map[x - 1][y - 1] = APPLE

l = int(input())

direction_changes = {}

for _ in range(l):
  second, direction = input().split()
  direction_changes[int(second)] = direction

result = 0
head_location = (0, 0)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 동, 남, 서, 북
direction = 0
tail_location = [(0, 0)]
game_map[0][0] = 1

while check_move(directions[direction], game_map, head_location):
  x, y = directions[direction]
  head_x, head_y = head_location
  head_x, head_y = head_x + x, head_y + y

  # 다음 이동칸이 사과가 아니라면
  if game_map[head_x][head_y] != APPLE:
    tail_x, tail_y = tail_location.pop(0)
    game_map[tail_x][tail_y] = 0

  # 머리 이동 확인
  game_map[head_x][head_y] = 1
  head_location = (head_x, head_y)
  tail_location.append((head_x, head_y))

  result += 1

  if result in direction_changes.keys():
    if direction_changes[result] == RIGHT:
      direction = (direction + 1) % 4
    if direction_changes[result] == LEFT:
      direction = (direction + 3) % 4
  # move(directions, direction, head_location, game_map, tail_location, result)

print(result + 1)
