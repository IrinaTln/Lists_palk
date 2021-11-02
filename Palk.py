from random import *
inimised=["Иванов", "Петров", "Боширов", "Сидоров", "Сидоров", "Васечкин", "Петров", "Петичкин"]
palgad=[7000, 1000, 2000, 3000, 4000, 5000, 6000, 2000]

def sisesta_andmed(i,p): #Добавить в список новых четыре фамилии
    N=4
    for n in range(N):
        a=input("Введите фамилию нового работника: ")
        i.append(a)
        palk=randint(100,10000)
        p.append(palk)
    return i,p

def andmed_ekranile(i,p): #выврдим на экран список имен и зарплат
    N=len(i)
    for n in range(N):
        print(i[n],"-",p[n])

def kustutamine(i,p): #удаляем человека из списка
    nimi=input("Введите имя для удаления из списка: ")
    n=i.count(nimi)
    abi_list=[]
    if n>0:
        t=0
        for e in range(len(i)):
            if i[e]==nimi:
                t+=1
                abi_list.append(int(e)) #список индексов
                print(t,". ",i[e],"-", p[e])
        jaar=int(input("Порядковый номер: "))
        i.pop(abi_list[jaar-1])
        p.pop(abi_list[jaar-1])
        andmed_ekranile(i,p)

    return i,p

def suur_palk(i,p): #находим самую большую зарплату
    suurim=max(p)
    j=p.count(suurim)
    abi_list2=[]
    if j>0:
        g=0
        for t in range(len(p)):
            if p[t]==suurim:
                g+=1
                abi_list2.append(int(t))
                print(g, "-", p[t],'-',i[t])
        jaar=int(input("Введите удаляемый номер: "))
        i.pop(abi_list2[jaar-1])
        p.pop(abi_list2[jaar-1])
        andmed_ekranile(i,p)
    return(i,p)

def sorteerimine(i,p,v): #сортиуем зарплату по возрастанию
    N=len(p)
    if v==2:
        for n in range(0,N):
            for m in range(n,N):
                if p[n]<p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi
    elif v==1:
        for n in range(0,N): #сортируем зарплату по убыванию
            for m in range(n,N):
                if p[n]>p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi
    andmed_ekranile(i,p)

def vordsed_palgad(i,p):
    N=len(p)
    dublikatid=[x for x in palgad if palgad.count(x)>1]
    dublikatid=list(set(dublikatid))
    for palk in dublikatid: 
        n=p.count(palk)
        k=-1
        for j in range(n): 
            k=p.index(palk, k+1)
            nimi=i[k]
            print(palk, "получают", nimi)

def name_search1(i,p):
    nimi=input("Введите имя работника: ")
    n=i.count(nimi)
    if n>0:
        t=0
        for e in range(len(i)):
            if i[e]==nimi:
                t+=1
                print(t,". ",i[e]," - ", p[e] )

def more_under(i,p,v): #сортировка зарплаты по возрастанию или убыванию
    number=int(input("Введите зарплату от которой начинать сортировку: "))
    abi_list3=[]
    g=0
    if v==1:
        for t in range(len(p)):
                if p[t]>number:
                    g+=1
                    abi_list3.append(int(t))
                    print(g, "-", p[t],'-',i[t])
    elif v==2:
        for t in range(len(p)):
                if p[t]<number:
                    g+=1
                    abi_list3.append(int(t))
                    print(g, "-", p[t],'-',i[t])

def top3(i,p,v): #три самых высоких зарплаты
    if v==1:
        p.sort()
        p.reverse()
        i.sort()
        i.reverse()
        for h in range (0,len(p),1):
            if h>=3:
                break
            print(p[h])
            print(i[h])
    elif v==2:
        p.sort()
        i.sort()
        for j in range(0,len(p),1):
            if j>=3:
                break
            print(p[j])
            print(i[j])

def keskmine(i,p): #средняя зарплата по больнице
    summa=0
    for palk in p:
        summa+=palk
    summa/=len(p)
    print("Средняя зарплата: ", summa)
    for palk in p:
            if palk==summa:
                n=p.index(palk)
                print("Зарплату получает", i[n])
            else:
                print("Работников, которые получают строго такую сумму нет.")
    
def tulumaks_pl(i,p):
    tulumaks=0
    pl=0
    for f in range(len(p)):
        if p[f]<1200:
            pl=int(p[f])
            tulumaks=(pl-((pl-500)*0.2))
            print(tulumaks," - ", i[f])
        elif p[f]>=1201 and p[f]<2099:
            pl=int(p[f])
            tulumaks=pl-(500-0.55556*(pl-1200))*0.2
            print(tulumaks," - ", i[f])
        elif p[f]>2100:
            pl=int(p[f])
            tulumaks=pl-(pl*0.2)
            print(tulumaks," - ",i[f])

def sorteerimine_nimi_jargi (p,i,v): #сортиуем по именам от А до Я
    N=len(p)
    if v==2:
        for n in range(0,N):
            for m in range(n,N):
                if p[n]<p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi

    elif v==1:
        for n in range(0,N): #сортируем в обратном порядке от Я до А
            for m in range(n,N):
                if p[n]>p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi
    andmed_ekranile(i,p)

def keskmine_kustutamine(i,p): #удаление всех зарплат ниже средней
    summa=0
    new_list5=[]
    for palk in p:
        summa+=palk
    summa/=len(p)
    print("Средняя зарплата составляет - ", summa, " все зарплаты ниже этой цифры будут удалены!")
    w=0
    while w<len(p):
        if p[w]<summa:
            del p[w]
        else:
            w+=1
    print("В списке зарплат остались зарплаты выше средней: ",p)
       


while 1:
    print("a - ввод данных: \ne - вывод на экран: \nk - удаление: \nm - удалить человека с самой высокой зарплатой: \nh - сортировка по убывания: \np - одинаковые зарплаты.\nz - топ три.\ny - повторяющиеся имена.\nu - поиск зарплат по имени.\nw - вывод зарплат по показателю.\nr - хозяин средней зарплаты в списке.\nv - зарплаты с налоговым вычетом.\ns - сортировка по имени.\nl - удаление зарплат ниже средней.")
    valik=input()
    if valik.lower()=="a":
        inimised,palgad=sisesta_andmed(inimised,palgad)
    elif valik.lower()=="e":
        andmed_ekranile(inimised, palgad)
    elif valik.lower()=="k":
        inimised,palgad=kustutamine(inimised, palgad)
    elif valik.lower()=="m":
        inimised,palgad=suur_palk(inimised, palgad)
    elif valik.lower()=="h":
        sorteerimine(inimised,palgad,int(input("1 - сортировка по убыванию, 2 - сотрировка по убыванию.")))
    elif valik.lower()=="p":
        vordsed_palgad(inimised, palgad)
    elif valik.lower()=="z":
        top3(inimised,palgad, int(input("1 - топ трех самых богатых, 2 - топ трех самых бедных.")))
    elif valik.lower()=="y":
        name_search(inimised,palgad)
    elif valik.lower()=="u":
        name_search1(inimised, palgad)
    elif valik.lower()=="w":
        more_under(inimised, palgad, int(input("1 - сортировка от и выше, 2 - сортировка от и меньше.")))
    elif valik.lower()=="r":
        keskmine(inimised,palgad)
    elif valik.lower()=="v":
        tulumaks_pl (inimised,palgad)
    elif valik.lower()=="s":
        sorteerimine_nimi_jargi(inimised,palgad, int(input("1 - сортировка от А до Я, 2 - сортировка от Я до А")))
    elif valik.lower()=="l":
        keskmine_kustutamine(inimised,palgad)
    else:
        break