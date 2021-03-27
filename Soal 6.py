biner1 = 4  #0000 0100
biner2 = 11 #0000 1011

a = biner1 | biner2
print("Hasil pada poin a adalah: ",a) #0000 1111

b= biner1 >> biner2
print("Hasil pada poin b adalah: ",b) #0000 0000

c= biner1 ^ biner2
print("Hasil pada poin c adalah: ",c) #0000 1111

d= ~ biner1
print("Hasil pada poin d adalah: ",d)

e= biner2 & biner1
print("Hasil pada poin e adalah: ",e) #0000 0000
