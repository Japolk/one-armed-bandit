import time

from bluejay_bonanza_slot_machine_data import\
    my_paytable, my_reel_1, my_reel_2, my_reel_3,\
    my_symbols_to_unicode, my_virtual_stops

from bandit import Bandit
from random_squence_generator import get_random_sequence
from utils import take_integer_on_input



slot_machine = Bandit(my_reel_1,
                      my_reel_2,
                      my_reel_3,
                      my_paytable,
                      my_virtual_stops,
                      my_symbols_to_unicode)

availabble_moves = ('spin', 's','help','exit', 'autoplay', 'cheat spin')

print('WELCOME TO CASINO!')
take_integer_on_input('Make you Deposit(integer value): ')
slot_machine.draw()

while True:

    move = input('Make your move:')

    while move not in availabble_moves:
        print('type \'help\' for help')
        move = input('Make your move:')

    if move == 'help':
        print("""
        type 'spin' or 's' to start the round;
        type 'exit' to take your money and leave;
        type 'autoplay', make computer spin for you every second;
        type 'help' for help.
        pssst, secret command:'cheat spin'.
        """)

    if move == 'spin' or move == 's':
        sequence = get_random_sequence(128)
        slot_machine.make_move(sequence)

    if move == 'cheat spin':
        slot_machine.make_move([127,127,127])

    if move == 'autoplay':
        games_number = take_integer_on_input('type number of games you want to autoplay: ')
        for counter in range(games_number):
            sequence = get_random_sequence(128)
            slot_machine.make_move(sequence)
            time.sleep(1)
    if move =='exit':
        break

print(f'You Got ${slot_machine.cash}')
