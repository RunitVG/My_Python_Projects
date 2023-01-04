def bevel():
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


    m = float(input('module: '))
    zp = int(input('no of teeth on pinion: '))
    try:
        i = float(input('gear ratio:  '))
        zg = zp * i
        print(f'no of teeth on gear: {zg}')
    except:
        zg = int(input('no of teeth on gear: '))
        i = zg / zp
        print(f'gear ratio: {i}')

    dp = m * zp
    dg = m * zg

    b = int(input('b/mn: '))
    kw = float(input('power: '))
    np = int(input('rpm of pinion: '))
    cs = float(input('service factor: '))
    bhn = int(input('BHN: '))

    gam = math.atan(zp / zg)
    gam = math.degrees(gam)
    print(f'gamma: {gam}')

    Ao = math.sqrt((dp/2)**2+(dg/2)**2)

    y = 0.484 - 2.87 / zp

    sb = m * b * sutp * y * (1 - b / Ao)
    print(f'Bending Strength: {sb}')
    q = 2 * zg / (zg + zp * math.tan(gam))
    k = 0.16 * (bhn/100)**2
    sw = 0.75 * b * q * dp * k / math.cos(gam)
    print(f'Wearing Strength: {sw}')

    mt = 60 * 10**6 * kw / (2 * math.pi * np)
    print(f'Torque (Mt): {mt}')

    pt = 2 * mt / dp
    print(f'tangential force (Pt): {pt}')

    print('for dynamic loading')

    v = (math.pi * dp * np) / (60 * 1000)
    print(f'velocity: {v}')

    C = float(input('deformation factor: '))
    e = float(input('error: '))

    pd = (21 * v * (C * e * b + pt))/(21 * v + math.sqrt(C * e * b + pt))
    print(f'Dynamic Load: {pd}')

    peff = cs * pt + pd
    print(f'Effective Load: {peff}')

    fos_b = sb / peff
    fos_w = sw / peff
    print(f'Factor of safety against Bending Failure: {fos_b}')
    print(f'Factor of safety against Wearing Failure: {fos_w}')




