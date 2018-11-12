printable_paytable = [(u'\U0001F4B0  \U0001F4B0  \U0001F4B0  ', 2000),('7   7   7   ', 330),('☰   ☰   ☰   ', 120),
                      ('=   =   =   ', 60),('―   ―   ―   ', 30),('any ― x3    ', 16),
                      (u'\U0001F352  \U0001F352  \U0001F352  ', 16),
                      (u'\U0001F352  \U0001F352 any  ',8),(u'\U0001F352 any any  ',4)
                    ]
u_l_corner = '\u2554'
u_r_corner = '\u2557'
b_l_corner = '\u255A'
b_r_corner = '\u255D'
vertical = '\u2551'
horizontal = '\u2550'
background = '\u2591'
logo = '    BANDITO!'
x_size = 11
y_size = 16

def draw_bandit(symbols):
    print()
    for x in range(x_size):
        for y in range(y_size):
            draw_block(x,y, x_size-1, y_size-1, symbols)
        print(' '*4, end='')
        try:
            print(f'{printable_paytable[x][0]}${printable_paytable[x][1]}')
        except IndexError:
            print()



def draw_block(x,y, x_size,y_size, symbols):
    if x == y == 0:
        print(u_l_corner, end='')
    elif x == x_size and y == y_size:
        print(b_r_corner, end='')
    elif x == 0 and y == y_size:
        print(u_r_corner, end='')
    elif x == x_size and y == 0:
        print(b_l_corner, end='')
    elif x ==0 or x == x_size:
        print(horizontal, end='')
    elif y ==0 or y == y_size:
        print(vertical, end='')
    elif x == 5 and y in range(3, 13):
        draw_screen(y, symbols)
        # print(' ', end='')
    elif x == 2 and y in range(4, 12):
            print(logo[y], end='')
    else:
        print(background, end='')


def draw_screen(position, sequence):
    index = 100
    if position == 4:    index = 0
    elif position == 7:  index = 1
    elif position == 10: index = 2
    elif position == 5:  index = 3
    elif position == 8:  index = 4
    elif position == 11: index = 5

    if index in (0,1,2):
        print(sequence[index], end='')
    elif index in(3,4,5):
        try:
            if sequence[index-3] in (u'\U0001F352', u'\U0001F4B0'):
                print('',end='')
            else:
                print(' ', end='')
        except IndexError:
            pass
    else:
        print(' ', end='')

