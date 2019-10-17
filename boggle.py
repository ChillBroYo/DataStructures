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
    storage_list = [[y, x, board[y][x]]]
    processed = []
    while len(storage) > 0:
        curr_item = storage.dequeue()
        processed.append(curr_item)
        c_y = curr_item[0]
        c_x = curr_item[1]

        # Down
        if len(board) > c_y + 1:
            down_item = [c_y + 1, c_x, board[c_y + 1][c_x]]
            if down_item not in storage_list:
                storage.enqueue(down_item)
                storage_list.insert(0, down_item)

        # Up
        if c_y - 1 > 0:
            up_item = [c_y - 1, c_x, board[c_y - 1][c_x]]
            if up_item not in storage_list:
                storage.enqueue(up_item)
                storage_list.insert(0, up_item)
        
        # Right
        if len(board[0]) > c_x + 1:
            right_item = [c_y, c_x + 1, board[c_y][c_x + 1]]
            if right_item not in storage_list:
                storage.enqueue(right_item)
                storage_list.insert(0, right_item)
        
        # Left
        if c_x - 1 > 0:
            left_item = [c_y, c_x - 1, board[c_y][c_x - 1]]
            if left_item not in storage_list:
                storage.enqueue(left_item)
                storage_list.insert(0, left_item)

        print(storage_list)
        storage_list[:-1]

# Takes set of words and sees if they exist in the set from the specified node
def dfs_get(x, y, path, words, board, words_found):
    if len(board) <= y or y < 0:
        return words_found
    elif len(board[0]) <= x or x < 0:
        return words_found
    else:
        for char in path:
            if char == board[y][x]:
                return words_found
    
    path.append(board[y][x])

    for word in words:
        if word == "".join(path):
            words_found.append(word)

    
    dfs_get(x, y + 1, path[:], words, board, words_found)
    dfs_get(x, y - 1, path[:], words, board, words_found)
    dfs_get(x + 1, y, path[:], words, board, words_found)
    dfs_get(x - 1, y, path[:], words, board, words_found)

    return words_found


if __name__ == "__main__":
    board = [["a", "b", "c"],
             ["d", "e", "f"],
             ["g", "h", "i"]]

    words = ["bad", "fed", "bed", "deb", "behifcb", "find", "hid", "back"]
    #dfs(0, 0, [], board)
    #bfs(0, 0, [], board)
    words_found = []
    for y in range(len(board)):
        for x in range(len(board[0])):
            words_found.extend(dfs_get(x,y,[],words, board,[]))
    
    print(words_found)