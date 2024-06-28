import os
from pathlib import Path
# Especifique o caminho da pasta que você deseja percorrer
pasta = Path('datasets')
item = os.listdir(pasta)
print(f'{pasta}/{item[0]}')


# Use a função os.listdir() para obter uma lista de arquivos e subpastas na pasta


# caminho_completo = os.path.join(pasta, item)  # Combina o caminho da pasta com o nome do item

# 'print(caminho_completo)


# if os.path.isfile(caminho_completo):  # Verifica se é um arquivo (não uma subpasta)
#     pasta2 = pasta2 + caminho_completo
