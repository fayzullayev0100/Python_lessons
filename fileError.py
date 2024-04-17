import json
files = ['talaba.json', 'talaba2.json', 'talaba3.jon']
for filename in files:
    try:
        with open(filename) as f:
            talaba = json.load(f)
    except FileNotFoundError:
        print(f"File {filename} mavjud emas")
    else:
        print(talaba[ism])

