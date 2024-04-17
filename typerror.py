yosh = input("Tug`ulgan yilingizni kririting: ")

try:
    yosh = int(yosh)
except:
    print("Butun son kiriting")
else:
    print(f"Sizning yoshimgiz {2024-yosh} da")
