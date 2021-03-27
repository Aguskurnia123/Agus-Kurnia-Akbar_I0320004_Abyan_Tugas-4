print("Berapa usia kamu?")
a = int(input("Jawab :"))

print("Apakah kamu sudah lulus ujian kualifikasi (Y/T)?")
b = str(input("Jawab :"))

if (a>=int(21)) and (b == "Y"):
    print("Anda dapat mendaftar di kursus")
else :
    print("Anda tidak dapat mendaftar di kursus")
