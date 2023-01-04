import math

global h


def rect_cs():
    # for rect cs
    Lc = float(input('Characteristic Length of Fin (m): '))
    k = float(input('Thermal Conductivity for Fin (W/mK): '))
    cp = float(input('Sp. Heat Capacity (J/kgK): '))
    Ts = float(input('Base Temperature: '))
    Tinf = float(input('Surrounding Temperature: '))
    # l = float(input("Length of Fin: "))
    Tm = (Ts + Tinf) / 2
    dT = Ts - Tinf
    F_or_N = input('Forced or Natural Convection (F/N): ').lower()

    def natural_conv():
        print('NATURAL CONVECTION')
        g = 9.81
        B = float(input('Coefficient of Thermal Expansion (x10^-6): '))
        B = B / 1000000
        # viscosity
        try:
            v = float(input('Kinematic Viscosity (x10^-5): '))
            v = v / 100000
            roh = float(input('Density: '))
            mu = v * roh
        except:
            mu = float(input('Dynamic Viscosity(x10^-5): '))
            mu = mu / 100000
            roh = float(input('Density: '))
            v = mu / roh
        Gr = (g * B * dT) * Lc ** 3 / v ** 2
        print(f'Grashoffs Number: {Gr}')
        Pr = mu * cp / k
        print(f'Prandtls Number: {Pr}')

        if 10 ** 5 < (Gr * Pr) < 10 ** 7:
            Nu_up = 0.54 * (Gr * Pr) ** (1 / 4)
        elif 10 ** 7 < (Gr * Pr) < 10 ** 10:
            Nu_up = 0.14 * (Gr * Pr) ** (1 / 3)
        else:
            Nu_up = 0.54 * (Gr * Pr) ** (1 / 4)
        if 10 ** 5 < (Gr * Pr) < 10 ** 16:
            Nu_low = 2 + 0.13 * (Gr * Pr) ** (1 / 4)
        else:
            Nu_low = 2 + 0.13 * (Gr * Pr) ** (1 / 4)
        Nu = Nu_low + Nu_up
        print(f'Nusselts Number: {Nu}')
        h = Nu * k / Lc
        print(f'HT coefficient of Convection: {h}')
        b = float(input('Breadth of Fin: '))
        t = float(input('Thickness of Fin: '))
        P = 2 * (b + t)
        A = b * t
        fin_type = input("Convective Off End Fin(C) or Insulated Tip Fin(I): ").lower()
        m = math.sqrt(h * P / k / A)

        if fin_type == 'c':
            print('Convective Off End Fin')
            q = math.sqrt(h * P * k * A) * dT * (math.tanh(m * Lc) + (h / (m * k))) / (
                    1 + (math.tanh(m * Lc) * (h / (m * k))))
            print(f'Rate of HT (q): {q}')
            # qmax = ((math.tanh(m * l) + (h / (m * k))) / (
            #         1 + (math.tanh(m * l) * (h / (m * k))))) / (m * l)
            # neff = q / (qmax)
            # print(f'Efficiency of fin is {neff}')
            # E = q / (h * A * dT)
            # print(f'Effectiveness of fin is {E}')


        elif fin_type == 'i':
            q = math.sqrt(h * P * k * A) * dT * math.tanh(m * Lc)
            print(f'Rate of HT (q): {q}')
            # qmax = math.tanh(m * l) / (m * l)
            # neff = q / (qmax)
            # print(f'Efficiency of fin is {neff}')
            # E = q / (h * A * dT)
            # print(f'Effectiveness of fin is {E}')

        else:
            print('oops plz choose appropriate type of fin')

    def forced_conv():
        print('FORCED CONVECTION')
        Uinf = float(input('Flow velocity of fluid: '))
        try:
            v = float(input('Kinematic Viscosity (x10^-5): '))
            v = v / 100000
            roh = float(input('Density: '))
            mu = v * roh
        except:
            mu = float(input('Dynamic Viscosity(x10^-5): '))
            mu = mu / 100000
            roh = float(input('Density: '))
            v = mu / roh
        Re = Uinf * Lc / v
        print(f'Reynolds Number: {Re}')
        Pr = mu * cp / k
        print(f'Prandtls Number: {Pr}')
        if Re < 300000:
            print('LAMINAR FLOW')
            Nu = 0.664 * (Re ** (1 / 2)) * (Pr ** (1 / 3))
        else:
            print('TURBULENT FLOW')
            Nu = 0.366 * (Re ** (4 / 5)) * (Pr ** (1 / 3))
        print(f'Nusselts Number: {Nu}')
        h = 2 * Nu * k / Lc
        print(f'HT coefficient of Convection: {h}')

        b = float(input('Breadth of Fin: '))
        t = float(input('Thickness of Fin: '))
        P = 2 * (b + t)
        A = b * t
        fin_type = input("Convective Off End Fin(C) or Insulated Tip Fin(I): ").lower()
        m = math.sqrt(h * P / k / A)

        if fin_type == 'c':
            print('Convective Off End Fin')
            q = math.sqrt(h * P * k * A) * dT * (math.tanh(m * Lc) + (h / (m * k))) / (
                    1 + (math.tanh(m * Lc) * (h / (m * k))))
            print(f'Rate of HT (q): {q}')
            # qmax = ((math.tanh(m * l) + (h / (m * k))) / (
            #         1 + (math.tanh(m * l) * (h / (m * k))))) / (m * l)
            # neff = q / (qmax)
            # print(f'Efficiency of fin is {neff}')
            # E = q / (h * A * dT)
            # print(f'Effectiveness of fin is {E}')

        elif fin_type == 'i':
            q = math.sqrt(h * P * k * A) * dT * math.tanh(m * Lc)
            print(f'Rate of HT (q): {q}')
            # qmax = math.tanh(m * l) / (m * l)
            # neff = q / (qmax)
            # print(f'Efficiency of fin is {neff}')
            # E = q / (h * A * dT)
            # print(f'Effectiveness of fin is {E}')

        else:
            print('oops plz choose appropriate type of fin')

    if F_or_N == 'f':
        forced_conv()
    elif F_or_N == 'n':
        natural_conv()
    else:
        print('oops!')


def cir_cs():
    # for horizontal cylinder
    d = float(input('Diameter of Fin (m): '))
    k = float(input('Thermal Conductivity for Fin (W/mK): '))
    cp = float(input('Sp. Heat Capacity (J/kgK): '))
    Ts = float(input('Base Temperature: '))
    Tinf = float(input('Surrounding Temperature: '))
    Tm = (Ts + Tinf) / 2
    dT = Ts - Tinf
    l = float(input("Length of Fin (m): "))
    F_or_N = input('Forced or Natural Convection (F/N): ').lower()

    def forced_conv():
        # FORCED CONVECTION
        Uinf = float(input('Flow velocity of fluid (m/s): '))
        try:
            v = float(input('Kinematic Viscosity (x10^-5): '))
            v = v / 100000
            roh = float(input('Density: '))
            mu = v * roh
        except:
            mu = float(input('Dynamic Viscosity (x10^-5): '))
            mu = mu / 100000
            roh = float(input('Density: '))
            v = mu / roh
        Re = Uinf * d / v
        print(f'Reynolds Number: {Re}')
        if 0.4 < Re < 4:
            c = 0.989
            n = 0.330
        elif 4 < Re < 40:
            c = 0.911
            n = 0.385
        elif 40 < Re < 4000:
            c = 0.683
            n = 0.466
        elif 4000 < Re < 40000:
            c = 0.193
            n = 0.618
        elif 40000 < Re < 400000:
            c = 0.27
            n = 0.805
        else:
            c = 0.5
            n = 0.5
        Pr = mu * cp / k
        print(f'Prandtls Number: {Pr}')
        h = k / d * c * Re ** n * Pr ** 1 / 3
        print(f'Convective Co eff for HT (h): {h}')
        P = math.pi * d
        A = math.pi * d ** 2 / 4
        fin_type = input("Convective Off End Fin(C) or Insulated Tip Fin(I): ").lower()
        m = math.sqrt(h * P / k / A)

        if fin_type == 'c':
            print('Convective Off End Fin')
            q = math.sqrt(h * P * k * A) * dT * (math.tanh(m * l) + (h / (m * k))) / (
                    1 + (math.tanh(m * l) * (h / (m * k))))
            print(f'Rate of HT (q): {q}')
            # qmax = ((math.tanh(m * l) + (h / (m * k))) / (
            #         1 + (math.tanh(m * l) * (h / (m * k))))) / (m * l)
            # neff = q / (qmax)
            # print(f'Efficiency of fin is {neff}')
            # E = q / (h * A * dT)
            # print(f'Effectiveness of fin is {E}')

        elif fin_type == 'i':
            q = math.sqrt(h * P * k * A) * dT * math.tanh(m * l)
            print(f'Rate of HT (q): {q}')
            # qmax = math.tanh(m * l) / (m * l)
            # neff = q / (qmax)
            # print(f'Efficiency of fin is {neff}')
            # E = q / (h * A * dT)
            # print(f'Effectiveness of fin is {E}')

        else:
            print('oops plz choose appropriate type of fin')

    def natural_conv():
        # NATURAL CONVECTION
        g = 9.81
        B = float(input('Coefficient of Thermal Expansion (x10^-6): '))
        B = B / 1000000
        # viscosity
        try:
            v = float(input('Kinematic Viscosity (x10^-5): '))
            v = v / 100000
            roh = float(input('Density: '))
            mu = v * roh
        except:
            mu = float(input('Dynamic Viscosity(x10^-5): '))
            mu = mu / 100000
            roh = float(input('Density: '))
            v = mu / roh
        Gr = (g * B * dT) * d ** 3 / v ** 2
        Pr = mu * cp / k
        print(f'Prandtls Number: {Pr}')
        if 10 ** 4 < (Gr * Pr) < 10 ** 8:
            Nu = 0.53 * (Gr * Pr) ** (1 / 4)
        elif 10 ** 8 < (Gr * Pr) < 10 ** 12:
            Nu = 0.13 * (Gr * Pr) ** (1 / 3)
        else:
            print('oops!')
            Nu = 50
        h = Nu * k / d
        print(f'HT coefficient of Convection: {h}')

        P = math.pi * d
        A = math.pi * d ** 2 / 4
        fin_type = input("Convective Off End Fin(C) or Insulated Tip Fin(I): ").lower()
        m = math.sqrt(h * P / k / A)

        if fin_type == 'c':
            print('Convective Off End Fin')
            q = math.sqrt(h * P * k * A) * dT * (math.tanh(m * l) + (h / (m * k))) / (
                    1 + (math.tanh(m * l) * (h / (m * k))))
            print(f'Rate of HT (q): {q}')
            # qmax = ((math.tanh(m * l) + (h / (m * k))) / (
            #         1 + (math.tanh(m * l) * (h / (m * k))))) / (m * l)
            # neff = q / (qmax)
            # print(f'Efficiency of fin is {neff}')
            # E = q / (h * A * dT)
            # print(f'Effectiveness of fin is {E}')

        elif fin_type == 'i':
            q = math.sqrt(h * P * k * A) * dT * math.tanh(m * l)
            print(f'Rate of HT (q): {q}')
            # qmax = math.tanh(m * l) / (m * l)
            # neff = q / (qmax)
            # print(f'Efficiency of fin is {neff}')
            # E = q / (h * A * dT)
            # print(f'Effectiveness of fin is {E}')

        else:
            print('oops plz choose appropriate type of fin')

    if F_or_N == 'f':
        forced_conv()
    elif F_or_N == 'n':
        natural_conv()
    else:
        print('oops!')


call = input('Select the cross section of Fin - Circular or Rectangular [C or R]: ').lower()

if call == 'c':
    cir_cs()

elif call == 'r':
    rect_cs()
