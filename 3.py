def calculate_structure_sum(data_structure):
    total_sum = 0


    def recursive_sum(element):
        nonlocal total_sum

        if isinstance(element, (list, tuple, set)):
            for item in element:
                recursive_sum(item)
        elif isinstance(element, dict):
            for key, value in element.items():
                recursive_sum(key)
                recursive_sum(value)
        elif isinstance(element, (int, float)):
            total_sum += element
        elif isinstance(element, str):
            total_sum += len(element)

    recursive_sum(data_structure)

    return total_sum


# Пример использования
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
