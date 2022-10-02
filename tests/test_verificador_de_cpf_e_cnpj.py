from asyncio import run

from verificador_de_cpf_e_cnpj import __version__
from verificador_de_cpf_e_cnpj.verificadores import CNPJ, CPF


def test_version():
    assert __version__ == '0.1.0'


def test_cpf_valido():
    assert run(CPF('356.914.610-36'))


def test_cpf_invalido():
    assert not run(CPF('356.964.610-36'))


def test_cnpj_valido():
    assert run(CNPJ('94.885.494/0001-82'))


def test_cnpj_invalido():
    assert not run(CNPJ('94.885.494/0401-82'))
