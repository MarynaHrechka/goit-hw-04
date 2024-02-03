def get_cats_info(path: str):
    result = []
    with open(path) as file:
        result = [line.split(",") for line in file.readlines()]
    return [dict(id=item[0], name=item[1], age=item[2].strip()) for item in result]


print(get_cats_info("test_2.txt"))