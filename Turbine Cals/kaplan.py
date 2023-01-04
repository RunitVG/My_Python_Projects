import math
def kaplan():
    g = 9.81
    roh = 1000
    H = float(input('Net Head: '))
    N = float(input('Speed: '))
    fr = float(input('Flow Ratio: '))
    sp = float(input("Shaft Power (in kW): "))

    Do = float(input('Diameter at outlet: '))
    Db = float(input('Diameter of Hub: '))

    A = math.pi * (Do**2 - Db**2) / 4
    print(f'Area of Flow: {A}m2')

    vf1 = fr * math.sqrt(2 * g * H)
    print(f'Flow Velocity: {vf1}m/s')

    u = math.pi * Do * N / 60

    phi = math.degrees(math.atan(vf1 / u))
    print(f'Outlet Vane Angle: {phi}')

    Q = A * vf1
    print(f'Discharge: {Q}m3/s')

    no = sp * 100000/ (roh * g * Q * H)
    print(f'Overall Efficiency: {no}%')

    Ns = N * math.sqrt(sp) / H**(5/4)
    print(f'Specific Speed: {Ns}rmp')

