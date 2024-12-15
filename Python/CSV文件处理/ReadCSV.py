import csv


def check():
    with open('1.csv', 'r', encoding='GBK') as f:
        data = csv.DictReader(f)
        for row in data:
            print(row)

if __name__ == '__main__':
    check()
    