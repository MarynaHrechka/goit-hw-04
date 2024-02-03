def total_salary(path: str):
    result = []
    with open(path) as file:
        result = [int(line.split(",")[1].strip()) for line in file.readlines()]
    return sum(result), int((sum(result)/len(result)))


total, average = total_salary("test_1.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")