from pelton import pelton
from kaplan import kaplan
from francis import francis


def ask():

    ask = input('select the type of turbine Pelton, Kaplan, Francis [p,k,f]: ').lower()
    if ask == 'p':
        print('PELTON WHEEL')
        pelton()
    elif ask == 'k':
        print('KAPLAN TURBINE')
        kaplan()
    elif ask == 'f':
        print('FRANCIS TURBINE')
        francis()
    else:
        print('oops! plz select appropriate turbine..')



ask()

