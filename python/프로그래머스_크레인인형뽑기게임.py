def pang(basket, answer, item):
    if basket[-1] == item:
        basket.pop()
        answer[0] += 1
    else:
        basket.append(item)

def solution(board, moves):
    depth = len(board)
    basket = [0]
    answer = [0]

    for move in moves:
        move -= 1
        for i in range(depth):
            if board[i][move] != 0:
                pang(basket, answer, board[i][move])
                board[i][move] = 0
                break

    return answer[0] * 2
