def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')  # - название файла для записи
    string_position = {}                         # - список строк для записи

    for line_no in range(len(strings)):
        string_position[(line_no + 1, file.tell())] = strings[line_no]
        file.write(strings[line_no] + r'\n')
    file.close()
    return string_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
