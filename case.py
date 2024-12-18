dia = input('Que dia é Hoje? ')
match dia:
        case'1':
            print('hj é Seg')
        case'2':
            print('hj é Ter')
        case'3':
            print('hj é Qua')
        case'4':
            print('hj é Qui')
        case'5':
            print('hj é Sex')
        case'6':
            print('hj é Sab')
        case'7':
            print('hj é Dom')
        case _: #colocamos _ para o fim, cono nada de interresante.
            print('digite um numero')
