while i != 19 or i != 22:

    if i == 1:
        print('Te vagy az iskola rosszfiúja. Késve érkezel a suli elé, még elszívod a cigidet, aztán… \n'
              '2. elnyomod a csikket az igazgatónő bringájának kerekébe. \n'
              '3. felrúgod a bejárat melletti szemeteskukát és mellé pöccinted a csikket.  \n'
              '4. odaér a haverod, Béci is. Rágyújtotok egy újabb cigire. \n')
        user_input = int(input('Give me a number:'))
        if user_input == 2 or user_input == 3 or user_input == 4:
            i = user_input

    if i == 2:
        print('észreveszi az éppen érkező töri tanárod, mit tettél és…\n'
              '5. azonnal felrángat az igazgatói irodába. Te hőzöngve tiltakozol végig a folyosón.\n'
              '6. gratulál neked, hisz szerinte is egy nagyképű szipirtyó a nő. \n'
              '7. szó nélkül tovább sétál, mivel eléggé parázik tőled.\n')
        user_input = int(input('Give me a number:\n'))
        if user_input == 5 or user_input == 6 or user_input == 7:
            i = user_input

    if i == 4:
        print('11. Béci rávesz, hogy lógjátok el az egész napot. Belemész.\n'
              '12. kiszúrod az éppen közeledő dögös csajt az évfolyamról és megszólítod.\n'
              '13. kiszúrod az éppen közeledő dögös csajt az évfolyamról és Béci megszólítja.\n')
        user_input = int(('Mit választasz? Írj be egy számot:\n'))
        if user_input == 11 or user_input == 12 or user_input == 13:
            i = user_input

    if i == 12:
        print('15. megbököd a vállát és megkínálod cigivel, elfogadja és rágyújt.  \n'
              '20. sikerül valami nyálas dumát nyomnod a kék szemeiről. \n'
              '21. elküld a francba.\n')
        user_input = int(input('Give me a number:'))
        if user_input == 15 or user_input == 20 or user_input == 21:
            i = user_input

    if i == 14:
        print('19. a legközelebbi kocsmáig meg se állsz és piszkosul berúgsz. \n'
              '21. elküld a francba.\n'
              '12. kiszúrod az éppen közeledő dögös csajt az évfolyamról és megszólítod.\n'
              'Mit választasz? Írj be a számot:\n')
        user_input = int(input("adj meg egy számot:"))
        if user_input == 19 or user_input == 21 or user_input == 12:
            i = user_input
