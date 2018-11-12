def get_symbol_from_reel(reel, selected_number):

    for reel_range, symbol in reel.items():
        if selected_number in reel_range:
            return symbol


def check_any_bar(payline):
    if payline.count('3bar') != 3 and \
        payline.count('2bar') !=3 and \
        payline.count('bar') !=3:
        for i in range(3):
           if payline[i] == 'bar' or payline[i][1:] == 'bar':
               payline[i] = 'any_bar'


def check_cherries_with_any(payline):
    if payline.count('cherry') in(1,2):
        for i in range(3):
            if payline[i] != 'cherry':
                payline[i] = 'any'


def take_integer_on_input(message):
    input_int = 0
    while not input_int:
        try:
            input_int = int(input(message))
        except ValueError:
            print('Please type integer number')
            continue
    return input_int


def paytable_to_list(paytable):
    paytable_list = []
    for key, value in paytable.items():
        paytable_list.append((key,value))
    return paytable_list