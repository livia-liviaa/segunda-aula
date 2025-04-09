def main():
  nome= ""
  idade= 0 
  email= ""
  cidade=""
  profissao= ""
  opcao = 0
while True: #(enquanto for verdadeiro executa o codigo) true= verdade
        print("\n MENU PRINCIPAL")
        print("1. Cadastrar o usuário")
        print("2. Ver dados cadastrados")
        print("3. Sair do sistema ")
        opcao= int(input("Escolha a opção: "))
        if opcao ==1:
            print ("Cadastrar o usuário")
            nome = input("Digite seu nome: ")
            idade =input ("Digite sua idade: ") 
            email= input("Dgite seu e-mail: ")
            cidade= input("Digite sua cidade: ")
            profissao=input("Digite sua profissão: ")


        elif opcao ==2: #elif(senão se)
            if nome == "" and idade==0 and email=="" and cidade=="" and profissao=="":
                print("Nenhum dado cadastrado ainda!\n")
            else:
                print("Dados cadastrado\n")
                print(f"Nome:{nome}\n") # f é função
                print(f"idade:{idade}\n")
                print(f"e-mail:{email}\n")
                print(f"cidade:{cidade}\n")
                print(F"profissão:{profissao}\n")
        elif opcao == 3:
            print("Encerrando o sistema...\n")
            break # sai do loop while, terminando o programa
        else: # else (senão)
            print("Opção invalida!Tente novamente")
        # verifica se este script está seno executado diretamente
if __name__ == "__main__":
    main()