dia = int(input('Digite o dia de seu aniversário: '))
mes = int(input('Digite o mês de seu aniversário: '))
m = ''
s = ''
passou = "Passou"

if mes == 1:
    diff_dias = 31 + 28 + 31 - dia + 1 # março + fev + janeiro
    if diff_dias > 1:
        passou = "Passaram"
        s = 's'
    print(f'{passou} {diff_dias} dia{s} do seu aniversário!')
elif mes == 2:
    diff_dias = 31 + 28 - dia + 1
    if diff_dias > 1:
        passou = "Passaram"
        s = 's'
    print(f'{passou} {diff_dias} dia{s} do seu aniversário!')
elif mes == 3:
    diff_dias = 31 - dia + 1
    if diff_dias > 1:
        passou = "Passaram"
        s = 's'
    print(f'{passou} {diff_dias} dia{s} do seu aniversário!')
elif mes == 4:
    diff_dias = dia - 1
    if diff_dias == 0:
        print('Feliz aniversário!')
    else:
        if diff_dias > 1:
            m = 'm'
            s = 's'
        print(f"Falta{m} {diff_dias} dia{s} para seu aniversário.")
elif mes == 5:
    diff_dias = 29 + dia #abril + maio
    print(f"Faltam {diff_dias} dias para seu aniversário.")
elif mes == 6:
    diff_dias = 29 + 31 + dia #abril + maio + junho
    print(f"Faltam {diff_dias} dias para seu aniversário.")
elif mes == 7:
    diff_dias = 29 + 31 + 30 + dia #abril + maio + junho + junho...
    print(f"Faltam {diff_dias} dias para seu aniversário.")
elif mes == 8:
    diff_dias = 29 + 31 + 30 + 31 + dia #abril + maio + junho + junho...
    print(f"Faltam {diff_dias} dias para seu aniversário.")
elif mes == 9:
    diff_dias = 29 + 31 + 30 + 31 + 31 + dia #abril + maio + junho + junho...
    print(f"Faltam {diff_dias} dias para seu aniversário.")
elif mes == 10:
    diff_dias = 29 + 31 + 30 + 31 + 31 + 30 + dia #abril + maio + junho + junho...
    print(f"Faltam {diff_dias} dias para seu aniversário.")
elif mes == 11:
    diff_dias = 29 + 31 + 30 + 31 + 31 + 30 + 31 + dia #abril + maio + junho + junho...
    print(f"Faltam {diff_dias} dias para seu aniversário.")
elif mes == 12:
    diff_dias = 29 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + dia #abril + maio + junho + junho...
    print(f"Faltam {diff_dias} dias para seu aniversário.")
else:
    print("Mês inválido!")