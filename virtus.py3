a,b = input().split(" ") # pega 2 valores na mesma linha e atribui a variáveis

# Converte o valor para os tipos necessários
a = int(a)
b = int(b)
c = 0
l = []

l = list(map(int, input().split(" ")))

for k in range(b):
    if(len(l) == 0):
        print("0")

    else:
        c = min(l)
        g = l.index(c)
        if(l[g] == 0):
            l.remove(c)
            c = min(l)
            g = l.index(c)
            l.remove(c)
            print(c)
            for i in range(len(l)):
                l[i] -= int(c)

        else:
            l.remove(c)
            print(c)
            for i in range(len(l)):
                l[i] -= int(c)