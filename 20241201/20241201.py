# Örnek listeler
stringlist = """\
3   4
4   3
2   5
1   3
3   9
3   3\
"""


liste1 = []
liste2 = []

def puzzle1():
# Listenin öğeleri alt alta olduğu için \n (newline) ile ayırıyoruz.
    for i in stringlist.split("\n"):
# listenin boşluktan önceki elemanları liste1 e alınır.
        liste1.append(int(i.split("   ")[0]))  
# Boşluktan sonraki elemanlar liste2 ye alınır.
        liste2.append(int(i.split("   ")[1]))

# Her iki liste küçükten büyüğe sıralanır.
    liste1.sort()
    liste2.sort()

    sum = 0
# Her bir eleman örnekte gösterildiği gibi büyükten küçüğün farkı alınır ve toplam değişkenine eklenir.
    for i in range(len(liste1)):
        if liste1[i] >= liste2[i]:
            sum += liste1[i] - liste2[i]
        else:
            sum += liste2[i] - liste1[i]
    
    return sum

def puzzle2():
    sum = 0
    for i in liste1:
# liste1 deki elemanın liste2 deki sayısı(count) bulunur ve liste1 deki eleman ile çarpılıp toplama yazılır.
        sum += i * liste2.count(i)

    return sum


# Toplamlar print edilir
print(puzzle1())
print(puzzle2())
"""
Advent Of Code 1.Gün
Problem 1

Her satırı 3 boşluk ile ayrılmış iki farklı liste verilmiştir.
Listelerdeki elemanların küçükten büyüğe eşleştirilip, eşleştirilen elemanların büyük olan elemandan çıkarılması istenmektedir.
Yukarıdaki listeye göre örnek:
    Eşler  : 1,3    Farklar : 3-1 = 2
             2,3              3-2 = 1
             3,3              3-3 = 0
             3,4              4-3 = 1 
             3,5              5-3 = 2
             9,4              9-4 = 5

Bütün elemanların farkının toplamı return edilmelidir.
(2+1+0+1+2+5) = 11


Problem 2

Aynı listelerde, 1.listede olan sayının 2.listede kaç defa geçtiğinin çarpımı bulunmalıdır.
Örnek:
    3, 2.listede 3 defa geçmektedir.    3*3 = 9
    4, 2.listede 1 defa geçmektedir.    4*1 = 4
    2, 2.listede hiç geçmemektedir.     2*0 = 0
    1, 2.listede hiç geçmemektedir.     1*0 = 0
    3, 2.listede 3 defa geçmektedir.    3*3 = 9
    3, 2.listede 3 defa geçmektedir.    3*3 ? 9
Toplamı return edilir.
(9+4+0+0+9+9) = 31
"""
