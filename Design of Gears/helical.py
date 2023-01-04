def helical():
    import math

    material_of_gear = input('material of gear: ').lower()
    material_of_pinion = input('material of pinion: ').lower()

    if material_of_gear == material_of_pinion:
        sut = int(input('Sut for pinion and gear: '))
        sutp = sut
        sutg = sut
    else:
        sutp = int(input('Sut for pinion: '))
        sutg = int(input('Sut for gear: '))

    psi = float(input('helix angle: '))
    psi = math.radians(psi)
    zp = int(input('no of teeth on pinion: '))
    try:
        i = float(input('gear ratio:  '))
        zg = zp * i
        print(f'no of teeth on gear: {zg}')
    except:
        zg = int(input('no of teeth on gear: '))
        i = zg / zp
        print(f'gear ratio: {i}')

    b = int(input('b/mn: '))
    kw = float(input('power: '))
    np = int(input('rpm of pinion: '))
    cs = float(input('service factor: '))
    fos = float(input('factor of safety: '))
    bhn = int(input('BHN: '))

    zph = zp / math.cos(psi) ** 3
    zgh = zg / math.cos(psi) ** 3
    dp = zp / math.cos(psi)
    dg = zg / math.cos(psi)
    ng = np / i
    yp = 0.484 - 2.87 / zph
    yg = 0.484 - 2.87 / zgh

    # if u make a gui put check boxes for bending or wear failure...
    # if both checked ask for both, if one checked just ask inputs for 1...

    def pinion_is_weaker():
        # checking for k
        if material_of_pinion == 'st' and material_of_gear == 'st':
            kfact = 0.16
        elif material_of_pinion == 'ci' and material_of_gear == 'ci':
            kfact = 0.21
        else:
            kfact = 0.18

        k = kfact * (bhn / 100) ** 2
        q = 2 * zg / (zp + zg)
        # check for beam strength
        bst = b * sutp * yp / 3
        # check for wear strength
        wst = b * q * k * zp / math.cos(psi) ** 2
        v = math.pi * zp * np / 60000
        if v > 20:
            a = 5.6
            gamma = 1 / 2
        else:
            gamma = 1
            if v <= 10:
                a = 3
            else:
                a = 6
        print('v')
        print(v)

        if bst > wst:
            print('considering pitting failure')

            alpha = (a * b * q * zp * k * np * math.pi * zp) / (60000000 * cs * fos * kw)
            bravo = 0
            charlie = -v
            delta = -a
            p = -bravo / (3 * alpha)
            q = p ** 3 + (bravo * charlie - 3 * alpha * delta) / (6 * alpha ** 2)
            r = charlie / (3 * alpha)

            m = (q + (q ** 2 + (r - p * p) ** 3) ** (1 / 2)) ** (1 / 3) + (
                        q - (q * q + (r - p * p) ** 3) ** (1 / 2)) ** (
                        1 / 3) + p
            print(f'module = {m}')
            m = math.ceil(m)
            print(f'module = {m}')

            # cals for dynamic loading
            phip = m * 0.25 * math.sqrt(m * zp)
            phig = m * 0.25 * math.sqrt(m * zg)

            G = int(input('Grade: '))

            if G == 1:
                ep = 0.8 + 0.06 * phip
                eg = 0.8 + 0.06 * phig
                e = ep + eg
            elif G == 2:
                ep = 1.25 + 0.1 * phip
                eg = 1.25 + 0.1 * phig
                e = ep + eg
            elif G == 3:
                ep = 2 + 0.16 * phip
                eg = 2 + 0.16 * phig
                e = ep + eg
            elif G == 4:
                ep = 3.2 + 0.25 * phip
                eg = 3.2 + 0.25 * phig
                e = ep + eg
            elif G == 5:
                ep = 5 + 0.4 * phip
                eg = 5 + 0.4 * phig
                e = ep + eg
            elif G == 6:
                ep = 8 + 0.63 * phip
                eg = 8 + 0.63 * phig
                e = ep + eg
            elif G == 7:
                ep = 11 + 0.9 * phip
                eg = 11 + 0.9 * phig
                e = ep + eg
            elif G == 8:
                ep = 16 + 1.25 * phip
                eg = 16 + 1.25 * phig
                e = ep + eg
            elif G == 9:
                ep = 22 + 1.8 * phip
                eg = 22 + 1.8 * phig
                e = ep + eg
            elif G == 10:
                ep = 32 + 2.5 * phip
                eg = 32 + 2.5 * phig
                e = ep + eg
            elif G == 11:
                ep = 45 + 3.55 * phip
                eg = 45 + 3.55 * phig
                e = ep + eg
            elif G == 12:
                ep = 63 + 5 * phip
                eg = 63 + 5 * phig
                e = ep + eg
            else:
                print('oops plz select proper grade')
            e = e / 1000
            print(f'error = {e}')

            c = int(input('load deformation factor: '))

            fs = 0
            while fs < fos:
                v = v * m
                pt = kw * 1000 / v
                pd = (21 * v * (c * e * b * math.cos(psi) ** 2 + pt) * math.cos(psi)) / (
                            21 * v + math.sqrt(c * e * b * math.cos(psi) ** 2 + pt))
                ptmax = cs * pt
                peff = ptmax + pd
                fs = (wst * m ** 2) / peff
                m += 1
            print(f'm = {m}')
            print(f'new fos = {fs}')

        else:
            print('considering bending failure')

            alpha = (a * b * yp * sutp * math.pi * zp * np) / (180000000 * cs * kw * fos)
            bravo = 0
            charlie = -v
            delta = -a
            p = -bravo / (3 * alpha)
            q = p ** 3 + (bravo * charlie - 3 * alpha * delta) / (6 * alpha ** 2)
            r = charlie / (3 * alpha)

            m = (q + (q ** 2 + (r - p * p) ** 3) ** (1 / 2)) ** (1 / 3) + (
                        q - (q * q + (r - p * p) ** 3) ** (1 / 2)) ** (
                        1 / 3) + p
            print(f'module = {m}')
            m = math.ceil(m)
            print(f'module = {m}')

            # cals for dynamic loading
            phip = m * 0.25 * math.sqrt(m * zp)
            phig = m * 0.25 * math.sqrt(m * zg)

            G = int(input('Grade: '))

            if G == 1:
                ep = 0.8 + 0.06 * phip
                eg = 0.8 + 0.06 * phig
                e = ep + eg
            elif G == 2:
                ep = 1.25 + 0.1 * phip
                eg = 1.25 + 0.1 * phig
                e = ep + eg
            elif G == 3:
                ep = 2 + 0.16 * phip
                eg = 2 + 0.16 * phig
                e = ep + eg
            elif G == 4:
                ep = 3.2 + 0.25 * phip
                eg = 3.2 + 0.25 * phig
                e = ep + eg
            elif G == 5:
                ep = 5 + 0.4 * phip
                eg = 5 + 0.4 * phig
                e = ep + eg
            elif G == 6:
                ep = 8 + 0.63 * phip
                eg = 8 + 0.63 * phig
                e = ep + eg
            elif G == 7:
                ep = 11 + 0.9 * phip
                eg = 11 + 0.9 * phig
                e = ep + eg
            elif G == 8:
                ep = 16 + 1.25 * phip
                eg = 16 + 1.25 * phig
                e = ep + eg
            elif G == 9:
                ep = 22 + 1.8 * phip
                eg = 22 + 1.8 * phig
                e = ep + eg
            elif G == 10:
                ep = 32 + 2.5 * phip
                eg = 32 + 2.5 * phig
                e = ep + eg
            elif G == 11:
                ep = 45 + 3.55 * phip
                eg = 45 + 3.55 * phig
                e = ep + eg
            elif G == 12:
                ep = 63 + 5 * phip
                eg = 63 + 5 * phig
                e = ep + eg
            else:
                print('oops plz select proper grade')
            e = e / 1000
            print(f'error = {e}')

            c = int(input('load deformation factor: '))

            fs = 0
            while fs < fos:
                v = v * m
                pt = kw * 1000 / v
                pd = (21 * v * (c * e * b * math.cos(psi) ** 2 + pt) * math.cos(psi)) / (
                            21 * v + math.sqrt(c * e * b * math.cos(psi) ** 2 + pt))
                ptmax = cs * pt
                peff = ptmax + pd
                fs = (bst * m ** 2) / peff
                m += 1
            print(f'm = {m}')
            print(f'new fos = {fs}')

    def gear_is_weaker():
        # checking for k
        if material_of_pinion == 'st' and material_of_gear == 'st':
            kfact = 0.16
        elif material_of_pinion == 'ci' and material_of_gear == 'ci':
            kfact = 0.21
        else:
            kfact = 0.18
        k = kfact * (bhn / 100) ** 2
        q = 2 * zg / (zp + zg)
        # check for beam strength
        bst = b * sutg * yg / 3
        # check for wear strength
        wst = b * q * k * zg / math.cos(psi) ** 2
        v = math.pi * zp * np / 60000
        if v > 20:
            a = 5.6
            gamma = 1 / 2
        else:
            gamma = 1
            if v <= 10:
                a = 3
            else:
                a = 6
        print('v')
        print(v)

        if bst > wst:
            print('considering pitting failure')
            alpha = (a * b * q * zp * k * np * math.pi * zp) / (60000000 * cs * fos * kw)
            bravo = 0
            charlie = -v
            delta = -a

            # print('abcd')
            # print(alpha)
            # print(bravo)
            # print(charlie)
            # print(delta)
            p = -bravo / (3 * alpha)
            q = p ** 3 + (bravo * charlie - 3 * alpha * delta) / (6 * alpha ** 2)
            r = charlie / (3 * alpha)
            # print('pqr')
            # print(p)
            # print(q)
            # print(r)
            m = (q + (q ** 2 + (r - p * p) ** 3) ** (1 / 2)) ** (1 / 3) + (
                        q - (q * q + (r - p * p) ** 3) ** (1 / 2)) ** (
                        1 / 3) + p
            print(f'module = {m}')
            m = math.ceil(m)
            print(f'module = {m}')

            # cals for dynamic loading
            # cals for dynamic loading
            phip = m * 0.25 * math.sqrt(m * zp)
            phig = m * 0.25 * math.sqrt(m * zg)

            G = int(input('Grade: '))

            if G == 1:
                ep = 0.8 + 0.06 * phip
                eg = 0.8 + 0.06 * phig
                e = ep + eg
            elif G == 2:
                ep = 1.25 + 0.1 * phip
                eg = 1.25 + 0.1 * phig
                e = ep + eg
            elif G == 3:
                ep = 2 + 0.16 * phip
                eg = 2 + 0.16 * phig
                e = ep + eg
            elif G == 4:
                ep = 3.2 + 0.25 * phip
                eg = 3.2 + 0.25 * phig
                e = ep + eg
            elif G == 5:
                ep = 5 + 0.4 * phip
                eg = 5 + 0.4 * phig
                e = ep + eg
            elif G == 6:
                ep = 8 + 0.63 * phip
                eg = 8 + 0.63 * phig
                e = ep + eg
            elif G == 7:
                ep = 11 + 0.9 * phip
                eg = 11 + 0.9 * phig
                e = ep + eg
            elif G == 8:
                ep = 16 + 1.25 * phip
                eg = 16 + 1.25 * phig
                e = ep + eg
            elif G == 9:
                ep = 22 + 1.8 * phip
                eg = 22 + 1.8 * phig
                e = ep + eg
            elif G == 10:
                ep = 32 + 2.5 * phip
                eg = 32 + 2.5 * phig
                e = ep + eg
            elif G == 11:
                ep = 45 + 3.55 * phip
                eg = 45 + 3.55 * phig
                e = ep + eg
            elif G == 12:
                ep = 63 + 5 * phip
                eg = 63 + 5 * phig
                e = ep + eg
            else:
                print('oops plz select proper grade')
            e = e / 1000
            print(f'error = {e}')
            c = int(input('load deformation factor: '))

            fs = 0
            while fs < fos:
                v = v * m
                pt = kw * 1000 / v
                pd = (21 * v * (c * e * b * math.cos(psi) ** 2 + pt) * math.cos(psi)) / (
                            21 * v + math.sqrt(c * e * b * math.cos(psi) ** 2 + pt))
                ptmax = cs * pt
                peff = ptmax + pd
                fs = (wst * m ** 2) / peff
                m += 1
            print(f'm = {m}')
            print(f'new fos = {fs}')

        else:
            print('considering bending failure')

            alpha = (a * b * yg * sutg * math.pi * zp * np) / (180000000 * cs * kw * fos)
            bravo = 0
            charlie = -v
            delta = -a

            # print('abcd')
            # print(alpha)
            # print(bravo)
            # print(charlie)
            # print(delta)
            p = -bravo / (3 * alpha)
            q = p ** 3 + (bravo * charlie - 3 * alpha * delta) / (6 * alpha ** 2)
            r = charlie / (3 * alpha)
            # print('pqr')
            # print(p)
            # print(q)
            # print(r)
            m = (q + (q ** 2 + (r - p * p) ** 3) ** (1 / 2)) ** (1 / 3) + (
                        q - (q * q + (r - p * p) ** 3) ** (1 / 2)) ** (
                        1 / 3) + p
            print(f'module = {m}')
            m = math.ceil(m)
            print(f'module = {m}')

            # cals for dynamic loading
            phip = m * 0.25 * math.sqrt(m * zp)
            phig = m * 0.25 * math.sqrt(m * zg)

            G = int(input('Grade: '))

            if G == 1:
                ep = 0.8 + 0.06 * phip
                eg = 0.8 + 0.06 * phig
                e = ep + eg
            elif G == 2:
                ep = 1.25 + 0.1 * phip
                eg = 1.25 + 0.1 * phig
                e = ep + eg
            elif G == 3:
                ep = 2 + 0.16 * phip
                eg = 2 + 0.16 * phig
                e = ep + eg
            elif G == 4:
                ep = 3.2 + 0.25 * phip
                eg = 3.2 + 0.25 * phig
                e = ep + eg
            elif G == 5:
                ep = 5 + 0.4 * phip
                eg = 5 + 0.4 * phig
                e = ep + eg
            elif G == 6:
                ep = 8 + 0.63 * phip
                eg = 8 + 0.63 * phig
                e = ep + eg
            elif G == 7:
                ep = 11 + 0.9 * phip
                eg = 11 + 0.9 * phig
                e = ep + eg
            elif G == 8:
                ep = 16 + 1.25 * phip
                eg = 16 + 1.25 * phig
                e = ep + eg
            elif G == 9:
                ep = 22 + 1.8 * phip
                eg = 22 + 1.8 * phig
                e = ep + eg
            elif G == 10:
                ep = 32 + 2.5 * phip
                eg = 32 + 2.5 * phig
                e = ep + eg
            elif G == 11:
                ep = 45 + 3.55 * phip
                eg = 45 + 3.55 * phig
                e = ep + eg
            elif G == 12:
                ep = 63 + 5 * phip
                eg = 63 + 5 * phig
                e = ep + eg
            else:
                print('oops plz select proper grade')
            e = e / 1000
            print(f'error = {e}')

            c = int(input('load deformation factor: '))

            fs = 0
            while fs < fos:
                v = v * m
                pt = kw * 1000 / v
                pd = (21 * v * (c * e * b * math.cos(psi) ** 2 + pt) * math.cos(psi)) / (
                            21 * v + math.sqrt(c * e * b * math.cos(psi) ** 2 + pt))
                ptmax = cs * pt
                peff = ptmax + pd
                fs = (bst * m ** 2) / peff
                m += 1
            print(f'm = {m}')
            print(f'new fos = {fs}')

    # don't check here
    if material_of_gear == material_of_pinion:
        print('pinion is weaker')
        pinion_is_weaker()
    else:
        # consider if gears are of different material
        stog = sutg * yg / 3
        stop = sutp * yp / 3
        if stop > stog:
            # gear is weaker
            gear_is_weaker()
        else:
            # pinion is weaker
            pinion_is_weaker()


