# Uppgift 2.1
# citat="datatyper har inbyggda metoder"
# print(citat.upper()) #"Upper" skriver ut allt i uppercase (lower gör motsatsen)


#Uppgift 2.2:

# a = float(input()) #a blir en input som blir en float, b är a fast int, skriv b (så en avrundad int kommer ut)
# b = int(a)
# print(b)



# print('"Dator": Hallå!')
# print('"Dator": Vad är ditt förnamn?')
# a = input()
# print('"' + a + '": ' + 'Mitt namn är ' + a)
# print("Dator: Vad är ditt efternamn")
# b = input()
# print('"' + a + '": '  + 'Mitt efternamn är ' + b)
# print('"Dator": Trevligt att träffa dig, ' + a +" " + b "!")

# #Kan ju vara kul att lära sig om hur man får med citattecken i strings, var dock svårt. a är förnamn, b är efternamn


#Uppgift 2.4

# print("Hur gammal är du?")
# a = int(input())
# b = 18-a
# print("Du är myndig inom " + str(b) + "år!")

# Uppgift 2.5
# import math
# print("Hej! Hur många ville ha två vanliga korvar?")
# VanligKorv2 = int(input())
# print("Och tre vanliga?")
# VanligKorv3 = int(input())
# print("Okej, Hur många vill ha två veganska korvar?")
# VeganKorv2 = int(input())
# print("Okej, Hur många vill ha tre sådana?")
# VeganKorv3 = int(input())
# Korvar= VanligKorv2*2+VanligKorv3*3
# Vegkorvar = VeganKorv2*2+VeganKorv3*3
# dryck= VanligKorv2+VanligKorv3+VeganKorv2+VeganKorv3 #Antal drickor är en per person, alltså en per val
# Korvpaketz = (Korvar/8)
# Vegkorvpaketz = (Vegkorvar/4)
# Korvpaket = math.ceil(Korvpaketz)
# Vegkorvpaket = math.ceil(Vegkorvpaketz)
# Priz = Vegkorvpaket*34.95+Korvpaket*20.95+dryck*13.95
# Pris = math.ceil(Priz)
# print("Korvpaket: " + str(Korvpaket) + " Vegkorvpaket: " + str(Vegkorvpaket) + " Drickor: " + str(dryck) + " Pris: " + str(Pris)) #Skapade en massa variabler som var inputbaserade, sedan avrundade jag alltid korvar per paket uppåt.

