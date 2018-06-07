def gra():
    #mozna by w sumie zrobic jakas ladna ramke
    tabelka= [None] + list(range(1, 10))
    wygrane = [
       (1, 2, 3),
       (4, 5, 6),
       (7, 8, 9),
       (1, 4, 7),
       (2, 5, 8),
       (3, 6, 9),
       (1, 5, 9),
       (3, 5, 7),
    ]
#wygrane kombinacje w grze
    def rozstawienie():
        print(tabelka[1], tabelka[2], tabelka[3])
        print(tabelka[4], tabelka[5], tabelka[6])
        print(tabelka[7], tabelka[8], tabelka[9])
        print()
#plansza początkowa
    def wybierz_numer():
        while True:
            try:
                a = int(input())
#zmienna a przechowuje cyfre podana przez gracza, warunek sprawdza, czy gracz podal niezajeta juz
#cyfre lub nie uzyl niedozwolonych znakow
                if a in tabelka:
                    return a
                else:
                    print("Podaj jeszcze nieuzyta liczbe!")
            except ValueError:
               print("Podaj numer z planszy")
#program sprawdza czy zmienne a,b,c sa ulozone w jednej kombinacji prowadzacych do zwyciestwa lub remisu
    def koniec():
        for a, b, c in wygrane:
            if tabelka[a] == tabelka[b] == tabelka[c]:
                print("Gracz {0} wygrywa!\n".format(tabelka[a]))
                print("Gratulacje!\n")
                return True
#nastepuje, gdy wszystkie pola na planszy zostaly zajete, ale nie wystapila zadna ze zwycieskich kombinacji
        if 9 == sum((pos == 'X' or pos == 'O') for pos in tabelka):
            print("Koniec gry! Remis\n")
            return True
#petla sprawdza, czy plansza nie zostala zapelniona, jesli tak, to nastepuje koniec rozgrywki.
#jesli nie, tura przechodzi na kolejnego gracza
    for gracz in 'XO' * 9:
        rozstawienie()
        if koniec():
            break
        print("Ruch gracza {0}, wybierz liczbę: ".format(gracz))
        tabelka[wybierz_numer()] = gracz
        print()
#koniec gry i pytanie o rozpoczecie ponownej rozgrywki
while True:
    gra()
    if input("Zagraj ponownie (y/n)") != "y":
        raise SystemExit
        #break
        #dobra powinno wyrzucac jak sie wcisnie cos innego od y
#zamiast brejka mozna by bylo zrobic zeby sie program zamykal jak juz nie chca grac
