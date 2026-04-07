num = int(input('Insira um numero: '))
soma = 0


while num != -1:
    
    if num < 21 or num > 70:
        num = int(input('Insira um valor entre 21 e 70: '))
    elif num >= 21 and num <= 70:
        print('chegou aqui')
        num = int(input('Insira outro numero: '))
        soma = soma + num
    
    
        
    soma = soma + num
