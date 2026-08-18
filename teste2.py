import pandas as pd
df = pd.read_csv(r'C:\Users\Thiago\OneDrive\Desktop\teiu\pokemon_projeto\Pokemon.csv')

#Quantos Pokémon são do tipo "Grass"?
grama = df[df['Type1'] == 'Grass']
print(f"EXISTE QUANTOS TIPOS PLANTAS : {len(grama)}")

#qual a média do atributo "Defense" entre todos os Pokémon?
defensa_media  = df['Defense'].mean()
print(f"A DEFENSA FISICA MÉDIA É {defensa_media:.2f}")

#Liste os 5 Pokémon com o menor "HP".
menos_resistene = df.nsmallest(5,'Defense')
print(menos_resistene[['Name','Type1','Type2','Defense','Generation']])

#Quantos Pokémon possuem "Speed" maior que 100?
mais_rapidos = df[df['Speed'] > 100]
print(f"QUANTOS POKEMOSN SÃO RAPIDOS : {len(mais_rapidos)}")

#Qual o Pokémon com o maior "Sp. Atk"?
maior_SpAtk = df[df['Sp. Atk'] == df['Sp. Atk'].max()]
print(f"QUAL POKEMON QUE TER MAIS ATAQUE ESPECIAL : {maior_SpAtk[['Name','Type1','Type2','Defense','Generation']]}")

#Agrupe por geração e mostre a média de "Attack"
geração_ataque = df.groupby('Generation')['Attack'].mean()
print("A MÉDIA DE ATAQUES DE CADA GERAÇÃO:")
print(geração_ataque)

#Filtre os Pokémon que são do tipo "Water" e têm "Total" acima de 500
aquaticos_fortes = df[(df['Type1'] == 'Water')   &   (df['Total'] > 500)]
print(aquaticos_fortes)

#Quantos Pokémon têm "Type1" igual a "Fire" e "Type2" igual a "Flying"?
fogo_voador = df[(df['Type1'] == 'Fire') & (df['Type2'] == 'Flying')]
print(f"EXISTEM QUANTOS POKEMONS DE TIPO FOGO E VOADOR SÃO : {len(fogo_voador)}")

#Quais são os 3 Pokémon com a maior "Defense"?
mais_resistente = df.nlargest(3,'Defense')
print(mais_resistente[['Name','Type1','Type2','Defense','Generation']])


#Crie uma coluna chamada "poderoso" que diga "Sim" se o Total for maior que 500 e "Não" caso contrário
def poderoso(Total):
    if Total > 500:
        return "SIm"
    else:
        return "Não"
df['poderoso'] = df['Total'].apply(poderoso)

print(df.head())