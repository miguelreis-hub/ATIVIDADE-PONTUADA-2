import os 
os.system("cls")

preco_total = 0

quantidade_de_exames = 0

lista_codigo = []

lista_nome_exame = []

lista_precos_exames = []



while True:
    
    print("""
          
1 - Hemograma Completo - R$ 25,00
2 - Raio-X - R$ 80,00
3 - Ultrassonografia - R$ 150,00
4 - Eletrocardiograma - R$ 100,00
5 - Tomografia - R$ 600,00
6 - Ressonância Magnética - R$ 900,00
7 - Exame de Glicose - R$ 15,00
""")
    
    opcao = int(input("Digite a opção do exame desejado = "))
    
    match opcao:
        
        
        case 1:
            
            lista_nome_exame.append("Hemograma Completo")
            lista_precos_exames.append(25.0)
            lista_codigo.append(1)
            
            quantidade_de_exames += 1
            
            preco_total += 25
            
            prosseguir = int(input("Deseja agendar outro exame? Aperte 1 para CONTINUAR ou 0 para PARAR = "))
            
            if prosseguir == 0:
                break
        
        case 2:
            
            lista_nome_exame.append("Raio-X ")
            lista_precos_exames.append(80.0)
            lista_codigo.append(2)
            
            quantidade_de_exames += 1
            
            preco_total += 80
            
            prosseguir = int(input("Deseja agendar outro exame? Aperte 1 para CONTINUAR ou 0 para PARAR = "))
            
            if prosseguir == 0:
                break
        
        case 3:
            
            lista_nome_exame.append("Ultrassonografia")
            lista_precos_exames.append(150.0)
            lista_codigo.append(3)
            
            quantidade_de_exames += 1
            
            preco_total += 150
            
            prosseguir = int(input("Deseja agendar outro exame? Aperte 1 para CONTINUAR ou 0 para PARAR = "))
            
            if prosseguir == 0:
                break
        
        case 4:
            
            lista_nome_exame.append("Eletrocardiograma")
            lista_precos_exames.append(100.0)
            lista_codigo.append(4)
            
            quantidade_de_exames += 1
            
            preco_total += 100
            
            prosseguir = int(input("Deseja agendar outro exame? Aperte 1 para CONTINUAR ou 0 para PARAR = "))
            
            if prosseguir == 0:
                break
        
        case 5:
            
            lista_nome_exame.append("Tomografia")
            lista_precos_exames.append(600.0)
            lista_codigo.append(5)
            
            quantidade_de_exames += 1
            
            preco_total += 600
            
            prosseguir = int(input("Deseja agendar outro exame? Aperte 1 para CONTINUAR ou 0 para PARAR = "))
            
            if prosseguir == 0:
                break
        
        case 6:
            
            lista_nome_exame.append("Ressonância Magnética")
            lista_precos_exames.append(900.0)
            lista_codigo.append(6)
            
            quantidade_de_exames += 1
            
            preco_total += 900
            
            prosseguir = int(input("Deseja agendar outro exame? Aperte 1 para CONTINUAR ou 0 para PARAR = "))
            
            if prosseguir == 0:
                break
        
        case 7:
            
            lista_nome_exame.append("Exame de Glicose")
            lista_precos_exames.append(15.0)
            lista_codigo.append(7)
            
            quantidade_de_exames += 1
            
            preco_total += 15
            
            prosseguir = int(input("Deseja agendar outro exame? DIGITE 1 para CONTINUAR ou 0 para PARAR = "))
            
            if prosseguir == 0:
                break
        
        case _:
             
            
            print("Dado invalido - Solicite o codigo novamente")

print("")
print("")

print("Exibindo resultado da lista........")
print("")

for i in range(quantidade_de_exames):
    
    print(f"{lista_codigo[i]} - {lista_nome_exame[i]} - {lista_precos_exames[i]}R$")

print("")

print(f"O preço total á pagar é = {preco_total}R$")

print("")



while True:
    
    pagamento = int(input("Qual é a forma do pagamento ? digite 1,2 ou 3 \n \n 1-Convenio \n 2-Particular \n 3-Cartao de credito \n \n digite =   "))
    print("")
    
    match pagamento:
    
        case 1:
            print("")
        
            print("CONVENIO")
        
            valor_desconto_convenio = preco_total * 0.15
        
            valor_total_convenio = preco_total - valor_desconto_convenio
        
            print(f"O valor do desconto é = {valor_desconto_convenio}R$")
            print(f"O valor total á pagar pelo convenio é de = {valor_total_convenio}R$")
            
            break
        
        case 2:
            
            print("")
            
            print("PARTICULAR")
            
            print(f"O valor total á pagar é de = {preco_total}R$ - sem desconto")
            
            break
        
        case 3:
            print("")
            
            print("CARTÃO DE CREDITO")
            
            valor_do_acrescimo = preco_total * 0.08
            
            valor_total_credito = preco_total + valor_do_acrescimo
            
            print(f"O valor do acréscimo é = {valor_do_acrescimo}R$")
            
            print(f"O valor total á pagar é = {valor_total_credito}R$")
            
            break
        
        case _:
            
            print("FORMA DE PAGAMENTO INVALIDA - DIGITE NOVAMENTE")

print("")
print("")
            
        
        
        
        