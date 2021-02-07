


README_FILE = open("README.md", "r")
README_CONTENT = README_FILE.read().split("####")

for content_sperated_by_day in README_CONTENT[2:]:
    day = content_sperated_by_day[0:9].replace(".", "-").strip()
    # print(day)

    content_sperated_by_problem = content_sperated_by_day.split("- [")
    for content_problem in content_sperated_by_problem[1:]:

        content_problem_sperated_by_br = content_problem.split("\n")

        name, url = content_problem_sperated_by_br[0].strip().split("..")
        name = name.replace("]", "").replace("(", "")
        name = name.replace(" ", "_")
        url = url.replace(")", "")

        # print(name)
        # print(url)

        content = ""
        for text in content_problem_sperated_by_br[1:]:
            content += text.strip()
        content += "\n"
        # print(content)

        SOURCE_NAME = name + ".py"
        try:
            SOURCE_FILE = open("python/%s" %SOURCE_NAME, "r")
            SOURCE_CONTENT = "```python\n"
            SOURCE_CONTENT += SOURCE_FILE.read()
            SOURCE_CONTENT += "\n```"
            SOURCE_FILE.close()

            NEW_FILE = open("Algorithm/%s_Python.md" % (name), "w")
            NEW_FILE_CONTENT = "---\n" \
                               "title: '%s - Python'\n" \
                               "date: 20%s 12:21:13\n" \
                               "category: 'Algorithm'\n" \
                               "draft: false\n" \
                               "---\n" % (name.replace("_", " "), day)

            NEW_FILE.write(NEW_FILE_CONTENT)
            NEW_FILE.write(content)
            NEW_FILE.write(SOURCE_CONTENT)
            NEW_FILE.close()
            print("Completed : %s" %name)

        except:
            print("ERROR : %s" %name)

README_FILE.close()
