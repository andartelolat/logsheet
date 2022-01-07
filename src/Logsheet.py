
print("==========SELAMAT NGERAPEL============")
#WAKTU
W = float(input("Masukkan jam awal rapel CF 1: "))
X = float(input("Masukkan jam awal rapel CF 2: "))
#CF1
A = float(input("Masukkan Counter Awal CF 1  : "))
B = float(input("Masukkan Counter Akhir CF 1 : "))
#CF2
Y = float(input("Masukkan Counter Awal CF 2  : "))
Z = float(input("Masukkan Counter Akhir CF 2 : "))

C = B-A #selisih CF1 
I = Z-Y #selisih CF2

print("Selisih Nilai Counter CF 1 : ", C)
print("Selisih Nilai Counter CF 2 : ", I)

#input block
D = int(input("Masukkan jumlah Block CF 1 : "))
J = int(input("Masukkan jumlah Block CF 2 : "))

E = C/D #rata-rata CF2
K = I/J #rata-rata CF2

print("Rata-rata flow tiap jam adalah CF 1 : ",E,"Ton/Jam")
print("Rata-rata flow tiap jam adalah CF 2 : ",K,"Ton/Jam")
L = 0
G = 0
#Cetak Log Unit 1
print ("=============CF 1=============")
print ("Jam ",W, " | " ,A, " | ")
while G < D :
    print ("Jam ",W+1, " | " ,A+E, " | ")
    A = A+E
    W = W+1
    G = G + 1
#Cetak log Unit 2
print ("=============CF 2=============")
print ("Jam ",X, " | " ,Y, " | ")
while L < J :
    print ("Jam ",X+1, " | " ,Y+K, " | ")
    Y = Y+K
    X = X+1
    L = L+1

print ("=========AMPURE MAKASI========")
print ("========AMPURE TESTING========")
print ("=========IBEN SANDARU=========")
