# king, queen, rook, bishop, knight, pawn = input().split()

board = [1,1,2,2,2,8]
ans = []
piece = list(map(int, input().split()))

for idx, val in enumerate(board):
    ans.append(val - piece[idx])

print(*ans)
