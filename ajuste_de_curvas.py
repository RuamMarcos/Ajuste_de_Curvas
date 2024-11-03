
# pts -> lista de pontos com elementos no formato: [x, y]
# reta -> lista com dois elementos ["ax + b", f(x)], 
#     1° Str com a lei de formação
#     2° É a função, que recebe o argumento x e retorna a imagem dele.

# retorna uma lista de pares ordenados
def ler_pts():
    pts = []
    n = 0

    print("\n\nDigite 'stop' para interromper a leitura dos pontos.")

    print("-"*10)

    while(1):
        x = input(f"\nx[{n}]: ")
        if x == 'stop' :
            break

        y = input(f"y[{n}]: ")
        if y == 'stop':
            break
        
        pts.append([float(x), float(y)])
        n+=1

    return pts

# retorna a lei de formação da reta e a função da reta
def ler_reta():
    print("Insira os coeficientes 'a' e 'b' de uma reta aletória: y = ax + b")

    a = float(input("a: "))
    b = float(input("b: "))   

    return fazer_reta(a, b)

def fazer_reta(a, b):
    y = []
    if (b > 0):
        y.append(f"{a}x + {b}")
    elif (b < 0):
        y.append(f"{a}x - {b*-1}")
    else:
        y.append(f"{a}x")
    y.append(lambda x: a*x + b)
    

    return y

# calcula o desvio total, dado uma lista de pontos e uma reta
def calcular_desvio(pts, reta):
    desvio = 0

    for i in pts:
        desvio += (i[1] - reta[1](i[0]))**2

    return desvio

#retorna a melhor reta de uma lista de pontos
def melhor_reta(pts):     

    a = len(pts)*sum(list(map(lambda par: par[0]*par[1], pts))) - sum(list(map(lambda z: z[0], pts)))*sum(list(map(lambda z: z[1], pts)))
    a = a / ((len(pts)*sum(list(map(lambda x: x[0]*x[0], pts)))) - (sum(list(map(lambda z: z[0], pts))))**2)
    b = (sum(list(map(lambda x: x[1], pts))) - a * (sum(list(map(lambda x: x[0], pts)))))/len(pts)
    
  
    return fazer_reta(a, b)
    