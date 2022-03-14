#-----------------------
# FUNÇÕES
#-----------------------
def verificacaoDeCpf(numerosDoCpf:str = '000.000.000-00')->bool:
    cpf = [int(char) for char in numerosDoCpf if char.isdigit()];
    if len(cpf) != 11 or cpf == cpf[::-1]:
        return False;
    for i in range(9, 11):
        valor = sum((cpf[num] * ((i + 1) - num) for num in range(0, i)));
        digito = ((valor * 10) % 11) % 10;
        if digito != cpf[i]:
            return False;
    return True;
#-----------------------
# M A I N ()
#-----------------------
if __name__ == '__main__':
    CPFS = [];
    for cpf in CPFS:
        var = 'falso';
        if verificacaoDeCpf(cpf):
            var = 'verdadeiro';
        print("O CNPJ: "+cpf+" é "+var);
#-----------------------