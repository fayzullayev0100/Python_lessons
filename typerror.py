yosh = int(input("Tug`ulgan yilingizni kiriting: "))
try:
    yosh = int(yosh)
except:
    print("Butun son kiriting")
else:
    print(f"Siz {2024-yosh} yoshda siz")
