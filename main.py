import random

with open('text.txt') as file:
    content = file.read()
    print(content)

random_number = str(random.randint(0, 10))
previous_number = [random_number]

with open('text.txt', mode='a') as file:
    seen_numbers = set(content.split())

    for i in previous_number:
        print(i)
        if i in seen_numbers:
            print(f"Duplicate found: {i}")
            previous_number.remove(i)

        if len(previous_number) > 10:
            print('too many items')
            previous_number.pop()
        else:
            file.write('\n' + i)