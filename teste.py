import pandas as pd
df = pd.read_csv(r'C:\Users\Thiago\OneDrive\Desktop\teiu\pokemon_projeto\Pokemon.csv')
#1)Quantos Pokémon existem no dataset?
print(f"EXISTEM QUANTOS POKEMONS NOS DADOS : {len(df)}")


#2)Qual é a média da coluna Attack?
media_ataque = df['Attack'].mean()
print(f"A MEDIA DE MOVIMENTO OFENSIVO É : {media_ataque:.2f}")

#3)Quais são os 5 Pokémon com maior Speed?
mais_rapido = df.nlargest(5,'Speed')
print(mais_rapido[['Name', 'Speed']])

#4)Quantos Pokémon são do tipo Fire?
tipo_fogo =df[df['Type1'] == 'Fire']
print(f"SÃO QUANTOS POKEMONS DO TIPO : {len(tipo_fogo)} ")

#5)Qual é o Pokémon com maior Total?
total_pontos = df[df['Total'] == df['Total'].max()]
print(total_pontos[['Name','Total']])

#6) Qual é a média de HP por geração (Generation)?
media_hp = df.groupby('Generation')['HP'].mean()
print(media_hp)

#7)Quantos Pokémon são do tipo Water e têm Attack maior que 100?
aquatico_forte = df[(df['Type1'] == 'Water') & ( df['Attack'] > 100) ]
print(aquatico_forte[['Name','Type1','Attack']])

#8)Quais são os 3 Pokémon com menor Defense?
mais_frageis = df.nsmallest(3,'Defense')
print(mais_frageis[['Name','Type1','Type2','Defense','Generation']])

#9)Qual é o desvio padrão da coluna Sp. Atk?
padrao_SpAtk = df['Sp. Atk'].std()
print(f"DESVIO PADRÃO DE SP. ATK: {padrao_SpAtk:.2f}")