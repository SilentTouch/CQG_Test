config_file = input('Enter config file name: ')
text_file = input('Enter text file name: ')

with open(config_file, 'rt', encoding='utf-8') as cfg:
    values = cfg.read().split('\n')


def format_values(values):
    """
    Форматирование данных из файла конфигурации
    :param values: str
    :return: list_of_values: попарный список букв для замены в формате list
    """
    list_of_values = []
    for i in range(len(values)):
        val = values[i].split('=')
        list_of_values.append(val)
    # print(list_of_values)
    return list_of_values


list_of_values = format_values(values)

with open(text_file, 'rt', encoding='utf-8') as text:
    content = text.read()
    # print(content)


def replace_values(content):
    """
    Замена изначального текста из файла в соответствии с файлом конфигурации
    :param content: str
    :return: content: новый контент для записи в файл
    """
    for i in range(len(list_of_values)):
        content = content.replace(list_of_values[i][0], list_of_values[i][1])
    # print(content)
    return content


new_content = replace_values(content)

with open(text_file, 'wt', encoding='utf-8')as text:
    text.write(new_content)

with open(text_file, 'rt', encoding='utf-8') as text:
    content = text.read()[::-1].split('\n')
    show = ''
    print(show.join(content))

input('For exit press Enter')