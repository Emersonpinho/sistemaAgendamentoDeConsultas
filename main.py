consultas = [ 
    {'nome': 'Emerson', 'cpf': '111', 'senha': '222', 'hora': '12:00', 'total' : 720}
]

lixeira = []

menu = ['Sair','cadastrar consulta', 'listar', 'Pesquisar por hora', 'cancelar consulta', 'editar']
dados = ['nome', 'cpf', 'hora']

opc = 0
while True:

    for i in range(6):
        print(f'{i} - {menu[i]}')

    opc = int(input('Digite sua opção: '))

    if opc == 1:

        hora = str(input('Digite o HORÁRIO deseja (formato 00:00): '))
        nome = str(input('Digite seu NOME: '))
        cpf = str(input('Digite o seu CPF: '))
        senha = str(input('Digite a SENHA: '))

        meia_Hora = False
        existe_hora = False
        existe_cpf = False

        novaHora = ''
        
        for i in hora:
            if i != ':':
                novaHora += i

        # Desculpa Geam pela gambiarra foi ideia de Pedro ksksksks
        horaInt = int(novaHora)

        horas = horaInt // 100
        minu = horaInt % 100

        total = horas * 60 + minu

        podeAgendar = True

        for i in consultas:
            if total >= i['total']:
                dif = total - i['total']
            else:
                dif = i['total'] - total

            if dif < 30:
                podeAgendar = False
        
        if podeAgendar == True:

            for i in consultas:
                if cpf == i['cpf']:
                    existe_cpf = True
                    break

            for i in consultas:
                if i['hora'] == hora:
                    existe_hora = True
                    break
            
            if (existe_cpf == True) or (existe_hora == True):

                if existe_cpf == True:
                    print('CPF já existente')
                if existe_hora == True:
                    print('HORA já marcada. Tente outro horário!')
                if (existe_cpf == True) and (existe_hora == True):
                    print('CPF e Horário já existentes. Tente novamanete')

            else:

                agendamento = {
                    'nome': nome,
                    'cpf': cpf,
                    'senha': senha,
                    'hora': hora,
                    'total' : total
                }

                consultas.append(agendamento)
                print('\n!Consulta agendada com SUCESSO!\n')

        else:
            print('\n!Tempo limite excedido (30min cada consulta). Tente outra hora!\n')

    elif opc == 2:

        if len(consultas) > 0:

            for i in consultas:
                print('\n-----')
                for j in dados:
                    print(f'{j}: {i[j]}')

            print()
        else:
            print('\nNenhuma consulta cadastrada no nosso Sistema, garanta sua vaga!\n')
        
    elif opc == 3:
        if len(consultas) > 0:
            pesqHora = str(input('Digite a HORA pela qual deseja PESQUISAR (formato 00:00): '))
            existe = False
            pos = 0

            for i in consultas:
                if i['hora'] == pesqHora:
                    existe = True
                    break
                pos += 1

            if existe == True:
                print('+---+---+')
                for j in dados:
                    print(f'{j}: {consultas[pos][j]}')
                
                print()
            else:
                print('\nHorário NÃO encontrado\n')
        else:
            print('\nNenhuma consulta cadastrada no nosso sistema, volte mais tarde!')

    elif opc == 4:
        if len(consultas) > 0:
            user = input('Digite o NOME de usuário: ')

            existe = False
            pos = 0

            for i in consultas:
                if i['nome'] == user: 
                    existe = True
                    break
                pos+=1
                
            if existe == True:
                userSenha = str(input('Digite a SENHA do seu usuário: '))
                if i['senha'] == userSenha:
                    cancelar = input('Agendamento de consulta encontrado com SUCESSO!\n\nDeseja realmente CANCELAR a consulta PERMANENTEMENTE? (s/n): ')

                    if cancelar == 's':
                        lixo = consultas.pop(pos)
                        lixeira.append(lixo)
                        print('\nConsulta cancelada Com SUCESSO!!\n')
                    else:
                        print('\nOperação de cancelar interronpida!\n')

                else:
                    print('\nSenha INVÁLIDA, tente novamente!!\n')

            else:
                print('Consulta NÂO encontrada')

        else:
            print('Nenhuma consulta agendada no nosso sistema. Volte mais tarde!')

    elif opc == 5:
        if len(consultas) > 0:
            atualizaCpf = input('Digite o CPF do usuário para ATUALIZAR os dados: ')
            existe = False
            pos = 0
            
            for i in consultas:
                if i['cpf'] == atualizaCpf:
                    existe = True
                    break
                pos += 1

            if existe == True:
                senhaAtual = str(input('Digite sua SENHA atual: '))
                existeSenha = False

                if consultas[pos]['senha'] == senhaAtual:
                    existeSenha = True

                if existeSenha == True:

                    novoNome = str(input('Digite o novo NOME: '))
                    novoCpf = str(input('Digite o novo CPF para Atualizar: '))
                    novoHorario = str(input('Digite o novo HORÁRIO: '))

                    novaSenha = str(input('Digite a nova SENHA: '))

                    if novoNome != '':
                        consultas[pos]['nome'] = novoNome
                    if novoCpf != '':
                        consultas[pos]['cpf'] = novoCpf
                    if novoHorario != '':
                        consultas[pos]['hora'] = novoHorario
                    if novaSenha != '':
                        consultas[pos]['senha'] = novaSenha

                    print('Dados atualizados com SUCESSO!')
                                        
                else:
                    print('Senha INCORRETA. Tente novamente.')

            else:
                print('CPF NÃO encontrado!')
        else:
            print('\nNenhuma consulta cadastrada no nosso sistema!\n')
            
    elif opc == 0:
        break

    else:
        print('\nOpção INVÁLIDA, tente novamente!\n')