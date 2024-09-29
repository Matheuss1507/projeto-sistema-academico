sistema_academico = {}
carga_horaria = int(input("Qual a carga horária da disciplina? "))

def situacao_aluno(aluno):
    for nome in sistema_academico:
     media = sum(aluno['notas']) / len(aluno['notas']) 
     porcentagem_frequencia = (aluno['frequencia'] / carga_horaria) * 100
     
     if porcentagem_frequencia < 75:
        return "Reprovado por falta"
     elif media >= 7:
        return "Aprovado por média"
     else:
        return "Reprovado por média"
    
opcao = 1

while opcao != 8:
    
    print("""\n1 - Adicionar aluno
2 - Remover aluno
3 - Adicionar notas
4 - Adicionar frequencia
5 - Editar informações
6 - Impressão de relatório de situação dos alunos
7 - Impressão de relatório de uma situação específica (Filtrar por: Aprovado, Reprovado por Falta ou Reprovado por Nota)
8 - Sair\n""")
    
    opcao = int(input("Qual sua opção? "))
    
    if opcao ==1:
        nome = input("Qual o nome do aluno? ")
        if nome in sistema_academico:
         print("Esse aluno já foi adicionado")
        else:
         sistema_academico[nome] = {"notas": [], "frequencia": 0}
         print(f"Aluno {nome} foi adicionado")

    elif opcao ==2:
        nome = input("Qual o nome do aluno que você quer remover? ")
        if nome in sistema_academico:
          del sistema_academico[nome]
          print(f"Aluno {nome} foi removido")
        else:
          print(f"Aluno {nome} não foi encontrado")
        
    elif opcao ==3:
        nome = input("Qual o nome do aluno que você quer adicionar as notas? ")
        if nome in sistema_academico:
           while len(sistema_academico[nome]['notas']) < 4:
             nota = float(input(f"Nota {len(sistema_academico[nome]['notas']) + 1}: "))
             sistema_academico[nome]['notas'].append(nota)
        else:
          print(f"Aluno {nome} não foi encontrado")

    elif opcao ==4:
        nome = input("Qual o nome do aluno que deseja adicionar a frequência? ")
        if nome in sistema_academico:
          frequencia = int(input(f"Qual a frequência do aluno {nome}? "))
          sistema_academico[nome]['frequencia'] = frequencia
        else:
          print(f"Aluno {nome} não foi encontrado") 

    elif opcao ==5:
       nome = input("Qual o nome do aluno que você quer editar? ")
       if nome in sistema_academico:
            nome_novo = input(f"Qual o novo nome para o aluno {nome}? ")
            sistema_academico[nome_novo] = sistema_academico.pop(nome)
            print(f"Nome do aluno {nome} foi alterado para {nome_novo}.")
       else:
            print(f"Aluno {nome} não foi encontrado.")
    elif opcao ==6:
       print("Relatório da situação dos alunos:")
       for nome in sistema_academico:
         aluno = sistema_academico[nome]
         media = sum(aluno['notas']) / len(aluno['notas']) 
         situacao = situacao_aluno(aluno)
        
         print(f"{nome} - nota: {media} / frequência: {aluno['frequencia']} aulas - ({situacao})")
    elif opcao ==7:
       situacao_filtro = input("Qual a situação que você deseja filtrar: Reprovado por falta, Aprovado por média, ou Reprovado por média? ")
       print(f"\nRelatório filtrado por: {situacao_filtro}")
       for nome in sistema_academico:
         aluno = sistema_academico[nome]
         media = sum(aluno['notas']) / len(aluno['notas']) 
         situacao = situacao_aluno(aluno)
         if situacao == situacao_filtro:
            print(f"{nome} - nota: {media} / frequência: {aluno['frequencia']} aulas - ({situacao})")
    elif opcao ==8:
       print("Saindo...")
       