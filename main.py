consultas = [ 
    {'nome': 'Emerson', 'cpf': '163.659.098-80', 'senha': 'Carasuja@3', 'hora': '12:00', 'especialidade': 'odontologia'}
]

menu = ['cadastrar consulta', 'listar', 'Pesquisar por hora', 'cancelar consulta', 'editar']
dados = ['nome', 'cpf', 'hora', 'especialidade']

opc = 0
while opc != -1:

    for i in range(5):
        print(f'{i+1} - {menu[i]}')

    opc = int(input('Digite sua opção: '))
    if opc == 1:
       
        hora = str(input('digite o horario deseja: '))

        existe  = False
        for i in consultas:
            if i['hora'] == hora:
                existe = True
                break
        
        if existe == True:
            print('\nHorario não disponivel!, tente outro')
            print()
        else:
            nome = str(input('digite seu nome: '))
            cpf = str(input('Digite o seu cpf: '))
            senha = str(input('Digite a senha: '))
            especialidade = str(input('\n--Serviços diponiveis--\n- Clínica Geral\n- Pediatria\n- Ginecologia\n- Odontologia\ndigite a especialidade que deseja: ')).lower()

            agendamento = {
                'nome': nome,
                'CPF': cpf,
                'senha': senha,
                'hora': hora,
                'especialidade': especialidade
            }

            consultas.append(agendamento)

    elif opc == 2:

        if len(consultas) > 0:

            for i in consultas:
                print('-----')
                for j in dados:
                    print(f'{j}: {i[j]}')

            print()
        
    elif opc == 3:
        if len(consultas) > 0:
            pesqHora = str(input('Digite a hora que deseja pesquisar: '))
            existe = False
            pos = 0

            for i in consultas:
                if i['hora'] == pesqHora:
                    existe = True
                    pos += 1
                    break

            if existe == True:
                for i in consultas:
                    print('+---+---+')
                    for j in dados:
                        print(f'{j}: {i[j]}')
                
                print()
            else:
                print('Horario não encontrado')

    elif opc == 4:
        if len(consultas) > 0:
            esc = input('Deseja realmente cancelar consulta? (s/n): ')

            if esc == 's':
                user = input('Digite o nome de usuario: ')
                existe = False

                for i in consultas:
                    if i['nome'] == user: 
                        existe = True
                        break
                
        else:
            print('Nenhuma consulta agendada no nosso sistema!')
            

    elif opc == -1:
        break

        
            



    