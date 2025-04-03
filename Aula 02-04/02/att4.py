nome = input("Digite seu nome: ")

while nome!= "Joe":
    nome = input("Digite seu nome:")


for tentativas in range(3):
    senha = input("Digite a senha: ")
    if senha == "swordfish":
        print("Correta")
        break
    else:
        print("Errada")
        
print("Encerramento")