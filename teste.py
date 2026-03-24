# tabela de cor e como definir cor ou negrito no python
RED = '\033[31m'
GREEN = '\033[32m'
BOLD = '\033[1m'
RESET = '\033[0m'

# aqui eu pergunto o nome da pessoa
nome = input('qual teu nome? ').lower() #.lower() serve pra captar tanto KYO e kyo
tentativas = 5
bla = ['kyo', 'enzo', 'valentina']
# setto uma condicao pra caso o nome da pessoa seja kyo
if nome in bla:
    """
    aqui eu uso o while pra coemcar o loop
    basicamente toda vez que a tentativa for maior que 0 ele vai refazer a pergunta
    """
    while tentativas > 0:
        aura = int(input('\nvalor em numero apenasssssssssssssssssss\nquantos de aura voce tem? '))
        
        if aura > 0:
            tentativas -= 1
    
            if tentativas == 0:
                print(f'{BOLD}{RED}NEGATIVO.{RESET}')
                print(f'sua aura na real e negativa.')

            elif tentativas == 1:
                print(f'{BOLD}{RED}NEGATIVO.{RESET}')
                print(f'ultima tentativa restante.')
            
            else: 
                aura > 0
                print('negativo.')
                print(f'tentativas restantes: {tentativas}')
        else:
            print(f'{BOLD}{GREEN}que bom que sabe.{RESET}')
            break
else:
    print(f'imagine se chamar {nome} 🤣😂😂😂😂🤣😂🤣🤣🤣🤣 LOL!')

    
