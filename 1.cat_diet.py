procent_maznini = int(input())
procent_protein = int(input())
procent_vaglehidrati = int(input())
obshto_kalorii = int(input())
procent_voda = int(input())

gram_maznini = ((procent_maznini * obshto_kalorii) / 100) / 9
gram_proteini = ((procent_protein * obshto_kalorii) / 100) / 4
gram_vaglehidrati = ((procent_vaglehidrati * obshto_kalorii) /100) / 4

teglo = gram_proteini + gram_maznini + gram_vaglehidrati
kalorii = obshto_kalorii / teglo
procent = 100 - procent_voda

voda = (procent * kalorii) / 100

print(f"{voda:.4f}")