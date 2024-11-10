import re

content = open('./58/first_task.txt').read().lower()
word_matcher = re.compile(r"(\w[\w']*\w|\w)")
sentences = re.split(r' *[\.\?!][\'"\)\]]* *', content)
words = word_matcher.findall(content)
result = dict()
for word in words:
    if word in result:
        result[word] = result[word] + 1
    else:
        result[word] = 1

with open('./results/first_task.txt', 'w+') as file:
    for item in sorted(result.items(), key=lambda kvp: kvp[1], reverse=True):
        file.write(F"{item[0]}:{item[1]}\n")

with open('./results/first_task_variative', 'w+') as variative_file:
    variative_file.write(str(len(words) / len(sentences)))
