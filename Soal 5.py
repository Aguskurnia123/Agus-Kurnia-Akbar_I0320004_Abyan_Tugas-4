s ="String may handsome!"
#Panjangnya harus 20
print("Panjang dari s =", len(s))

#huruf pertama 'a' harusnya di index no 8
print("Kemunculan pertama a =", s.index("a"))

#jumlah huruf a harusnya 2
print("a muncul sebanyak ",s.count("a"), "kali" )

#memotong string berdasarkan index
print("Lima karakter pertama adalah", s[:5]) #Start to 5
print("Lima karakter berikutnya adalah", s[5:10]) # 5 to 10
print("Karakter ketiga belas adalah ", s[12]) #just number 12
print("Karakter dengan indeks ganjil adalah",s[1::2]) #(0-based index)
print("Lima karakter terakhir adalah ", s[-5:] )  #5th-from-last to end

#konversikan ke upercase
print("String dalam huruf besar :", s.upper())

#konversikan ke lowercase
print("String dalam huruf kecil :", s.lower())

#cek bagaimana string itu dimulai
if s.startswith("Str"):
    print("String dimulai dengan 'Str' . Good!")
#cek bagaimana string itu diakhiri
if s.endswith("ome!"):
    print("String diakhiri dengan 'ome!' . Good!")

#Pisahkan string menjadi tiga string yang terpisah,
#masing masing hanya berisi satu kata
print("Pisahkan kata-kata dari string tersebut :", s.split(" "))




