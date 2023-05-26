import re


def checkfunc(col):
    smth = '@' in col and col.replace('@', '[at]') or (
        ('(' in col or '-' in col) and
        re.sub(r'\([^)]*\)', '', col).replace('-', '').replace(' ', '')
    ) or (col.count(' ') == 1 and ' '.join(col.split(' ')[::-1])) or ''
    return smth


def transform_table(input_table):
    unique_cols = []
    output_table = []
    output_table = list(map(
        lambda row: list(filter(
            lambda col:
            (col not in unique_cols) and (unique_cols.append(col) or True),
            row
        )),
        input_table
    ))

    output_table = list(map(
        lambda row: list(map(
            lambda col: checkfunc(col) if col is not None else None,
            row
        )),
        output_table
    ))

    transposed_table = []
    max_len = max([len(row) for row in output_table])
    transposed_table = list(map(
        lambda j: [
            output_table[i][j] if j < len(output_table[i]) else None
            for i in range(len(output_table))
        ],
        range(max_len)
    ))

    return transposed_table

input_table = [
    ['evgenij3@yandex.ru', 'Евгений Деров', '(452) 977-1242', '(452) 977-1242'],
    ['aleksandr18@mail.ru', 'Александр Бусилев', '(814) 692-0844', '(814) 692-0844'],
    ['fekomov60@gmail.com', 'Роман Фекомов', '(172) 774-3276', '(172) 774-3276'],
    ['aroslav89@yahoo.com', 'Ярослав Сориди', '(984) 639-5519', '(984) 639-5519']
]

output_table = transform_table(input_table)

for row in output_table:
    print(row)
