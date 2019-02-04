# a = [simbolo, número n,..., número 0],[número 0,..., número n]
def imprimir(a):
    num=""
    for i in range(2):
        for j in range(len(a[i])):
            if i==0: j=-j-1
            elif i==1 and j==0 and a[i]!=[]: num+="."
            num+=str(a[i][j])
    return num
def tupla(a):
    if type(a)==int: return enterot(a)
    elif type(a)==float: return flotantet(a)
    else: raise TypeError("No es un número")
def enterot(x):
    ent=str(x)
    if ent[0]!="-": ent="+"+ent
    ent=list(ent)
    for i in range(1,len(ent)):
        ent[i]=int(ent[i])
    return ent[::-1],[]
def flotantet(x):
    flo=str(x);
    if flo[0]!="-": flo="+"+flo
    j=1; ent=[flo[0]]
    for i in flo[1:]: 
        j+=1
        if i==".":
            break
        ent=[int(i)]+ent
    dec=list(flo[j:])
    for i in range(1,len(dec)):
        dec[i]=int(dec[i])
    return ent,dec
def tratar(x,y):
    x=list(x)
    y=list(y)
    x[0]=x[0][0:-1]
    y[0]=y[0][0:-1]
    x[0]=x[0][::-1]
    y[0]=y[0][::-1]
    if len(x[1])<len(y[1]): x[1]+=(len(y[1])-len(x[1]))*[0]
    elif len(x[1])>len(y[1]): y[1]+=(len(x[1])-len(y[1]))*[0]
    if len(x[0])<len(y[0]): x[0]=(len(y[0])-len(x[0]))*[0]+x[0]
    elif len(x[0])>len(y[0]): y[0]=(len(x[0])-len(y[0]))*[0]+y[0]
    #hace que x,y tengan igual cantidad de dígitos
    #devuelve una tupla con x,y como listas y con la parte entera en orden normal
    return x,y
def tratarsin0(x,y):
    x=list(x) ; x[0]=x[0][0:-1] ; x[0]=x[0][::-1]
    y=list(y) ; y[0]=y[0][0:-1] ; y[0]=y[0][::-1]
    return x,y
def sin0aladerecha(x):
    l=x[1]; 
    i=1
    if len(l)>0:
        while i<=len(x[1]):
            if l[-i]!=0: 
                l[len(l)+1-i:]=[]
                break
            i+=1
            if i>len(l): 
                l[:]=[]
                break
    return x
def sin0alaizquierda(a):
    a=list(a); 
    i=2
    if len(a[0])>2:
        while i<=len(a[0]):
            if a[0][-i]!= 0: 
                a[0][-i+1:-1]=[]
                break
            i+=1
            if i>len(a[0]):
                a[0]=a[0][-2:]  
    return tuple(a)
def suma(x, y):
    vx=x[0][-1]
    vy=y[0][-1]
    if vx!=vy:
        if vx=="-": 
            x[0][-1]="+"
            return resta(y,x)
        else: 
            y[0][-1]="+"
            return resta(x,y)
    x,y=tratar(x,y);d=[];e=[];r=0
    vf=vy
    for j in reversed(range(2)):
        for i in range(len(y[j])):
            s= y[j][-i-1] + x[j][-i-1] + r
            if len(str(s))==2:
                r=int(str(s)[0])
                s=int(str(s)[1])
            else: r=0
            if j==1:d=[s]+d
            else:e=e+[s]
    if r!=0:  e=e+[r]
    z= e+[vf],d
    z=sin0aladerecha(z)
    return z
def mayorabs(x,y):
    xm,ym=tratar(x,y);
    xm=xm[0]+xm[1];ym=ym[0]+ym[1];
    if xm==ym:
        return y
    else:
        t=0
        while t<len(ym):
            if xm[t]<ym[t]:
                return y
            elif xm[t]>ym[t]:
                return x
            else:
                t+=1

def resta(x, y):
    vx=x[0][-1]
    vy=y[0][-1]
    if vx!=vy:
        if vx=="-": 
            y[0][-1]="-"
            return suma(y,x)
        else: 
            y[0][-1]="+"
            return suma(x,y)
    if not x==mayorabs(y,x): 
        x,y=y,x
        if vy=="+": vx="-"
        else: vx="+"
    [x,y]=tratar(x,y); 
    x=x[0]+x[1];ent=len(y[0]);y=y[0]+y[1];r=[]
    for i in range(len(y)):
        if x[-i-1] < y[-i-1]: 
            j=1
            while 2==2:
                if x[-i-1-j]>0:
                    x[-i-1-j]-=1
                    if j>1:
                        x[-i-j:-i-1]=[9]*(j-1)
                    x[-i-1]+=10
                    break
                else: j+=1
        s=x[-i-1] - y[-i-1]
        r=[s]+r
    e=r[ent-1::-1];d=r[ent:]
    z=e+[vx],d
    z=sin0alaizquierda(z)
    z=sin0aladerecha(z)
    return z


def multiplicacion(x, y):
    vx=int(x[0][-1]+"1")
    vy=int(y[0][-1]+"1")
    vf=vx*vy
    x=sin0alaizquierda(x);y=sin0alaizquierda(y)
    x=sin0aladerecha(x);y=sin0aladerecha(y)
    if vf==1: vf="+"
    x,y=tratarsin0(x,y);
    d3=len(x[1]);d2=len(y[1]);x=x[0]+x[1];y=y[0]+y[1]
    lx=len(x) ; p=[0,"+"],[0];d1=d2+d3; lt=lx+len(y); ent=lt-d1
    for i in range(lx):
        if x[-i-1]!=0:
            si=[]
            for j in range(len(y)):
                si+=[y[j]*x[-i-1]]
            si=(lx-i)*[0]+si+[0]*i
            d=si[ent:]; 
            e=si[:ent];
            e=e[::-1];
            si=e+["+"],d;
            p=suma(p,si); 
    l=p[0];l[-1]=str(vf)[0]
    p=sin0aladerecha(p)
    p=sin0alaizquierda(p)
    return p


def division(x, y,n=100):
    cero=([0,"+"],[]);
    if mayorabs(y,cero)==cero: raise ZeroDivisionError
    if mayorabs(x,cero)==cero: return cero
    vx=int(x[0][-1]+"1")  ; vy=int(y[0][-1]+"1")  
    vf=vx*vy
    if vf==1: vf="+"
    x=sin0alaizquierda(x)   ;   y=sin0alaizquierda(y)
    x=sin0aladerecha(x)   ;   y=sin0aladerecha(y)
    [x,yr]=tratarsin0(x,y); 
    dx=len(x[1]) ;   dy=len(yr[1])
    yr=yr[0]+yr[1] ; x=x[0]+x[1] ; yr.reverse() ; x.reverse(); 
    dec0=dy-dx  ;   ly=len(yr) ; cociente=[]
    x=[x+["+"],[]]  ;    r=x ;    y=[yr+["+"],[]]; 
    from numpy import asarray as np
    yr=np(yr); diez=([0,1,"+"],[]) ; r1=1 ; j=0
    while len(cociente)< n and not comparacion(x,cero):
        if x!=mayorabs(y,x) and r1==0: 
            x=list(x); x[0]=[0]+x[0]; r=x; r1=1
        elif comparacion(x,mayorabs(multiplicacion(diez,y),x)):
            x=x[0][-2::-1] ;  q=x[:ly] ;x=x[ly:] ;q=[q[::-1]+["+"],[]]; 
            if comparacion(y,mayorabs(y,q)) and not comparacion(q,y): 
                q[0]=x[:1]+q[0];x=x[1:]; 
            while True:
                if q!=mayorabs(y,q) and r1==0: 
                    q=list(q); 
                    if x==[]:
                        x=r; break
                    q[0]=x[:1]+q[0]; r=q;x=x[1:]; r1=1
                else: 
                    i=0 ; j+=1
                    while i<10:
                        intento=yr*i;
                        intento=list(intento); 
                        intento=intento+["+"],[];
                        intento=suma(cero,intento);
                        r=resta(q,intento);
                        if not comparacion(r,mayorabs(y,r)): break
                        i+=1
                    cociente+=[i]
                    q=r;r1=0
        else: 
            i=0 ; 
            if j==0: j=1
            while i<10:
                intento=yr*i; 
                intento=list(intento); 
                intento=intento+["+"],[]
                intento=suma(cero,intento);
                r=resta(x,intento); 
                if not comparacion(r,mayorabs(y,r)):  break
                i+=1
            cociente+=[i]; 
            x=r; r1=0
    com=dec0+j; 
    if com >= 0:e=cociente[:com];e.reverse(); cociente=e+[str(vf)[0]],cociente[com:]
    else: cociente=[0]+ [str(vf)[0]],[0]*abs(com)+cociente
    return cociente


def comparacion(x, y):
    vx=int(x[0][-1]+"1")
    vy=int(y[0][-1]+"1")
    xm,ym=tratar(x,y)
    if xm==ym and vx==vy: 
        #print("son iguales")
        return True
    else:
        #print("no son iguales")
        return False


def pi(x=1000):
    s=[0,"+"],[] ; k=0 ; uno=[1,"+"],[] ; j=uno ; dos=[2,"+"],[]
    for i in range(1,x):
        k=k%2 + 1 
        if k==1: a=resta;
        else: a=suma;
        j=suma(j,dos);
        b=division(uno,j)
        s=a(s,b); 
    s=suma(s,uno) 
    s=multiplicacion(s,([4,"+"],[]))
    return s


if __name__ == "__main__":
    print(imprimir(pi()))
