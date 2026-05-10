import os
os.system("cls")

# 1.m
# users = [
#     'Abdulla Abdullaev', 
#     'Samandar Asadov', 
#     'Shaxnoza Jurayeva', 
#     'Ikrom Karimov',
#     'Gulnora Xalilova',
#     'Ziyoda Yuldashova'
#     ]
# men = []
# women =[]
# for i in users:
#     if i[-2:]== "ov" or i[-2:]=="ev":
#         men.append(i)
#     elif i[-2:] == "va":
#         women.append(i)
# print("men = ",men)
# print("women = ",women)
    


# 2.m
# mahsulot = {
#     "olma": [13000, 14000, 15000],
#     "anor": [19000, 22000, 24000, 15000],
#     "gilos": [6000, 9000, 5000, 4000],
#     "banan": [30000, 28000]
# }
# def chiqar(mahsulotlar):
#     for i,j in mahsulot.items():
#         narxi = sum(j)
#         print(i," = ",narxi)

# chiqar(mahsulot)
  
  
# 3.m
# books = [
#     ("O'tkan kunlar", "Roman"),
#     ("Mehrobdan chayon", "Roman"),
#     ("Shum bola", "Povest"),
#     ("Alkimyogar", "Roman"),
#     ("Boy va kambag'al", "Hikoya"),
#     ("Urush va tinchlik", "Roman"),
#     ("Kecha va kunduz", "Roman"),
#     ("Yulduzli tunlar", "Povest"),
#     ("Qorako'z Majnun", "Hikoya"),
#     ("Qalb ko'zi", "Hikoya")
# ]

# book = {}

# for i,j in books:
#     if j not in book:
#         book[j] = []
#     book[j].append(i)
# print(book)



# 4.m
# def bank(dep,foiz,yil):
#     s=0
#     for i in range(yil):
#         s+= dep*foiz/100
#     natija = dep + s
#     return natija

# print(bank(10000,24,3))

