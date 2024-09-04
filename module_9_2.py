first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(x) for x in first_strings if len(x) >= 5]

second_result = [(y, b) for y in first_strings for b in second_strings if len(y) == len(b)]

third_result = {x: len(x) for x in first_strings + second_strings if len(x) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)
