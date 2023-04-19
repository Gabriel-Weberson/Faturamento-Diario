import pandas as pd

# Para que o código funcione corretamente é necessário ter os arquivos "dados.json" e o "FaturamentoDiario.py" precisam estar na mesma pasta
tabela = pd.read_json("dados.json")
df_diasFaturados = tabela[tabela['valor'] != 0]
piorDia = tabela['valor'].min()
piorDiaFaturado = df_diasFaturados['valor'].min()
melhorDia = tabela['valor'].max()
mediaMensal = df_diasFaturados['valor'].mean()
melhoresDias = len(df_diasFaturados[df_diasFaturados['valor'] > mediaMensal])

print(f'O menor valor de faturamento foi de R$ {piorDia}')
print(f'O menor valor de faturamento (ACIMA DE 0) foi de R$ {piorDiaFaturado}')
print(f'O melhor valor de faturamento foi de R$ {melhorDia}')
print(f'Houveram {melhoresDias} dias com o valor de faturamento acima da media')
