# ETE PORTO DIGITAL
# PROFESSOR: CLOVES ROCHA
# EXERCÍCIO DA AULA 4
# DUPLA: LUCILA SILVA E VITÓRIA 

# Desenvolva [em dupla] um algoritmo/programa que:
# Execute comandos de controle/decisão de um aeromodelo:
# Acelerar;
# Decolar;
# Planar;
# Função Piloto Automático;
# Pousar.

print('1.Acelerar\n2.Decolar\n3.Planar\n4.Função Piloto Automático\n5.Pousar')
acao = int(input('Qual ação você deseja executar?\n'))
if acao == 1:
  print('Você está acelerando o avião')
elif acao == 2:
  print('Você vai decolar')
elif acao == 3:
  print('Você está planando o avião')
elif acao == 4:
  print('Você está na Função de Piloto Automático')
elif acao == 5:
  print('Você está pousando o avião')
else:
  print('Você não escolheu nenhum dos comandos')
