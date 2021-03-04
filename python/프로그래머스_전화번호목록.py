def solution(phone_book):
    hash = {i: True for i in phone_book}

    for word in phone_book:
        temp = ""
        for text in word:
            temp += text
            if temp in hash and word != temp:
                return False
    return True
