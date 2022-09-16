# Esse código separa os níveis de prioridade dos atendimentos, em um hospital em idade ou em salas

nome = input('Qual é o seu nome, paciente? ')
idade = int(input('Qual é a sua idade? '))
doenca = input('Teve alguma doenca infectocontagiosa, nos últimos 7 dias? ').upper()
if idade >= 65 and doenca == 'SIM':
    print('O/A paciente {} precisa de atendimento prioritáio na sala amarela!'.format(nome))
elif idade >= 65 and doenca == 'NAO':
    print('O/A paciente {} precisa de atendimento prioritário na sala branca!'.format(nome))
elif idade < 65 and doenca == 'SIM':
    print('O/A paciente {} precisa de atendimento na sala amarela!'.format(nome))
elif idade < 65 and doenca == 'NAO':
    print('O/A paciente {} precisa de atendimento na sala branca!'.format(nome))
else:
    print('Responda as perguntas corretamente para que o atendimento seja realizado!')
