nomes= ["Adriel","Amanda","Ana","Felipe","Fe Mayumi","Guilherme","Kim","Leticia","Marcelo","Maria","Mateus","Milena","Paulo","Theo","Vitor"]
import random 
grupo_FeMees= random.sample(nomes,4)
print(f'O grupo da Fernanda Mees é: {grupo_FeMees}')

for pessoas in grupo_FeMees:
    nomes.remove(pessoas)

grupo_Gabriel= random.sample(nomes,4)
print(f'O grupo do Gabriel é {grupo_Gabriel}')

for pessoas in grupo_Gabriel:
    nomes.remove(pessoas)

grupo_Andre= random.sample(nomes,4)
print(f'O grupo do André é {grupo_Andre}')

for pessoas in grupo_Andre:
    nomes.remove(pessoas)

grupo_Henrique= random.sample(nomes,3)
print(f'O grupo do Henrique é {grupo_Henrique}')



 