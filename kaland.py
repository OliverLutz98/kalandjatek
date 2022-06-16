i = 3

while i != 19 or i != 22:
    if i == 3:
        print(
            '8. az akciód nem jól sül el, mivel az égő csikktől meggyullad a szemét és lángra kap az egész bejárati ajtó\n'
            '9. a gondnok meghunyászkodva elkezdi összeseperni a szemetet.\n'
            '10. pechedre akkor ér oda melléd az a dögös csaj az évfolyamról, akinek szemlátomást nem jön be a viselkedésed.\n')
        user_input = int(input('Give me a number:'))
        if user_input == 8 or user_input == 9 or user_input == 10:
            i = user_input
