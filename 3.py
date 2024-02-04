import json


def main():
    with open("info.json", encoding="utf8") as file_in:
        records = json.load(file_in)
    a = input('Что изменить: ')
    records[a] = input('Впишите новые данные: ')
    with open("info.json", "w") as write_file:
        json.dump(records, write_file)


if __name__ == "__main__":
    main()