import math
def francis():
    g = 9.81
    H = float(input('Net Head: '))
    N = float(input('Speed: '))
    fr = float(input('Flow Ratio: '))
    sp = float(input("Shaft Power: "))

    d1 = float(input('Diameter at inlet: '))
    d2 = float(input('Diameter at outlet: '))

    u1 = math.pi * d1 * N / 60
    u2 = math.pi * d2 * N / 60

    vf1 = fr * math.sqrt(2 * g * H)
    print(f'Flow velocity at Inlet: {vf1}')
    phi = float(input('Outlet vane angle: '))
    theta = float(input('Inlet vane angle: '))
    rad_theta = theta * math.pi / 180
    rad_phi = phi * math.pi / 180
    vf2 = u2 * math.tan(rad_phi)
    print(f'Flow velocity at Outlet: {vf2}')
    vw1 = vf1 / math.tan(rad_theta) + u1
    print(f'Whirl velocity at Inlet: {vw1}')

    try:
        b1 = float(input('Width at inlet: '))
        Q = math.pi * b1 * d1 * vf1
    except:
        b2 = float(input('Width at outlet: '))
        Q = math.pi * b2 * d2 * vf2
    print(f'Discharge = {Q}')

    aof = Q / vf1
    print(f'area of flow = {aof}')

    wp = (H * g * Q)
    print(f'Water Power = {wp}')

    nh = vw1 * u1 / (g * H) * 100
    print(f'Hydraulic Efficiency: {nh}%')

    no = wp * 100 / sp
    print(f'Overall Efficiency: {no}%')
