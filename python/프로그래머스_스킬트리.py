from collections import deque

def solution(skill, skill_trees):
    skill_dict = {i: True for i in skill}
    ans = 0

    for skill_tree in skill_trees:
        temp_skill = deque(skill)

        for now_skill in skill_tree:
            if now_skill in skill_dict:
                if now_skill != temp_skill.popleft():
                    break
        else:
            ans += 1

    return ans
