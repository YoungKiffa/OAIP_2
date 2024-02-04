import json


# def main():
with open("saa (1).json", "r", encoding="utf8") as file:
    sas = json.load(file)
for z in sas:
    s = sas[z]["city"]
    if s == "Moscow":
        print(sas[z]["name"])
        print(sas[z]["age"])


# if __name__ == "__main__":
#     main()