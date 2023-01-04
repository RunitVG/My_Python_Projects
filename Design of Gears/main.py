from spur import spur
from helical import helical
from bevel import bevel



def choose_gear():
    user_input = input('Spur[S], Helical[H], Bevel[B]: ').lower()
    if user_input == 's':
        print('CALS FOR SPUR GEAR \n')
        spur()
    elif user_input == 'h':
        print('CALS FOR HELICAL GEAR \n')
        helical()
    elif user_input == 'b':
        print('CALS FOR BEVEL GEAR \n')
        bevel()
    else:
        print('oops! plz choose appropriate gear type')
        choose_gear()


choose_gear()
