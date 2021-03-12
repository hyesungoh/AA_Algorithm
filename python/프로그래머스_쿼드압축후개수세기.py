def solution(arr):


    def search(startY, startX, size):
        if size == 1:
            answer[arr[startY][startX]] += 1
            return

        temp_graph = []
        for y in range(startY, startY+size):
            temp_graph.append(arr[y][startX:startX+size])

        first_ele = temp_graph[0][0]
        for temp_l in temp_graph:
            for temp_ele in temp_l:
                if temp_ele != first_ele:
                    half = size // 2
                    search(startY, startX, half)
                    search(startY, startX+half, half)
                    search(startY+half, startX, half)
                    search(startY+half, startX+half, half)
                    return
        else:
            answer[first_ele] += 1
            return


    length = len(arr)
    answer = [0, 0]
    search(0, 0, length)
    return answer
