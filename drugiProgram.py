# promenjive i tipovi
'''
print("hello world!")
print(123)
print(1.5)

'''
# escaping operator \ignorise karakter naveden pored njega
# ctrl + / za komentarisanje i odkomntarisanje
# print('naziv knjige \"Python knjiga\" je u prodaji')
# print("neki tekst")
# print("print" class def")
print("Cao","Hello",3,1000,'abc')

naziv_proizvoda = "Jakna"
print("Proizvod:",naziv_proizvoda)
cena = 12000
print("Cena proizvoda",cena)
print(id(cena))

cena = 30000
print(id(cena))
print(cena)

klub  = "Denver Nuggets"
igrac = "Sasa Djordjevic"
broj  = 25
godine = 30
broj_ocekivano = 15
igrac_ocekivano = "Nikola Jokic"


print(broj_ocekivano, broj)
print(igrac_ocekivano, igrac)
broj1 = 5
broj2 = 7
zbir= broj1+ broj2
zbir_ocekivano = 12
print(zbir, zbir_ocekivano)

print(igrac)
print(godine)
print(broj)

godine_uvecano = godine  + 1
print(godine_uvecano) 


# igrac =input("Unesite ime igraca:") 
# godine = input("Unesite godine igraca:")# iz inputa je tekst
# #"29"
# print("Uneli ste:",igrac,godine)
# #29
# print("Sledece godinece da ima",int(ggodine)+1)




knjiga = "Python programiranje"
print("Nova knjiga:",knjiga)
ispis = f"Nova knjiga:\{knjiga}\""
print(ispis)
print(f"Nova knjiga:\"{knjiga}\"")
# model:Samsung, cena: 150$, boja: crvena- akcija
model = "Samsung"
cena = 150
boja = "crvena"
print("Model",model,"Cena",cena,"Boja",boja)
print(f"Model:{model},\n cena:{cena},boja:{boja}- na akciji")
# primer za razmaka i novi red
# \t -tab \n novi red
print("*\t*\t*")
print("*\n*\n*")
'''

Temperatura je     15 tepeni
grad je  Beograd
suncano  false
'''

#temperatura   = 15 
#grad ="Beograd"  
#suncano =False

#print(f"Temperatura je\t{temperatura},stepeni\ngrad je\t{grad},\nsuncano\t{suncano}")


temperatura = 2
grad = "Beograd"
opis = "Sneg"
# Trenutna temperatura: 1 stepen
# Grad: Beograd 
# Trenutmo je : sneg

print("Trenutna temperatura:",temperatura,"stepen")
print(f"Trenutna temperatura:{temperatura}stepen\nGrad:{grad}\nTrenutno je:{opis}")


ispis = "Trenutna temperatura: " + str(temperatura)
print(ispis)
opis_prognoze = "Trenutno je: " + opis
print(opis_prognoze)
print(ispis + " " + opis_prognoze) # konkatenacija stringova
# unesite prvi broj,  drugi broj, ispis rezultata
broj1 = 20 #input("Unesite prvi broj:")
broj2 = 50 #input("Unesite drugi broj:")
ocekivano = 60
# == operator poredjenja - jednakosti
rezultat = int(broj1) + int(broj2)
print(f"Rezultat je :{rezultat}")
print(rezultat == ocekivano)

# deljenje bez ostatka
print(10//2)
print(9//2)
print(2**8) # stepenovanje, posle** je stepen
# celobrojni ostatak pri deljenju
print(10 % 3) # 3*3+1 
print (10 % 2)
# r na kvadrat pi - povrsina kruga
poluprecnik = 10
pi = 3.14
povrsina = poluprecnik*poluprecnik*pi # poluprecnik**2*pi
print(povrsina) 
ocekivano = 78.5
dobijeno = povrsina
print(ocekivano == dobijeno)
print(- ocekivano)

#auto_x = 0
#parking_x = 40
 #auto_x += parking_x # odmaah je stigaox
#print(auto_x)
#auto_x += 10
#print(auto_x)
#auto_x += 10
#print(auto_x)
# auto_x += 10
#print(auto_x)
#auto_x += 10
#print(auto_x)
# proveri da li auto na poziciji parkinga
#print("Stigai",auto_x == parking_x)
#auto_X -= 5
#print("Stigao", auto_x == parking_x)
#auto_x *= 2
#print(auto_x)

# izracunaati porez 20% od cene
#Cena = int(input("Unesite cenu :"))
#porez = 0.2


'''porez_na_cenu = cena * porez # rezulatat programa
# test - unosim 1000 ocekujem  da je  porez 200
ocekivano =200
dobijeno = porez_na_cenu
print("Test prosao:",ocekivano == dobijeno)
rezultat_teksta = ocekivano == dobijeno
print(rezultat_teksta)
print(f"Uneli ste cenu:{cena}, porez na cenu:{porez_na_cenu}")'''


# ustanoviti da li broj paran ili neparan
#broj = 10
# % celobrojni ostatak pri deljenju
ostatak = 10 % 2
print(ostatak)
#broj je paran: True
 #kada je deljiv sa dva nema ostatak
print("Broj je paran:",ostatak == 0)
# != razlicito == jednakost





'''auto_x = 0
parking_x = 10

auto_x += 2
print("Nije stigao :", auto_x != parking_x)
auto_x +=2
print("Nije stigao:", auto_x != parking_x)

korisnicko_ime_baze = "admin"
uneto_ime = input("Unesite korisnicko  ime:")
# uspesno logovanje : True/False
# neuspesno logovanje: True /False
print("Uspesno logovanje:", korisnicko_ime_baze == uneto_ime)
print("Neuspesno  logovanje:", korisnicko_ime_baze != uneto_ime)'''


'''igrac_1_x = 0
igrac_2_x = 50
metak  = 0
brzina = 10
jacina = 20
# umanji za jacinu udarca
igrac_2_health =100
metak += brzina
print(metak == igrac_2_x)
igrac_2_health -= jacina
http://collabedit.com/qn4nm'''


print("hello")

  

            



i = 0
while(i < 5) :
print ("Hello")
i=i+1


























