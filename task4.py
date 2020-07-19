d=dict()
lc=[]
lt=[]
k=int(input('количество стран'))  #количество стран
for i in range(k):
    s=input('Введите строку: ') #ввод названия страны и городов
    l=s.split()
    print(l)
    lc.insert(len(lc),l[0])
    print(lc)
    lt.insert(len(lt),l[1:len(l)])
    print(lt)
    d=dict(zip(lc,lt))
    print(d)
k=int(input('kоличество городов')) 
for i in range(k):
    city=input('Введите строку: ')
    for key, value in d.items():
        if city in value:
            print(key)

# countries = dict()
# list_country = []
# list_sity = []
# how_many_countries = (3)
# for i in range(how_many_countries):