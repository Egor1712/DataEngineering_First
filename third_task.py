rows = open('./58/third_task.txt').readlines()
result_rows = []
for row in rows:
    values = row.split()
    result_values = []
    for index, value in enumerate(values):
        if value == 'N/A':
            result_values.append((int(values[index - 1]) + int(values[index + 1])) / 2)
        else:
            result_values.append(int(value))

    result_rows.append(result_values)

with open('./results/third_task.txt', 'w+') as file:
    for row in result_rows:
        filtered = list(filter(lambda b: b % 7 == 0, row))
        file.write(f'{0 if len(filtered) == 0 else sum(filtered) / len(filtered)}\n')
