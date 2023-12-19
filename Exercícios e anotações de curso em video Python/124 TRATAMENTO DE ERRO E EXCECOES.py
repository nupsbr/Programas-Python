try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'Infelizmente tivemos um problema {erro.__class__}') 
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Voce conseguiu. Volte sempre! ')
    
    
#----------------------------------------------------------

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que voce digitou.')
except ZeroDivisionError:
    print('Não é possivel dividir um numero por zero!')
except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro entrado foi {erro.__cause__}')   
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Voce conseguiu. Volte sempre! ')
    