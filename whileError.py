while True:
    yosh = input("Yoshingizni son orqali kiriting: ")
    if yosh.isdigit():
        yosh = int(yosh)
        break
print(f"Yoshingizni {yosh} da")