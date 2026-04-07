salFix = float((input('Digite o salario fixo: ')))
vendas = float(input('Digite o valor das vendas: '))
diferenca = 0


if vendas <= 15000:
    salFix = (vendas * 1.03) + salFix
if vendas > 1500:
    salFix = (vendas * 1.03) + salFix
    diferenca = (vendas - 1500) * 1.05
    salFix = salFix + diferenca

print(round(salFix, 2))



