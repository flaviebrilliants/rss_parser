import requests
import json
import time

def start():

    organs_list = []
    block_organ = []

    blocks = [
        ('e94b6872-dcac-414f-b2f1-a538d13a12a0', 'Президент Российской Федерации'),
        ('a30c9c82-4a21-48ab-a41d-d1891a10962c', 'Федеральное Собрание Российской Федерации'),
        ('19bb10cd-32f3-4632-8303-c94dd5f45359', 'Правительство Российской Федерации'),
        ('28bdeebd-e2cf-45ce-8d2a-2bc1aaadd7fc', 'Федеральные органы исполнительной власти и федеральные государственные органы Российской Федерации'),
        ('b85249b6-f6e6-4562-a783-90ea989af2db', 'Конституционный Суд Российской Федерации'),
        ('022fd55f-9f60-481e-a636-56d74b9ca759', 'Органы Государственной Власти Субъектов Российской Федерации')

    ]

    for block in blocks:

        print('Блок:', block[1])

        r = requests.post('http://publication.pravo.gov.ru/RssList/GetContent', data={
            'blockID': block[0]
        })

        time.sleep(0.3)

        data = json.loads(r.text)

        organs = data['SignatoryAuthorities']

        print('\t Органы:')
        for organ in organs:

            str1 = '''INSERT INTO organ VALUES ('{}');'''.format(organ['Text']).rstrip()

            if block[0] == 'e94b6872-dcac-414f-b2f1-a538d13a12a0':
                str2 = '''INSERT INTO organ_block VALUES (1, '{}');'''.format(organ['Text']).rstrip()
            if block[0] == 'a30c9c82-4a21-48ab-a41d-d1891a10962c':
                str2 = '''INSERT INTO organ_block VALUES (2, '{}');'''.format(organ['Text']).rstrip()
            if block[0] == '19bb10cd-32f3-4632-8303-c94dd5f45359':
                str2 = '''INSERT INTO organ_block VALUES (3, '{}');'''.format(organ['Text']).rstrip()
            if block[0] == '28bdeebd-e2cf-45ce-8d2a-2bc1aaadd7fc':
                str2 = '''INSERT INTO organ_block VALUES (4, '{}');'''.format(organ['Text']).rstrip()
            if block[0] == 'b85249b6-f6e6-4562-a783-90ea989af2db':
                str2 = '''INSERT INTO organ_block VALUES (5, '{}');'''.format(organ['Text']).rstrip()
            if block[0] == '022fd55f-9f60-481e-a636-56d74b9ca759':
                str2 = '''INSERT INTO organ_block VALUES (6, '{}');'''.format(organ['Text']).rstrip()

            organs_list.append(str1)
            block_organ.append(str2)
            print('\t\t' + organ['Text'])

    organs_list1 = set(organs_list)
    block_organ1 = set(block_organ)

    with open('organs.txt', 'w') as fo:
        for organ in organs_list1:
            fo.write(organ + '\n')

    with open('organ_block.txt', 'w') as fo:
        for item in block_organ1:
            fo.write(item + '\n')

    print()
start()