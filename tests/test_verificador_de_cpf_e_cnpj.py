from verificadores import __version__
from verificadores.cnpj import CNPJ
from verificadores.cpf import CPF


def test_version():
    assert __version__ == '0.2.0'


def test_cpf_valido():
    assert CPF('356.914.610-36')


def test_cpf_invalido():
    assert not CPF('356.964.610-36')


def test_cnpj_valido():
    assert CNPJ('94.885.494/0001-82')


def test_cnpj_invalido():
    assert not CNPJ('94.885.494/0401-82')
