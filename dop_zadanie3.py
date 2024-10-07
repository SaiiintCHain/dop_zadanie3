def calculate_structure_sum(data):
    summator = 0
    if isinstance(data,(int,float)):
        summator += data
    elif isinstance(data,str):
        summator += len(data)
    elif isinstance(data,(tuple,list,set)):
        for i in data:
            summator += calculate_structure_sum(i)
    elif isinstance(data,dict):
        for key, value in data.items():
            summator += calculate_structure_sum(key)
            summator += calculate_structure_sum(value)
    return summator


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)







