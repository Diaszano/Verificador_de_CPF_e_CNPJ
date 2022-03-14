#-----------------------
# FUNÇÕES
#-----------------------
def verificacaoDeCnpj(cnpj:str = '00.000.000/0000-00')->bool:
    cnpjo = [int(char) for char in cnpj if char.isdigit()];
    cnpj = cnpjo[:12];
    prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2];
    
    while len(cnpj) < 14:
        valor = sum([x*y for (x, y) in zip(cnpj, prod)])%11;
        if valor > 1:
            resto = 11 - valor;
        else:
            resto = 0;
        cnpj.append(resto);
        prod.insert(0, 6);
    if cnpj == cnpjo:
        return True;
    return False;
#-----------------------
# M A I N ()
#-----------------------
if __name__ == '__main__':
    CNPJ = [];
    for cnpj in CNPJ:
        var = 'falso';
        if verificacaoDeCnpj(cnpj):
            var = 'verdadeiro';
        print("O CNPJ: "+cnpj+" é "+var);
#-----------------------