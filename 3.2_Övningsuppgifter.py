# male = [
#     "Erik",
#     "Lars",
#     "Karl",
#     "Anders",
#     "Johan"
# ]

# female = [
#     "Maria",
#     "Anna",
#     "Margareta",
#     "Elisabeth",
#     "Eva"
# ]

# print("Vilket namn ska tas bort")

# print(male[0])
# print(female[2])
# print(female[3])
# print(male[1])
# print( 'Mansgrisar: ', male)
# print( 'Kvinnor:', female)


# #uppg3:2
# male = [
#     "Erik",
#     "Lars",
#     "Karl",
#     "Anders",
#     "Johan"
# ]

# female = [
#     "Maria",
#     "Anna",
#     "Margareta",
#     "Elisabeth",
#     "Eva"
# ]

# print("Vilket namn ska tas bort")

# print(male[0])
# print(female[2])
# print(female[3])
# print(male[1])
# del male[2]
# del male[2]
# del female[0]
# print( 'Mansgrisar: ', male)
# print( 'Kvinnor:', female)


# #uppgift3.3
# male = [
#     "Erik",
#     "Lars",
#     "Karl",
#     "Anders",
#     "Johan"
# ]

# female = [
#     "Maria",
#     "Anna",
#     "Margareta",
#     "Elisabeth",
#     "Eva"
# ]

# print("Vilket namn ska tas bort")

# print(male[0])
# print(female[2])
# print(female[3])
# print(male[1])
# del male[2]
# del male[2]
# del female[0]
# male.append("Elias")
# print( 'Mansgrisar: ', male)
# print( 'Kvinnor:', female)

# #UPPG3:3
# male = [
#     "Erik",
#     "Lars",
#     "Karl",
#     "Anders",
#     "Johan"
# ]

# female = [
#     "Maria",
#     "Anna",
#     "Margareta",
#     "Elisabeth",
#     "Eva"
# ]

# print("Vilket namn ska tas bort")

# print(male[0])
# print(female[2])
# print(female[3])
# print(male[1])
# del male[2]
# del male[2]
# del female[0]
# male.append("Elias")
# male.sort()
# female.sort()
# print( 'Mansgrisar: ', male)
# print( 'Kvinnor:', female)


male = [
    "Erik",
    "Lars",
    "Karl",
    "Anders",
    "Johan"
]

female = [
    "Maria",
    "Anna",
    "Margareta",
    "Elisabeth",
    "Eva"
]


print(male[0])
print(female[2])
print(female[3])
print(male[1])
del male[2]
del male[2]
del female[0]
male.append("Elias")
male.sort()
female.sort()
print( 'Mansgrisar: ', male)
print( 'Kvinnor:', female)
print("Vilket namn ska tas bort")
tabort = (input())
if tabort in male:
    male.remove(tabort)
if tabort in female:
    female.remove(tabort)
print( 'Mansgrisar: ', male)
print( 'Kvinnor:', female)