def spur():
    import math

    material_of_gear, sutg = map(str, input('material and Sut of gear: ').lower().split())
    material_of_pinion, sutp = map(str, input('material and Sut of pinion: ').lower().split())
    sutp = float(sutp)
    sutg = float(sutg)
    try:
        zp = int(input('no of teeth on pinion: '))
    except:
        zp = 18
        print(18)
    try:
        i = float(input('gear ratio:  '))
        zg = zp * i
        zg = math.ceil(zg)
        print(f'no of teeth on gear: {zg}')
    except:
        zg = int(input('no of teeth on gear: '))
        i = zg / zp
        print(f'gear ratio: {i}')
    b = int(input('b/m: '))
    np = int(input('rpm for pinon: '))
    kw = int(input('power: '))
    cs = float(input('service factor: '))
    fos = float(input('factor of safety: '))
    bhn = int(input('BHN: '))
    ng = np / i
    print(f'gear speed = {ng}')
    yp = 0.484 - 2.87 / zp
    yg = 0.484 - 2.87 / zg

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
        wst = b * q * k * zp
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
            G = int(input("Grade:"))

            phiP = m + 0.25 * (math.sqrt(m * zg))
            errorP = {1: (0.80 + 0.06 * phiP), 2: (1.25 + 0.10 * phiP), 3: (2.00 + 0, 16 * phiP),
                      4: (3.20 + 0.25 * phiP), 5: (5.00 + 0.40 * phiP), 6: (8.00 + 0.63 * phiP),
                      7: (11.00 + 0.90 * phiP), 8: (16.00 + 1.25 * phiP), 9: (22.00 + 1.80 * phiP),
                      10: (32.00 + 0.25 * phiP), 11: (45.00 + 3.55 * phiP), 12: (63.00 + 5.00 * phiP)}
            eg = errorP[G]

            phiG = m + 0.25 * (math.sqrt(m * zp))
            errorG = {1: (0.80 + 0.06 * phiG), 2: (1.25 + 0.10 * phiG), 3: (2.00 + 0, 16 * phiG),
                      4: (3.20 + 0.25 * phiG), 5: (5.00 + 0.40 * phiG), 6: (8.00 + 0.63 * phiG),
                      7: (11.00 + 0.90 * phiG), 8: (16.00 + 1.25 * phiG), 9: (22.00 + 1.80 * phiG),
                      10: (32.00 + 0.25 * phiG), 11: (45.00 + 3.55 * phiG), 12: (63.00 + 5.00 * phiG)}
            ep = errorG[G]

            e = (ep + eg) / 1000
            print(e)
            print(f'error = {e}')

            c = int(input('load deformation factor: '))

            fs = 0
            while fs < fos:
                v = v * m
                pt = kw * 1000 / v
                pd = (21 * v * (c * e * b + pt)) / (21 * v + math.sqrt(c * e * b + pt))
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
            G = int(input("Grade:"))

            phiP = m + 0.25 * (math.sqrt(m * zg))
            errorP = {1: (0.80 + 0.06 * phiP), 2: (1.25 + 0.10 * phiP), 3: (2.00 + 0, 16 * phiP),
                      4: (3.20 + 0.25 * phiP), 5: (5.00 + 0.40 * phiP), 6: (8.00 + 0.63 * phiP),
                      7: (11.00 + 0.90 * phiP), 8: (16.00 + 1.25 * phiP), 9: (22.00 + 1.80 * phiP),
                      10: (32.00 + 0.25 * phiP), 11: (45.00 + 3.55 * phiP), 12: (63.00 + 5.00 * phiP)}
            eg = errorP[G]

            phiG = m + 0.25 * (math.sqrt(m * zp))
            errorG = {1: (0.80 + 0.06 * phiG), 2: (1.25 + 0.10 * phiG), 3: (2.00 + 0, 16 * phiG),
                      4: (3.20 + 0.25 * phiG), 5: (5.00 + 0.40 * phiG), 6: (8.00 + 0.63 * phiG),
                      7: (11.00 + 0.90 * phiG), 8: (16.00 + 1.25 * phiG), 9: (22.00 + 1.80 * phiG),
                      10: (32.00 + 0.25 * phiG), 11: (45.00 + 3.55 * phiG), 12: (63.00 + 5.00 * phiG)}
            ep = errorG[G]

            e = (ep + eg) / 1000
            print(e)
            print(f'error = {e}')

            c = int(input('load deformation factor: '))

            fs = 0
            while fs < fos:
                v = v * m
                pt = kw * 1000 / v
                pd = (21 * v * (c * e * b + pt)) / (21 * v + math.sqrt(c * e * b + pt))
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
        wst = b * q * k * zg
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
            G = int(input("Grade:"))

            phiP = m + 0.25 * (math.sqrt(m * zg))
            errorP = {1: (0.80 + 0.06 * phiP), 2: (1.25 + 0.10 * phiP), 3: (2.00 + 0, 16 * phiP),
                      4: (3.20 + 0.25 * phiP), 5: (5.00 + 0.40 * phiP), 6: (8.00 + 0.63 * phiP),
                      7: (11.00 + 0.90 * phiP), 8: (16.00 + 1.25 * phiP), 9: (22.00 + 1.80 * phiP),
                      10: (32.00 + 0.25 * phiP), 11: (45.00 + 3.55 * phiP), 12: (63.00 + 5.00 * phiP)}
            eg = errorP[G]

            phiG = m + 0.25 * (math.sqrt(m * zp))
            errorG = {1: (0.80 + 0.06 * phiG), 2: (1.25 + 0.10 * phiG), 3: (2.00 + 0, 16 * phiG),
                      4: (3.20 + 0.25 * phiG), 5: (5.00 + 0.40 * phiG), 6: (8.00 + 0.63 * phiG),
                      7: (11.00 + 0.90 * phiG), 8: (16.00 + 1.25 * phiG), 9: (22.00 + 1.80 * phiG),
                      10: (32.00 + 0.25 * phiG), 11: (45.00 + 3.55 * phiG), 12: (63.00 + 5.00 * phiG)}
            ep = errorG[G]

            e = (ep + eg) / 1000
            print(e)
            print(f'error = {e}')
            c = int(input('load deformation factor: '))

            fs = 0
            while fs < fos:
                v = v * m
                pt = kw * 1000 / v
                pd = (21 * v * (c * e * b + pt)) / (21 * v + math.sqrt(c * e * b + pt))
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
            G = int(input("Grade:"))

            phiP = m + 0.25 * (math.sqrt(m * zg))
            errorP = {1: (0.80 + 0.06 * phiP), 2: (1.25 + 0.10 * phiP), 3: (2.00 + 0, 16 * phiP),
                      4: (3.20 + 0.25 * phiP), 5: (5.00 + 0.40 * phiP), 6: (8.00 + 0.63 * phiP),
                      7: (11.00 + 0.90 * phiP), 8: (16.00 + 1.25 * phiP), 9: (22.00 + 1.80 * phiP),
                      10: (32.00 + 0.25 * phiP), 11: (45.00 + 3.55 * phiP), 12: (63.00 + 5.00 * phiP)}
            eg = errorP[G]

            phiG = m + 0.25 * (math.sqrt(m * zp))
            errorG = {1: (0.80 + 0.06 * phiG), 2: (1.25 + 0.10 * phiG), 3: (2.00 + 0, 16 * phiG),
                      4: (3.20 + 0.25 * phiG), 5: (5.00 + 0.40 * phiG), 6: (8.00 + 0.63 * phiG),
                      7: (11.00 + 0.90 * phiG), 8: (16.00 + 1.25 * phiG), 9: (22.00 + 1.80 * phiG),
                      10: (32.00 + 0.25 * phiG), 11: (45.00 + 3.55 * phiG), 12: (63.00 + 5.00 * phiG)}
            ep = errorG[G]

            e = (ep + eg) / 1000
            print(e)
            print(f'error = {e}')

            c = int(input('load deformation factor: '))

            fs = 0
            while fs < fos:
                v = v * m
                pt = kw * 1000 / v
                pd = (21 * v * (c * e * b + pt)) / (21 * v + math.sqrt(c * e * b + pt))
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
