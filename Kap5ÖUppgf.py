# Namn = ["Daniel Radcliffe", "Rupert Grunt", "Emma Watson", "Selena Gomez"]
# Kön = ["Man", "Man", "Kvinna", "Kvinna"]
# Hfärg = ["Brun", "Röd", "Brun", "Brun"]
# ÖFärg = ["Brun", "Blå", "Brun", "Brun"]


# AKön = input("Ange kön ")
# AHfärg = input("Ange hårfärg ")
# AÖfärg = input("Ange ögonfärg ")

# AKön = AKön.capitalize()
# AHfärg = AHfärg.capitalize()
# AÖfärg = AÖfärg.capitalize()

# Lenname = 0 
# antalnamn = len(Namn)-1
# Rättnamn = []
# while(Lenname<=antalnamn):
#     if (AKön == Kön[Lenname]and AHfärg == Hfärg[Lenname] and AÖfärg == ÖFärg[Lenname]):
#         Rättnamn.append(Namn[Lenname])
#         Lenname+=1
#     else:
#         Lenname+=1
# if(len(Rättnamn)!=0):
#     print("Du liknar: ", Rättnamn)
# else:
#     print("Du liknar ingen känd kändis")


# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,]
# SH = [14, 13, 12, 11.5, 11, 11, 10.5, 10, 10, 10, 9.5, 9, 9, 9, 9, 8.5, 8]
# print("Hur gammal är du")
# IA = int(input())
# name = (input("skriv ditt för och efternamn"))
# if (IA >17):
#     print("Du behöver sova 8h timmar.")
# else:
#     ageLen = IA - 1
#     print("Hallå", name, "! Enligt Vårdguidens rekommendationer behöver individer i din ålder" , SH[ageLen] , "timmar sömn.")

Länder = ['sverige', 'norge', "danmark", "finland", "island", "england", "nordirland", "skottland", "wales"]

userland = (input("Vilket land"))
scandinavia=Länder[0:4]
GB = Länder[5:8]
Lowerland = userland.lower()
if Lowerland in scandinavia:
    print(Lowerland , "tillhör norden")
elif Lowerland in GB:
    print(Lowerland , "tillhör GB")
else:
    print("Landet är varken brittiskt eller skandinaviskt")
