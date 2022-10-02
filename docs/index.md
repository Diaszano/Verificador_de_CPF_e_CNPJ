# 🐍 Rastreador de Encomendas

## Esse programa tem como seu intuito fazer a verificação de CPF e CNPJ.

## Como utilizar?

```shell
$ pip install pyVerificadorDocs
```

```Python
from asyncio import run

from pyVerificadorDocs import CPF, CNPJ


async def main():
    resultado = await CPF('000.000.000-00')
    print(f'CPF é {resultado}')
    resultado = await CNPJ('00.000.000/0000-00')
    print(f'CNPJ é {resultado}')


run(main())
```

### O que usamos na infraestrutura?

- [Utilizamos a linguagem Python](https://www.python.org/)
