from collections import deque

def make_graph(graph, words, words_length, word_length):
    for word_index in range(words_length):
        for compare_word_index in range(words_length):
            if word_index == compare_word_index:
                continue

            cnt = 0
            word = words[word_index]
            compare_word = words[compare_word_index]
            for index in range(word_length):
                if word[index] != compare_word[index]:
                    cnt += 1

                if cnt > 1:
                    break
            else:
                graph[word].append(compare_word)
                graph[compare_word].append(word)

def solution(begin, target, words):
    words.append(begin)
    word_length = len(begin)
    words_length = len(words)
    graph = {i: [] for i in words}
    dist = {i: words_length + 1 for i in words}

    make_graph(graph, words, words_length, word_length)

    q = deque([begin])
    dist[begin] = 0
    while q:
        word_now = q.popleft()

        for word_next in graph[word_now]:
            if dist[word_next] < dist[word_now] + 1:
                continue

            dist[word_next] = dist[word_now] + 1
            q.append(word_next)

    if target in dist:
        return dist[target] if dist[target] != words_length + 1 else 0
    else:
        return 0
