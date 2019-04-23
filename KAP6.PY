import requests 
# # # inter = int(input("ange ett positivt jämnt heltal"))
# # # url = "http://77.238.56.27/examples/numinfo/?integer=" 
# # # Iurl = url + str(inter)
# # # print(Iurl)
# # # print(inter)
# # # if(inter %2 == 0): 
# # #     print("hej")
# # #     r = requests.get(Iurl)
# # #     response_dictionary = r.json()
# # #     print(response_dictionary)  
# # # else:
# # #     print("Vi behöver ett jämt tal.")


# # UPPGIFT 6.2:

# stadcheck =    ["Stockholm",
# "Göteborg",
# "Malmö",
# "Uppsala",
# "Västerås",
# "Vasteras"]
# url = "https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/"
# stad = input("Vilken stad vill du se vädret ifrån")
# if stad in stadcheck:
#     checkurl = url + str(stad)
#     r = requests.get(checkurl)
#     response = r.json()
#     # print(response)

#     dab = response["forecasts"]
#     # print(dab)
  

#     for j in dab:
#         print(j)
       




    
# else:
#     print("Vi kan inte hitta staden")



#Uppgift 6:3

Artists = ["Ariana Grande",
"Avicii",
"Blink -182",
"Brad Paisley",
"Ed Sheeran",
"Imagine Dragons",
"Maroon 5",
"Scorpions"]

Url= "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"

nummer = 0
for artistname in Artists:
    print(artistname + " (ID)" + str(nummer))
    nummer +=1

selectid = int(input("Välj ett artist ID:"))

choosenartist = Artists[selectid]
print(choosenartist)

r = requests.get(Url)
response = r.json()
# print(response)
artistdic=response["artists"]
#print(artistdic)
artistfind = artistdic[selectid]
#print(artistfind)
searchid = artistfind["id"] 
Infourl = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/" + searchid 
x = requests.get(Infourl)
responsecool = x.json()
#if (choosenartist == int(1)): 
 #    print("F")
   # print(responsecool)
#else:
    #print(responsecool)
print(responsecool)


