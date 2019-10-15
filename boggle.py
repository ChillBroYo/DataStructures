from custom_queue import CustomQueue

# Takes a NxN board and a starting_node,  traversing all paths, printing items, path where it was from and the prev_node where it just came from
def dfs(x, y, path, board):
    print(path)
    if len(board) <= y or y < 0:
        return
    elif len(board[0]) <= x or x < 0:
        return
    else:
        already_exists = False
        for item in path:
            if item == board[y][x]:
                already_exists = True
                break
        if already_exists and len(path) == len(board) * len(board[0]):
            print("Full dfs completed")
            return
        elif already_exists:
            return
    
    path.append(board[y][x])
    
    dfs(x, y + 1, path, board)

    dfs(x, y - 1, path, board)

    dfs(x + 1, y, path, board)
    
    dfs(x - 1, y, path, board)

def bfs(x, y, path, board):
    storage = CustomQueue()
    storage.enqueue([y, x, board[y][x]])
    processed = []

    while len(storage) > 0:
        curr_val = storage.dequeue()
        processed.append(curr_val[2])
        if len(board) > curr_val[0] + 1:
            print("entered1")
            n_val = board[curr_val[0] + 1][curr_val[1]]
            exists = False
            for item in processed:
                if item == n_val:
                    exists = True
            for item in storage:
                if item[2] == n_val:
                    exists = True
            if not exists:
                storage.enqueue([curr_val[0] + 1, curr_val[1], board[curr_val[0] + 1][curr_val[1]]])
        if curr_val[0] - 1 >= 0:
            print("entered2")
            n_val = board[curr_val[0] - 1][curr_val[1]]
            exists = False
            for item in processed:
                if item == n_val:
                    exists = True
            for item in storage:
                if item[2] == n_val:
                    exists = True
            if not exists:
                storage.enqueue([curr_val[0] - 1, curr_val[1], board[curr_val[0] - 1][curr_val[1]]])
        if len(board[0]) > curr_val[1] + 1:
            print("entered3")
            n_val = board[curr_val[0]][curr_val[1] + 1]
            exists = False
            for item in processed:
                if item == n_val:
                    exists = True
            for item in storage:
                if item[2] == n_val:
                    exists = True
            if not exists:
                storage.enqueue([curr_val[0], curr_val[1] + 1, board[curr_val[0]][curr_val[1] + 1]])
        if curr_val[1] - 1 >= 0:
            print("entered4")
            n_val = board[curr_val[0]][curr_val[1] - 1]
            exists = False
            for item in processed:
                if item == n_val:
                    exists = True
            for item in storage:
                if item[2] == n_val:
                    exists = True
            if not exists:
                storage.enqueue([curr_val[0], curr_val[1] - 1, board[curr_val[0]][curr_val[1] - 1]])
    
    print(processed)


if __name__ == "__main__":
    board = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
    #dfs(0, 0, [], board)
    bfs(0,0, [], board)