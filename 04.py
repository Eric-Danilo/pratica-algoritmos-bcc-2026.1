num = 0

while num <= 100:
    print('passando aqui limnha 4')
    if num != 7 and num != 13 and num != 21 and num != 50:
        print(num)
    else:
        print(f'o numero {num} pertence ao gp dos nums escolhidos')
    
    num = num + 1