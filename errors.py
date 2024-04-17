"""sntaksis error"""
son = float(input("Juft son kiriting: "))
if son%2==0:
    print("Bu son juft emas.")
else:
    print("Rahmat!")

# son = float(input("Juft son kiriting: ") #qavs #qolip #ketgan
# if son%2==0:
#     print("Bu son juft emas.')
# else:
#     print("Rahmat!")) bitta qavs ortiqcha

yosh = (input("Yoshingiz nechida?"))

if yosh<=4 or yosh>=60:
    narh = 0
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
    print(f"Chipta {narh} so'm")

# tepadagi kodda : qolip ketgan


x = float(input("Birinchi sonni kiriting: ")) #oxirida qavs qolip ketgan
y = float(input("Ikkinchi sonni kiriting: ")) #oxirida qavs qolip ketgan
if x==y:
    print(f"{x}={y}")
elif x<y:
    print(f"{x}<{y}")
elif x>y:
    print(f"{x}>{y}")


