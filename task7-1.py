
groupe = "2-МЗ-4.txt"
ans = str('')
with open(groupe, "w") as file:
    while ans == "да" or "Да":
        name = input("Введите фамилию студента: ")
        email = input("Введите Email: ")
        file.write(f"{name} - {email}\n")
        ans = input("Ввести ещё данные?: ").strip().lower()
        if ans != "да":
            break
print("Содержимое файла:")
with open(groupe, "r") as file:
    for line in file:
        line = line.replace("\n","")
        print(line)