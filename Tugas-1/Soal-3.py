a = input ("Silakan masukan nilai ujian teori : ")
b = input ("Silakan masukan nilai praktik : ")

ujian = float (a)
praktik = float (b)

if (ujian > 70 and praktik > 70):
    print ("Selamat, anda lulus!")

elif (ujian > 70 and praktik < 70):
    print ("Anda harus mengulang ujian praktik.")

elif (ujian < 70 and praktik > 70):
    print ("Anda harus mengulang ujian teori.")

elif (ujian < 70 and praktik < 70):
    print ("Anda harus mengulang ujian teori dan praktik.")

else:
    print ("Error")