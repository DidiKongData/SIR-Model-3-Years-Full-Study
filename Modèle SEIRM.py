import matplotlib.pyplot as plt
# Programme où régissent les 5 équations du système SEIRM.
def Euler(F,C,G,H,M,t0,tf,x0,c0,y0,z0,m0,n) :
    t=t0 # Origine des Temps
    x=x0 # Nombre de personnes saines   à t = 0.
    c=c0 # Nombre de personnes infectés à t = 0.(non-contagieux)
    y=y0 # Nombre de personnes inféctes à t = 0.
    z=z0 # Nombre de personnes rétablis à t = 0.
    m=m0 # Nombre de personnes décedés  à t = 0.
    h=(tf-t0)/float(n) # Plus il est petit (ie plus n est grand), meilleure est la précision !
    temps=[t0] # Liste du temps en abscisse
    X=[x0] # Liste contenant les valeurs de S(t) (n valeurs entre t0 et tf)
    C0=[c0]# Liste contenant les valeurs de C(t) (n valeurs entre t0 et tf)
    Y=[y0] # Liste contenant les valeurs de I(t) (n valeurs entre t0 et tf)
    Z=[z0] # Liste contenant les valeurs de R(t) (n valeurs entre t0 et tf)
    M0=[m0]# Liste contenant les valeurs de M(t) (n valeurs entre t0 et tf)
    for i in range(n) :
        # Résolution du système différentiel ---> Méthode d'Euler :
        # Consiste à approximer localement les dérivées par la tangente.
        x,c,y,z,m=x+h*F(t,x,c,y,z,m),c+h*C(t,x,c,y,z,m),y+h*G(t,x,c,y,z,m),z+h*H(t,x,c,y,z,m),m+h*M(t,x,c,y,z,m)
        t=t+h
        temps.append(t)
        X.append(x)
        C0.append(c)
        Y.append(y)
        Z.append(z)
        M0.append(m)
    N=[]
    for k in range(len(temps)):
        N.append(X[k]+C0[k]+Y[k]+Z[k]) # Liste contenant la population totale N(t) (n valeurs entre t0 et tf)
    plt.plot(temps,N,"--")
    plt.plot(temps,X,color="b")
    plt.plot(temps,C0,color="g")
    plt.plot(temps,Y,color="y")
    plt.plot(temps,Z,color="r")
    plt.plot(temps,M0,color="black")
    plt.xlabel('TEMPS (t)')
    plt.ylabel('POPULATION (%)')
    plt.legend(["Population Totale","Sains","Infectés non-contagieux","Infectés","Rétablis","Morts"])
    plt.axis([0,35,0,1]) # Abscisses allant de 0 à 17.5 et ordonnées de 0 à 1
    # Abscisse allant à "tf" possible aussi
    plt.grid() # Affiche la grille
    plt.title("Modélisation SEIRM avec 'Méthode d'Euler'")
    plt.show()

β=0.5 # β le taux de transmission ( = k*log(1-c) )
# c : probabilité de transmission lors d’un contact entre un infectieux et un susceptible
# k : nombre de contact d’un individu avec d’autres individus de la population par unité de temps
ν=21.1 # ν le temps moyen d'incubation
λ=11   # λ le temps moyen de guérison
γ=1/λ  # γ le taux de guérison ( = 1/λ )
μ=0.04 # μ le taux de mortalité
# α
def F(t,x,c,y,z,m): # Correspond à S'(t) = -β*S(t)*I(t)
    return(-β*x*y)
def C(t,x,c,y,z,m): # Correspond à C'(t) = β*S(t)*I(t)-(1/ν)*C(t)
    return(β*x*y-(1/ν)*c)
def G(t,x,c,y,z,m): # Correspond à I'(t) = (1/ν)*C(t)-(1/λ)*I(t)-μ*I(t)
    return((1/ν)*c-γ*y-μ*y)
def H(t,x,c,y,z,m): # Correspond à R'(t) = (1/λ)*I(t)
    return(γ*y)
def M(t,x,c,y,z,m): # Correspond à M'(t) = μ*I(t)
    return(μ*y)

#Euler(F,C,G,H,M,0,20,0.9,0.05,0.05,0,0,1000)
Euler(F,C,G,H,M,0,35,0.3,0.36,0.34,0,0,100000)
#R0 =
#β * c * d
#taux de contact, nombre de contacts, durée de la période contagieuse
#X=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
#Y=[1,1,1,10,50,100,200,800,1000,1050,1020,900,450,250,220,100,70,60,60,70,40,1]
#plt.plot(X,Y)
#plt.show()
