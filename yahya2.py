def motavalide (mot):


    if (len(mot)>4 and 25 >len(mot)) and mot.isupper() :

        return True
    else :

        return False

def convertirCH (mot):
    t=[]
    for i in mot :
        t.append(i)
    return  t
def initalisatn (tcar):

    if motavalide("YAHYA"):
        tcar=convertirCH("YAHYA")
    return tcar
def creeressai (tessai,n):
    for i in range(n):
        tessai.append("*")
    return tessai
def afficher (tcar):
    m= ''.join(tcar)
    return m
def jouer(tcar,tessai,c):
    j=0
    for i in range(len(tcar)):
        if tcar[i]==c:
            tessai[i]=c
            j=1
    if(j==1):
        return True
    else:
        return False

def estfini (tessai):
    if '*' in tessai:
        return False
    else:
        return  True


t=[]
t1=[]
tcar=[]
tess=[]

tcar=initalisatn(t)

tess=creeressai(t1,len(tcar))
print(tess)
i=0
while i<5:
    c=input('donner un caracter magiscile:')
    if jouer(tcar,tess,c):
        print(tess)
    else:
        i=i+1
        print('il reste ',5-i,'tentatifs')
    if(estfini(tess)):
        print('reussi le mot est:',afficher(tess))
        break

    if(i==5):
        print('echouee')
        break
