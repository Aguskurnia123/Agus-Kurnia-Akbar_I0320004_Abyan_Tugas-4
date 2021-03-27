bil1 = int(input("Masukan bilangan pertama :"))
bil2 = int(input("Masukan bilangan bulat kedua :"))
if (bil1 > bil2):
    print("Bilangan ",bil2,"dapat membagi bilangan ",bil1,"sebanyak ",bil1//bil2,"kali")
elif (bil1 < bil2):
    print("Bilangan ", bil1, "dapat membagi bilangan ", bil2, "sebanyak ", bil2 // bil1, "kali")
