def find_average_for_negative(values):
    sum = 0
    count = 0
    for value in values:
        if value < 0:
            sum += value
            count = count + 1

    return sum / count


rows = map(lambda s: map(lambda x: int(x), s.split()), open('./58/second_task.txt').readlines())

averages = list(map(lambda row: find_average_for_negative(row), rows))
min = min(averages)
max = max(averages)
with open('./results/second_task.txt', 'w+') as file:
    for value in averages:
        file.write(f"{value}\n")
    file.write("\n")
    file.write(f"{max}\n")
    file.write(f"{min}\n")
