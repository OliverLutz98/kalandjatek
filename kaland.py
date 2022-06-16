i = 1

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
        user_input = int(input('Give me a number: \n'))
        if user_input == 5 or user_input == 6 or user_input == 7:
            i = user_input

    if i == 6:
        print('4. odaér a haverod, Béci is. Rágyújtotok egy újabb cigire.\n'
              '15. megbököd a vállát és megkínálod cigivel, elfogadja és rágyújt.\n'
              '16. Bemész a suliba. Feszkós vagy, ezért betörsz egy ablakot a folyosón.\n')
        user_input = int(input('Give me a number: \n'))
        if user_input == 4 or user_input == 15 or user_input == 16:
            i = user_input
