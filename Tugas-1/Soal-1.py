nama = input ("Masukkan nama Anda : ")
b = input ("Masukkan umur Anda : ")
c = input ("Masukkan tinggi Anda : ")

umur = int (b)
tinggi = float (c)

# print (type (nama))
# print (type (umur))
# print (type (tinggi)) 

text = ("Nama saya {}, umur saya {} tahun dan tinggi saya {} cm.") .format (nama, umur, tinggi)
print (text)