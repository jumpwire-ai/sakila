from faker import Faker
from random import randint
fake = Faker()


def generate_datur(f):
    perc = 0.0
    for i in range(600, 500000):
        row = []
        row.append(i)
        row.append(randint(1, 2))
        fn = fake.first_name()
        ln = fake.last_name()
        row.append(fn)
        row.append(ln)
        row.append(f'{fn}.{ln}@sakilacustomer.org')
        row.append(randint(1, 605))
        row.append('t')
        row.append('2006-02-14')
        row.append('2006-02-15 09:57:20')
        row.append('1')
        sql = '\t'.join(map(str, row))
        f.write(f'{sql}\n')

        iperc = round(i/500000, 2) * 100
        if perc != iperc:
            print(f'{iperc}% done')
            perc = iperc

with open('postgres-sakila-data.sql') as datur:
    with open('postgres-sakila-data-large.sql', 'a') as newdatur:
        print('Generating large customer data set')
        for line in datur:
            if line.startswith('COPY customer'):
                newdatur.write(line)
                generate_datur(newdatur)
            else:
                newdatur.write(line)

