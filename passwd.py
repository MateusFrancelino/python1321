def criauser(usuario,id):
    usuario.append(input("Digite o Nome de usuario"))
    id.append(input("Digite o ID"))
    id2.append(input("Digite o ID de grupo"))
    name.append(input("Digite o Nome"))
    home.append(input("Digite o Home"))














passwd=open('passwd.txt')
linha=passwd.readlines()
passwd.close()
entrada=True

n=len(linha)
usuario=[]
senha='x'
id=[]
id2=[]
name=[]
home=[]
shell=[]
i=0
for linha in linha:
    dados=linha.split(":")
    usuario.append(dados[0])
    id.append(dados[2])
    id2.append(dados[3])
    name.append(dados[4])
    home.append(dados[5])
    shell.append(dados[6])
    print (dados[0],":",dados[1],":",dados[2],":",dados[3],":",dados[4],":",dados[5])


while(entrada==True):
    print("1-Para criar novo usario")
    print("2-Para excluir usuario")
    print("3-Para sair")
    select=int(input())
    if(select==1):
        criauser(usuario,id)
    else:
        entrada=False



saida.close()