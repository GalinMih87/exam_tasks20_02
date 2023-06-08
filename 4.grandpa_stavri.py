broi_dni = int(input())
sum_rakia = 0
sum_gradus = 0

for i in range (1, broi_dni + 1):
    rakia = float(input())
    sum_rakia += rakia
    gradus = float(input())
    sum_gradus += rakia * gradus

sredno = sum_gradus / sum_rakia

print(f"Liter: {sum_rakia:.2f}")
print(f"Degrees: {sredno:.2f}")

if sredno < 38:
    print(f"Not good, you should baking!")
elif 38 <= sredno <= 42:
    print(f"Super!")
else:
    print("Dilution with distilled water!")



