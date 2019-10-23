def criauser(usuario,id,id2,name,home,shell):
    usuario.append(input("Digite o Nome de usuario"))
    id.append(input("Digite o ID"))
    id2.append(input("Digite o ID de grupo"))
    name.append(input("Digite o Nome"))
    home.append(input("Digite o Home"))
    shell.append(input("Digite o Shell"))


def deletauser(usuario,id,id2,name,home,shell):
    numero_usuario=input("Digite o usuario Para exluir")
    if(numero_usuario in id):
        n=id.index(numero_usuario)
        del usuario[n]
        del id[n]
        del id2[n]
        del name[n]
        del home[n]
        del shell[n]
    else:
        print ("ID não encontrado")


def cria_arquivo(usuario,id,id2,name,home,shell):
    cont = 0
    novoarquivo = open("novoarquivo.txt","w")
    for aux in usuario:
        line = (usuario[cont]+":x:"+id[cont]+":"+id2[cont]+":"+name[cont]+":"+home[cont]+":"+shell[cont]+"\n")
        novoarquivo.write(line)
        cont += 1
    novoarquivo.close()
def mostrar(usuario,id,id2,name,home,shell):
    n = len(usuario)
    for aux in range(0,n):
        print(usuario[aux],id[aux],id2[aux],name[aux],home[aux],shell[aux])


def moduser(usuario,id,id2,name,home,shell):
    numero_usuario = input("Digite o usuario Para modificar")
    if (numero_usuario in id):
        n=id.index(numero_usuario)
        usuario[n]=input("Digite o novo usuario ")
        id[n]=input("Digite o novo ID")
        id2[n]=input("Digite o novo ID de grupo")
        name[n]=input("Digite o novo nome")
        home[n]=input("Digite o novo home")
        shell[n]=input("Digite o novo shell")
    else:
        print ("ID não encontrado")







passwd=open('passwd.txt')
linha=passwd.readlines()
passwd.close()
entrada=True


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
    print("3-Para editar um usuario")
    print("4-Para Salvar Arquivo")
    print("5-Para Mostrar Conteudo")
    print("5-Para sair")
    select=int(input())
    if(select==1):
        criauser(usuario,id,id2,name,home,shell)
    elif(select==2):
        deletauser(usuario,id,id2,name,home,shell)
    elif(select==3):
        moduser(usuario,id,id2,name,home,shell)
    elif (select == 5):
        mostrar(usuario, id, id2, name, home, shell, )

    elif(select==4):
        cria_arquivo(usuario,id,id2,name,home,shell)
    else:
        entrada=False


