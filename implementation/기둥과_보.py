NOTHING = 3
PILLAR = 0
TILE = 1
PILLAR_ON_TILE = 2
DELETE = 0
INSTALL = 1


def insertPossibleFrame(x,
                        y,
                        frame,
                        build_map,
                        possible_frame,
                        pillar_on_tile=False):
    if pillar_on_tile:
        build_map[x][y] = PILLAR_ON_TILE
    else:
        build_map[x][y] = frame
    possible_frame.append([x, y, frame])


def deletePossibleFrame(x, y, frame, build_map, possible_frame):
    build_map[x][y] = NOTHING
    possible_frame.remove([x, y, frame])


def canDeletePillar(x, y, build_map):
    # 삭제하는 기둥의 윗부분 좌표에 보 혹은 다른 기둥이 없으면 ok
    if build_map[x][y + 1] == NOTHING and not (
            build_map[x - 1][y + 1] == TILE and
        (build_map[x - 1][y] == PILLAR or build_map[x - 1][y]
         == PILLAR_ON_TILE)) and build_map[x][y] == PILLAR:
        return True
    return False


def canInstallPillar(x, y, build_map):
    # 기둥 좌표가 바닥이고 해당 좌표에 아무것도 없거나, 다른 기둥의 윗부분이고 해당 좌표에 아무것도 없거나, 보이고 해당 좌표에 아무것도 없으면 ok
    if (build_map[x][y] == NOTHING and y == 0) or (
            build_map[x][y] == NOTHING and build_map[x][y - 1] == PILLAR) or (
                build_map[x][y] == NOTHING
                and build_map[x - 1][y] == TILE) or (build_map[x][y] == TILE):
        return True
    return False


def canDeleteTail(x, y, build_map):
    # 삭제하는 보의 좌표 혹은 오른쪽 +1 좌표에 기둥이 없고, 삭제하는 보의 좌표와 오른쪽 +1 좌표 모두 보가 연결되지 않으면 ok
    if (build_map[x][y] != PILLAR_ON_TILE or
        (build_map[x][y] == PILLAR_ON_TILE
         and build_map[x - 1][y] == TILE)) and (
             (build_map[x + 1][y] == TILE
              and not build_map[x + 2][y - 1] != PILLAR) or
             (build_map[x - 1][y] == TILE
              and not build_map[x - 1][y - 1] != PILLAR)) and (build_map[x][y]
                                                               == TILE):
        return True
    return False


def canInstallTail(x, y, build_map):
    # 보의 좌표와 오른쪽 +1 좌표가 다른 보거나, 둘 중 하나가 기둥의 윗부분이라면 ok
    if build_map[x][y -
                    1] == PILLAR or build_map[x][y - 1] == PILLAR_ON_TILE or (
                        build_map[x - 1][y] == TILE
                        and build_map[x + 1][y] == TILE):
        return True
    return False


def solution(n, build_frame):
    build_map = [[NOTHING] * (n + 1) for _ in range(n + 1)]
    possible_frame = []

    while len(build_frame) != 0:
        x, y, frame, deleteOrInstall = build_frame.pop(0)

        if frame == PILLAR:
            if deleteOrInstall == DELETE:
                if canDeletePillar(x, y, build_map):
                    deletePossibleFrame(x, y, frame, build_map, possible_frame)
            if deleteOrInstall == INSTALL:
                if canInstallPillar(x, y, build_map):
                    insertPossibleFrame(x, y, frame, build_map, possible_frame)

            if frame == TILE:
                if deleteOrInstall == DELETE:
                    if canDeleteTail(x, y, build_map):
                        deletePossibleFrame(x, y, frame, build_map,
                                            possible_frame)
                if deleteOrInstall == INSTALL:
                    if canInstallTail(x, y, build_map):
                        insertPossibleFrame(x, y, frame, build_map,
                                            possible_frame)

    return sorted(possible_frame)

print(
    solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1],
                 [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
