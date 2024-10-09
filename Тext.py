def custom_write(file_name, strings):
    strings_position = {}
    number = 0
    for i in strings:
        file = open(file_name, "a", encoding = "utf-8")
        number_b = file.tell()
        file.write(f"{str(i)}\n")
        number += 1
        strings_position[(number, number_b)] = i
        print(f"{str(i)}\n")
        file.close()
    return(strings_position)


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)