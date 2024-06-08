def calc_structure_sum(data_struct):
    result_sum = 0
    for elem in data_struct:
        if isinstance(elem, dict):
            result_sum += calc_structure_sum(elem.items())
        elif isinstance(elem, int):
            result_sum += elem
        elif isinstance(elem, str):
            result_sum += len(elem)
        else:
            result_sum += calc_structure_sum(elem)
            # if isinstance(elem, list):
            #     result_sum += calc_structure_sum(elem)
            # if isinstance(elem, tuple):
            #     result_sum += calc_structure_sum(elem)
            # if isinstance(elem, set):
            #     result_sum += calc_structure_sum(elem)
    return result_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calc_structure_sum(data_structure)
print(result)
