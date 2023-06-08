broi_hora = int(input())
sezon = input()
price = 0
if broi_hora <= 5:
    if sezon == "spring":
        price = broi_hora * 50.00
    if sezon == "summer":
        price = broi_hora * 48.50
    if sezon == "autumn":
        price = broi_hora * 60.00
    if sezon == "winter":
        price = broi_hora * 86.00
if broi_hora > 5:
    if sezon == "spring":
        price = broi_hora * 48.00
    if sezon == "summer":
        price = broi_hora * 45.00
    if sezon == "autumn":
        price = broi_hora * 49.50
    if sezon == "winter":
        price = broi_hora * 85.00
if sezon == "summer":
    price -= price * 0.15
if sezon == "winter":
    price += price * 0.08
print(f"{price:.2f} leva.")
