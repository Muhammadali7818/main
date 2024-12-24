def sontaqsimlash(sonlar):
    toq_sonlar = []
    for i in sonlar:
        if i % 2 != 0:  
            toq_sonlar.append(i)
    return toq_sonlar

sonlar = [12, 7, 34, 55, 23, 8, 19, 42, 91, 6]

toq_sonlar = sontaqsimlash(sonlar)
print("Toq sonlar:", toq_sonlar)