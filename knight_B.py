def is_valid_move(board, move):
    x, y = move
    if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or x == 0 and y == 0 or x == 7 and y == 0 \
            or x == 0 and y == 7 or x == 7 and y == 7:
        return False
    return True


def knight_tour(board, move, visited, steps):
    directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                  (1, -2), (1, 2), (2, -1), (2, 1)]

    visited.append(move)
    if len(visited) == steps:
        if is_valid_move(board, (move[0] - 2, move[1] - 1)):
            print("Solution found:")
            for cell in visited:
                x,y = cell
                board[x][y] = 1
                for line in board:
                    print(line)
                print("")
            return True
        else:
            visited.pop()
            return False

    for dx, dy in directions:
        new_x, new_y = move[0] + dx, move[1] + dy
        if is_valid_move(board, (new_x, new_y)) and (new_x, new_y) not in visited:
            if knight_tour(board, (new_x, new_y), visited, steps):
                return True

    visited.pop()
    return False


def remove_corners(board):
    for i in range(2):
        for j in range(2):
            board[i * (len(board) - 1)][j * (len(board[0]) - 1)] = -1


def main():
    # Sakktábla inicializálása
    rows = 8
    cols = 8
    board = [[0 for _ in range(cols)] for _ in range(rows)]

    # Sarokmezők eltávolítása
    remove_corners(board)

    # Kiindulási pozíció beállítása
    start_position = (0, 1)

    # Lépések számítása
    steps = rows * cols - 4

    # Megoldás keresése
    visited = []
    knight_tour(board, start_position, visited, steps)


if __name__ == "__main__":
    main()
