'''crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato br
A) os 5 primeiros
B) os ultimos 4 colocados
C) times em ordem alfabetica
D) em que posição esta o time da chapecoense'''
from time import sleep
am = '\033[1;33m'
vr = '\033[1;32m'
az = '\033[1;36m'
lp = '\033[m'
times = ("Flamengo", "Santos", "Palmeiras", "Gremio",
         "Atletico Paranaense", "São Paulo", "Internacional",
         "Conrithians", "Fortaleza", "Goias", "Bahia", "Vasco",
         "Atletico Mineiro", "Fluminense", "Botafogo", "Ceará",
         "Cruzeiro", "CSA", "Chapecoense", "Avaí")

print(f'{az}#{am}#{vr}#{lp}'*20)
print("{:^80}".format("\033[1;36mLISTA \033[1;33mCAMPEONATO \033[1;32mBRASILEIRO\033[m"))
print(f'{az}#{am}#{vr}#{lp}'*20)
sleep(2)
print('\n')
print(f'{az}Lista dos times do Brasileirao:{lp}')
for comida in times[::2]:
    print(f'{am}{comida}{lp}',end=' - ')
for comida in times[1::2]:
    print(f'{vr}{comida}{lp}',end=' - ')  
print('\n')
sleep(2)  
print(f'{az}#{am}#{vr}#{lp}'*40)
print('\n')
print(f'{az}5 {am}primeiros {vr}times:{lp}')
for comida in times[0:5]:
    print(f'{az}{comida}{lp}',end=' - ')
print('\n')
sleep(2) 
print(f'{az}#{am}#{vr}#{lp}'*40)
print('\n')
print(f'{az}4 {am}ultimos {vr}times:{lp}')
for comida in times[16:]:
    print(f'{az}{comida}{lp}',end=' - ')
print('\n')
sleep(2) 
print(f'{az}#{am}#{vr}#{lp}'*40)
print('\n')
print(f'{vr}Ordem Alfabetica:{lp}')
for comida in sorted(times):
    print(f'{az}{comida}{lp}',end=' - ')
print('\n')
sleep(2) 
print(f'{az}#{am}#{vr}#{lp}'*40)
print('\n')
sleep(2) 
print(f'{am}A posicao de chapecoense é {vr}{times.index("Chapecoense")+1}{am} posicao{lp}')
print('\n')
print(f'{az}#{am}#{vr}#{lp}'*40)