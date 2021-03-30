import os

def make_readme(README_CONTENT, start_index, LANGUAGE):
    # 언어마다 컨텐츠의 시작 지점이 다르기 때문에
    for content_sperated_by_day in README_CONTENT[start_index:]:
        day = content_sperated_by_day[0:9].replace(".", "-").strip()
        # print(content_sperated_by_day)

        content_sperated_by_problem = content_sperated_by_day.split("-   [")

        for content_problem in content_sperated_by_problem[1:]:
            content_problem_sperated_by_br = content_problem.split("\n")

            name, url = content_problem_sperated_by_br[0].strip().split("..")
            name = name.replace("]", "").replace("(", "")
            name = name.replace(" ", "_")
            # print(name)

            content = ""
            for text in content_problem_sperated_by_br[1:]:
                content += text.strip()
            content += "\n"
            # print(content)

            if LANGUAGE == "Python":
                SOURCE_PATH = "python/" + name + ".py"
            elif LANGUAGE == "Javascript":
                SOURCE_PATH = "../algorithmJS/nodejs/BOJ/" + name + ".js"

            try:
                SOURCE_FILE = open(SOURCE_PATH, "r")
                if LANGUAGE == "Python":
                    SOURCE_CONTENT = "```python\n"
                elif LANGUAGE == "Javascript":
                    SOURCE_CONTENT = "```javascript\n"

                SOURCE_CONTENT += SOURCE_FILE.read()
                SOURCE_CONTENT += "\n```"
                SOURCE_FILE.close()
                name = name.replace("_", "-")

                try:
                    if LANGUAGE == "Python":
                        NEW_FILE = open("Algorithm/%s-Python.md" % (name), "w")
                    elif LANGUAGE == "Javascript":
                        NEW_FILE = open("Algorithm/%s-Javascript.md" % (name), "w")
                except:
                    print("Algorithm 폴더가 없어서 생성하였습니다")
                    os.mkdir("Algorithm")
                    if LANGUAGE == "Python":
                        NEW_FILE = open("Algorithm/%s-Python.md" % (name), "w")
                    elif LANGUAGE == "Javascript":
                        NEW_FILE = open("Algorithm/%s-Javascript.md" % (name), "w")

                NEW_FILE_CONTENT = "---\n" \
                                   "title: '%s - %s'\n" \
                                   "date: 20%s 12:21:13\n" \
                                   "category: 'Algorithm'\n" \
                                   "draft: false\n" \
                                   "---\n" % (name.replace("_", " "), LANGUAGE, day)

                NEW_FILE.write(NEW_FILE_CONTENT)
                NEW_FILE.write(content)
                NEW_FILE.write(SOURCE_CONTENT)
                NEW_FILE.close()
                print("Completed : %s" % name)

            except:
                print("ERROR : %s" % name)


# 파이썬
PYTHON_PATH = "README.md"
PYTHON_README_FILE = open(PYTHON_PATH, "r")
PYTHON_README_CONTENT = PYTHON_README_FILE.read().split("####")
PYTHON_START_INDEX = 2

make_readme(PYTHON_README_CONTENT, PYTHON_START_INDEX, "Python")
PYTHON_README_FILE.close()


# 자바스크립트
JAVASCRIPT_PATH = "../algorithmJS/nodejs/README.md";
JAVASCRIPT_FILE = open(JAVASCRIPT_PATH, "r")
JAVASCRIPT_CONTENT = JAVASCRIPT_FILE.read().split("## Log")[1].split("####")
JAVASCRIPT_START_INDEX = 0

make_readme(JAVASCRIPT_CONTENT, JAVASCRIPT_START_INDEX, "Javascript")
JAVASCRIPT_FILE.close()






# README_FILE = open("README.md", "r")
# README_CONTENT = README_FILE.read().split("####")

# for content_sperated_by_day in README_CONTENT[2:]:
#     day = content_sperated_by_day[0:9].replace(".", "-").strip()
#     # print(day)

#     content_sperated_by_problem = content_sperated_by_day.split("- [")
#     for content_problem in content_sperated_by_problem[1:]:

#         content_problem_sperated_by_br = content_problem.split("\n")

#         name, url = content_problem_sperated_by_br[0].strip().split("..")
#         name = name.replace("]", "").replace("(", "")
#         name = name.replace(" ", "_")
#         url = url.replace(")", "")

#         # print(name)
#         # print(url)

#         content = ""
#         for text in content_problem_sperated_by_br[1:]:
#             content += text.strip()
#         content += "\n"
#         # print(content)

#         SOURCE_NAME = name + ".py"
#         try:
#             SOURCE_FILE = open("python/%s" %SOURCE_NAME, "r")
#             SOURCE_CONTENT = "```python\n"
#             SOURCE_CONTENT += SOURCE_FILE.read()
#             SOURCE_CONTENT += "\n```"
#             SOURCE_FILE.close()

#             name = name.replace("_", "-")
#             NEW_FILE = open("Algorithm/%s-Python.md" % (name), "w")
#             NEW_FILE_CONTENT = "---\n" \
#                                "title: '%s - Python'\n" \
#                                "date: 20%s 12:21:13\n" \
#                                "category: 'Algorithm'\n" \
#                                "draft: false\n" \
#                                "---\n" % (name.replace("_", " "), day)

#             NEW_FILE.write(NEW_FILE_CONTENT)
#             NEW_FILE.write(content)
#             NEW_FILE.write(SOURCE_CONTENT)
#             NEW_FILE.close()
#             print("Completed : %s" %name)

#         except:
#             print("ERROR : %s" %name)

# README_FILE.close()
