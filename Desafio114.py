'''from urllib import request

print(f"\033[;1m{'Desafio 114 - Status de um link':*^70}\033[m")
endereco = dict()

try:
    response = request.urlopen('https://viacep.com.br/')
except Exception:
    print(f"O site não está acessível")
else:
    print("O site está online")
'''

import endereco

local = endereco.endereco(29836693)
for t,v in local.items():
      print(f"{t} : {v}")
print(local)
