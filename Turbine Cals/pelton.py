import math
def pelton():
    g = 9.81
    roh = 1000
    try:
        H = float(input('Net Head: '))
    except:
        hg = float(input('Gross Head: '))
        try:
            hf = float(input('Head loss due to friction: '))
        except:
            f = float(input('Friction factor: '))
            D = float(input('Diameter of Penstock: '))
            L = float(input('Length of Penstock: '))
            V = float(input('Velocity of flow in Penstock: '))
            hf = (2 * f * L * V ** 2) / (g * D)
        H = hg - hf
    u = float(input('Bucket Velocity: '))
    delta = float(input('Angle of Deflection: '))
    cv = float(input('Coefficient of Velocity: '))
    v1 = cv * math.sqrt(2 * g * H)
    d = float(input('Diameter of Jet:'))
    A = math.pi * d ** 2 / 4
    q = A * v1
    phi = (180 - delta) * math.pi / 180
    print(f'Outlet Vane Angle: {phi}')

    vw1 = v1
    k = float(input('friction '))
    vr2 = k * v1
    vw2 = vr2 * math.cos(phi) - u

    print(f'Whirl velocity at Inlet: {vw1}')
    print(f'Whirl velocity at Outlet: {vw2}')

    wd_per_s = (roh * A * v1) * (vw1 + vw2) * u
    ke_per_s = roh * A * v1 ** 3 / 2
    wat_p = roh * g * q * H
    sp = int(input('Shaft Power: '))
    nhy = wd_per_s / ke_per_s
    nmech = sp / wd_per_s
    nov = nmech * nhy

    print(f'Work Done: {wd_per_s}')
    print(f'Hydraulic Efficiency: {nhy}')
    print(f'Mechanical Efficiency: {nmech}')
    print(f'Overall Efficiency: {nov}')

    rpm = int(input('rpm: '))
    D = 60 * u / math.pi / rpm
    m = D / d
    z = 15.0 + 0.5 * m

    print(f'No of buckets: {z}')
    print(f'Jet Ratio: {m}')
