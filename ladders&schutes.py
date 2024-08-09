import random

# Ölme mantığı ekleme
# zar atmadan önce seçeneklerin sunulması:isterse direkt 3 atmak gibi
# karakter seçme seçneği
# para sistemi ve paraların kullanımı örneğin ileriki tehlikeleri görme veya zarı tahmin ederek ekstra puan kazanmak
# trivia soruları

from typing import List

P1 = 0
P2 = 0
P3 = 0
P4 = 0
P5 = 0
P6 = 0
P7 = 0
P8 = 0
P9 = 0
P10 = 0

P1_hamle = []
P2_hamle = []
P3_hamle = []
P4_hamle = []
P5_hamle = []
P6_hamle = []
P7_hamle = []
P8_hamle = []
P9_hamle = []
P10_hamle = []
i = 0
b = random.randint(1, 6)

#otomatik düşürme ve yükseltme fonksiyonu
def dusus(bla):
    if bla == 6:
        bla = 0
    elif bla == 9:
        bla = 4
    else:
        pass
    return bla

#3 defa tekrar olunca 15 puan ek verme
#if (i >= (len(count)*3)):
#    if (P1_hamle[-1] == P1_hamle[-2] == P1_hamle[-3]):
#        P1 += 15
#        print("!Egemen gained additional 15 points for being consistent 3 rounds in a row.")
#P1 = dusus(P1)
#print(" Egemen rolled a " + str(b) + " and stays at " + str(P1) + ".")


#isim seçme
count=[]
while True:
    soru= str(input("Press a to add new players:"))
    if (soru.capitalize()=="A"):
        isim= str(input("Enter players name: "))
        count.append(isim)
    else:
        break

players= [P1,P2,P3,P4,P5,P6,P7,P8,P9,P10]

for j in range(10 - len(count)):
    del players[-1]

x=0
while x<10:
    for j in range(len(count)):
        b = random.randint(1, 6)
        players[j] += b
        players[j] = dusus(players[j])
        print( str(count[j]) + " rolled a " + str(b) + " and stays at " + str(players[j]) + ".")
    x+=1


players_name= {}
for j in range(len(count)):
    players_name[count[j]] = players[j]

ranking = dict(sorted(players_name.items(), reverse=True ,key=lambda item: item[1]))

print (players)
print (ranking)



#if (P1 > P2):
#    print("Egemen has won with " + str(P1) + " points. İlter lost with " + str(P2) + " points")
#elif (P1 == P2):
#    print("Tied")
#else:
#    print("İlter has won with " + str(P2) + " points. Egemen lost with " + str(P1) + " points")