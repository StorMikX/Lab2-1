params = dict()
with open("Lab2/conf", 'r') as file:
    for line in file:
        if line[0] != '#' and line[0] != ';' and line[0] != '\n':
            key, *value = line.rstrip("\n").split(" ")
            params[key] = value 
            
print("Существующие параметры:", end="\n")
for key in params:
    print(key)

flag = True
while flag:
    param1 = input("Введите параметр: ")
    print("Значение параметра: ", params.get(param1))

    command = (input("Завершить программу?(Y/N): "))

    if command == "Y":
        flag = False
    elif command == "N":
        continue


