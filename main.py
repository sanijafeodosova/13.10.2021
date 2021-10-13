answer = input("Ievadīt jā vai nē: ")
f=open("teksts.txt", "a+", encoding="utf-8")

if answer == "jā" or answer == "Jā":
    teksts = input("Ievadi tekstu, ar ko vēlies papildināt failu: ")
    fails.write(teksts)
    f=open("teksts.txt", "r", encoding="utf-8")
    print(f.read())
else:
    print("Programma beidz darbu!")

fails.close()