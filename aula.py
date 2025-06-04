tempo= float(input("Digite o tempo em que os fundos foram mantidos em depósito: "))
dinheiro=float(input("Digite o valor depositado"))
if tempo >=5:
    taxa= 0.95
elif tempo <5 and tempo >=4:
    taxa=0.9
elif tempo <4 and tempo >=3:
    taxa=0.85
elif tempo <3 and tempo >=2:
    taxa=0.75
elif tempo <2 and tempo >=1:
    taxa=0.65
else:
    taxa=0.55
juros=dinheiro*(taxa/100)
total= dinheiro+ juros
print("A taxa de juros foi de {:.2f}%: " .format(taxa))
print("O valor do juros foi de:",juros)
print("O valor total após",tempo,"anos é:R$",total)



