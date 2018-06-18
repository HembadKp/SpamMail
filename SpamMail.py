#!/usr/bin/python3

import smtplib
import os as sistema

sistema.system('cls' if sistema.name == 'nt' else 'clear')

def banner():
    ban = '''
    +---------------------------------------+
    ____                        __  __       _ _
/ ___| _ __   __ _ _ __ ___ |  \/  | __ _(_) |
\___ \| '_ \ / _` | '_ ` _ \| |\/| |/ _` | | |
 ___) | |_) | (_| | | | | | | |  | | (_| | | |
|____/| .__/ \__,_|_| |_| |_|_|  |_|\__,_|_|_|
      |_|

        Editado por: Coringa/Hembad
  
    +---------------------------------------+    
    '''
    print(ban)

banner()

try:
    print('====' * 10)
    meu_email = input('[*]Seu Gmail: ')
    print('====' * 10)
    min_senha = input('[*]Sua senha: ')
    print('====' * 10)
    destinatario = input('[*]Email que deseja floodar: ')
    print('====' * 10)
    assunto = input('[*]Assunto: ')
    print('====' * 10)
    menssagem = input('[*]Menssagem: ')
    print('====' * 10)
    quantidade = int(input('[*]Quantidade de Emails: '))
    print('====' * 10)

    i = 0

    while (i < quantidade):
        i = i + 1

        msg_header = 'Content-type: text/html\n' \
                     'Subject: {}\n'.format(assunto)
        msg_content = '<h2> <font color="black"> {menssagem} </font></h2>\n'.format(menssagem=menssagem)
        msg_full = (''.join([msg_header, msg_content])).encode()

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(meu_email, min_senha)
        server.sendmail(meu_email,
                        [destinatario, destinatario],
                        msg_full)
        server.quit()

        print('[{}]Email enviado...'.format(i))

except:
    erro = '''
    +------------------------------------------------------+
    | Algo deu errado!                                     |
    | Certifique-se de que seu email/senha estão corretos! |
    | Permita aplicativos menos seguros em:                |
    | https://myaccount.google.com/lesssecureapps?pli=1    |
    +------------------------------------------------------+
    '''
    print(erro)