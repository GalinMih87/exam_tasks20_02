from math import floor, ceil

broi_dni = int(input())
hrana = int(input())
e1 = float(input())
e2 = float(input())
e3 = float(input())

hrana1 = broi_dni * e1
hrana2 = broi_dni * e2
hrana3 = broi_dni * e3

total_hrana = hrana1 + hrana2 + hrana3

diff = abs(hrana - total_hrana)

if hrana >= total_hrana:
    print(f"{floor(diff)} kilos of food left.")
else:
    print(f"{ceil(diff)} more kilos of food are needed.")