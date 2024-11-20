def calculate_sum_and_length(data):
    total_sum = 0
    total_length = 0

    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(key, (int, float)):
                total_sum += key
            elif isinstance(key, str):
                total_length += len(key)
            total_sum, length = calculate_sum_and_length(value)
            total_sum += length

    elif isinstance(data, list):
        for item in data:
            total_sum_item, length = calculate_sum_and_length(item)
            total_sum += total_sum_item
            total_length += length

    elif isinstance(data, tuple):
        for item in data:
            total_sum_item, length = calculate_sum_and_length(item)
            total_sum += total_sum_item
            total_length += length

    elif isinstance(data, (int, float)):
        total_sum += data

    elif isinstance(data, str):  
        total_length += len(data)

    return total_sum, total_length


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

total_sum, total_length = calculate_sum_and_length(data_structure)

print(f"Сумма всех чисел: {total_sum}, Общая длина всех строк: {total_length}")