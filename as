passwd=open('passwd.txt')
linha=passwd.readlines()
n=len(linha)
usuario=[]
senha=[]
i=0
for linha in linha:
    dados=linha.split(":")
    usuario.append(dados[0])
    senha.append(dados[1])

print(usuario[4])






passwd.close()
