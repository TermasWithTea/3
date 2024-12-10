def calculate_structure_sum(*data_structure):
    total_sum = 0
    total_string_length = 0

    for element in data_structure:
        if isinstance(element, (list, tuple, set)):
            for item in element:
                total_sum, total_string_length = calculate_structure_sum(item, total_sum, total_string_length)
        elif isinstance(element, dict):
            for key, value in element.items():
                total_sum, total_string_length = calculate_structure_sum(key, value, total_sum, total_string_length)
        elif isinstance(element, str):
            total_string_length += len(element)
        elif isinstance(element, (int, float)):
            total_sum += element
        else:
            pass

    return total_sum, total_string_length

# Пример использования
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(*data_structure)
print(result)  