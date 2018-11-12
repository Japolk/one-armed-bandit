from utils import  get_symbol_from_reel, check_any_bar,\
    check_cherries_with_any
from drawing import draw_bandit

class Bandit:
    reel_1 = {}
    reel_2 = {}
    reel_3 = {}

    payline = ['JP']* 3
    paytable = {}
    virtual_stops = 0
    symbols_to_unicode = {}

    cash = 100
    last_payout = 0
    is_win = False


    def __init__(self, reel_1={}, reel_2={}, reel_3={}, paytable={}, virtual_stops=0, symbols_to_unicode={}):
        self.reel_1 = reel_1
        self.reel_2 = reel_2
        self.reel_3 = reel_3
        self.paytable = paytable
        self.symbols_to_unicode = symbols_to_unicode
        self.virtual_stops = virtual_stops



    def pull_the_lever(self, selected_numbers):
        self.cash -= 1
        self.payline.clear()
        self.payline.append(get_symbol_from_reel(self.reel_1, selected_numbers[0]))
        self.payline.append(get_symbol_from_reel(self.reel_2, selected_numbers[1]))
        self.payline.append(get_symbol_from_reel(self.reel_3, selected_numbers[2]))


    def chek_combination(self):
        self.is_win = False
        check_any_bar(self.payline)
        check_cherries_with_any(self.payline)

        payline_tuple = tuple(self.payline)

        for symbols, payout in self.paytable.items():
            if payline_tuple == symbols:
                self.is_win = True
                self.cash += payout
                self.last_payout = payout


    def draw(self):
        unicode_payline = []
        for symbol in self.payline:
            unicode_payline.append(self.symbols_to_unicode[symbol])
        draw_bandit(unicode_payline)

    def make_move(self,selected_numbers):
        self.pull_the_lever(selected_numbers)
        self.draw()
        self.chek_combination()
        if self.is_win:
            print(f'WON ${self.last_payout}')
        print(f'BANK: ${self.cash}', end='\n\n')


pass