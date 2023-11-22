import matplotlib.pyplot as plt
# Programme où régissent les 4 équations du système SIRM.
def Euler(F,t0,tf,X0,n) :

    t  = t0      # Origine des Temps
    x  = X0[0]   # Nombre de personnes saines   à t = 0.
    y1 = X0[1]   # Nombre de personnes inféctes par la souche 1 à t = 0.
    y2 = X0[2]   # Nombre de personnes inféctes par la souche 2 à t = 0.
    z  = X0[3]   # Nombre de personnes rétablis à t = 0.
    m  = X0[4]   # Nombre de personnes décedés  à t = 0.
    h  = (tf-t0)/float(n)

    # Plus h est petit (i.e. plus n est grand), meilleure est la précision !

    temps = [t0] # Liste du temps en abscisse
    X  = [X0[0]] # Liste contenant les valeurs de S(t)  (n valeurs entre t0 et tf)
    Y1 = [X0[1]] # Liste contenant les valeurs de I1(t) (n valeurs entre t0 et tf)
    Y2 = [X0[2]] # Liste contenant les valeurs de I2(t) (n valeurs entre t0 et tf)
    Z  = [X0[3]] # Liste contenant les valeurs de R(t)  (n valeurs entre t0 et tf)
    M  = [X0[4]] # Liste contenant les valeurs de M(t)  (n valeurs entre t0 et tf)e

    for i in range(n) :
        # Résolution du système différentiel ---> Méthode d'Euler :
        # Consiste à approximer localement les dérivées par la tangente.

        x  = x  + h*F(x,y1,y2,z,m)[0]
        y1 = y1 + h*F(x,y1,y2,z,m)[1]
        y2 = y2 + h*F(x,y1,y2,z,m)[2]
        z  = z  + h*F(x,y1,y2,z,m)[3]
        m  = m  + h*F(x,y1,y2,z,m)[4]
        t  = t  + h

        temps.append(t)
        X.append(x)
        Y1.append(y1)
        Y2.append(y2)
        Z.append(z)
        M.append(m)

    plt.plot(temps,X,color="b")
    plt.plot(temps,Y1,"--")
    plt.plot(temps,Y2,'+',color="y")
    plt.plot(temps,Z,color="r")
    plt.plot(temps,M,color="black")
    plt.xlabel('TEMPS (t)')
    plt.ylabel('POPULATION (%)')
    plt.legend(["Sains","Infectés par la souche 1","Infectés par la souche 2","Rétablis","Morts"])
    plt.axis([0,tf,0,1])  # Abscisse allant à "tf" possible aussi
    plt.grid()            # Affiche la grille
    plt.title("Modèle SIRM à 2 souches de virus")
    plt.show()

β1=2.3  # β le taux de transmission
β2=3

γ1=0.6  # γ le taux de guérison ( = 1/λ où λ le temps moyen de guérison )
γ2=0.1

μ1=0.05 # μ le taux de mortalité
μ2=1.3

def F(x,y1,y2,z,m):
    return [-β1*x*y1-β2*x*y2,β1*x*y1-γ1*y1-μ1*y1,β2*x*y2-γ2*y2-μ2*y2,γ1*y1+γ2*y2,μ1*y1+μ2*y2]

# Correspond à S'(t) = -β1*S(t)*I1(t)-β2*S(t)*I2(t)
# Correspond à I1'(t) = β1*S(t)*I1(t)-γ1*I1(t)-μ1*I1(t)
# Correspond à I2'(t) = β2*S(t)*I2(t)-γ2*I2(t)-μ2*I2(t)
# Correspond à R'(t) = γ1*I1(t) + γ2*I2(t)
# Correspond à M'(t) = μ1*I1(t) + μ2*I2(t)

# α ν
Euler(F,0,10,[0.95,0.025,0.025,0,0],170)
