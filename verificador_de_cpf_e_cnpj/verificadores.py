"""Módulo dos verificadores"""


async def CNPJ(CNPJ: str = '00.000.000/0000-00') -> bool:
    """CNPJ.

    Nesta função fazemos a verificação do CNPJ passado.

    Args:
        CNPJ (str): CNPJ para a verificação.

    Returns:
        bool: Retornarmos se é verdadeiro ou falso.
    """
    cnpj = [int(char) for char in CNPJ if char.isdigit()]
    CNPJ = cnpj[:12]
    prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    while len(CNPJ) < 14:
        valor = sum([x * y for (x, y) in zip(CNPJ, prod)]) % 11
        if valor > 1:
            resto = 11 - valor
        else:
            resto = 0
        CNPJ.append(resto)
        prod.insert(0, 6)
    if CNPJ == cnpj:
        return True
    return False


async def CPF(CPF: str = '000.000.000-00') -> bool:
    """CPF.

    Nesta função fazemos a verificação do CPF passado.

    Args:
        CPF (str): CPF para a verificação.

    Returns:
        bool: Retornarmos se é verdadeiro ou falso.
    """
    cpf = [int(char) for char in CPF if char.isdigit()]
    if len(cpf) != 11 or cpf == cpf[::-1]:
        return False
    for index in range(9, 11):
        valor = sum(
            (cpf[num] * ((index + 1) - num) for num in range(0, index))
        )
        digito = ((valor * 10) % 11) % 10
        if digito != cpf[index]:
            return False
    return True
