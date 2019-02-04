class MyFloat:
    def __init__(self,t):
        if type(t)!=tuple and type(t)!=list: t=t.tupla()
        self.t=t
    def tupla(a):
        if type(a)==int: return a.enterot()
        elif type(a)==float: return a.flotantet()
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
    def __str__(self):
        num=""
        for i in range(2):
            for j in range(len(self.t[i])):
                if i==0: j=-j-1
                elif i==1 and j==0 and self.t[i]!=[]: num+="."
                num+=str(self.t[i][j])
        return num        
    def tratar(self,other):
        x=[1,1];x[0]=self.t[0][:];x[1]=self.t[1][:];
        y=[0,1];y[0]=other.t[0][:];y[1]=other.t[1][:];
        x[0]=x[0][0:-1]
        y[0]=y[0][0:-1]
        x[0]=x[0][::-1]
        y[0]=y[0][::-1]
        if len(x[1])<len(y[1]): x[1]+=(len(y[1])-len(x[1]))*[0]
        elif len(x[1])>len(y[1]): y[1]+=(len(x[1])-len(y[1]))*[0]
        if len(x[0])<len(y[0]): x[0]=(len(y[0])-len(x[0]))*[0]+x[0]
        elif len(x[0])>len(y[0]): y[0]=(len(x[0])-len(y[0]))*[0]+y[0]
        return x,y
    def tratarsin0(self,other):
        x=[1,1];x[0]=self.t[0][:];x[1]=self.t[1][:];
        x[0]=x[0][0:-1] ; x[0]=x[0][::-1]
        y=[0,1];y[0]=other.t[0][:];y[1]=other.t[1][:]
        y[0]=y[0][0:-1] ; y[0]=y[0][::-1]
        return x,y
    def sin0aladerecha(self):
        l=self.t[1]; 
        i=1
        if len(l)>0:
            while i<=len(self.t[1]):
                if l[-i]!=0: 
                    l[len(l)+1-i:]=[]
                    break
                i+=1
                if i>len(l): 
                    l[:]=[]
                    break
        return self
    def sin0alaizquierda(self):
        self.t=list(self.t); 
        i=2;
        if len(self.t[0])>2:
            while i<=len(self.t[0]):
                if self.t[0][-i]!= 0: 
                    self.t[0][-i+1:-1]=[]
                    break
                i+=1
                if i>len(self.t[0]):
                    self.t[0]=self.t[0][-2:]  
        self.t=tuple(self.t)
        return self
    def mayorabs(self,other):
        xm,ym= self.tratar(other);
        xm=xm[0]+xm[1];ym=ym[0]+ym[1];
        if xm==ym:
            return other
        else:
            t=0
            while t<len(ym):
                if xm[t]<ym[t]:
                    return other
                elif xm[t]>ym[t]:
                    return self
                else:
                    t+=1
    def __add__(self,other):
        vx=self.t[0][-1]
        vy=other.t[0][-1]
        if vx!=vy:
            if vx=="-":
                x=[0,0]; x[0]=self.t[0][:]; x[1]=self.t[1][:];
                x[0][-1]="+"
                return other-MyFloat(x)
            else: 
                y=[0,0]; y[0]=other.t[0][:]; y[1]=other.t[1][:];
                y[0][-1]="+"
                return self-MyFloat(y)
        
        x,y=self.tratar(other); d=[]; e=[]; r=0
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
        z= MyFloat((e+[vy],d))
        z.sin0aladerecha()
        z.sin0alaizquierda()
        return z
    def __sub__(self,other):
        vx=self.t[0][-1]
        vy=other.t[0][-1]
        if vx!=vy:
            if vx=="-": 
                y=[0,0]; y[0]=other.t[0][:]; y[1]=other.t[1][:];
                y[0][-1]="-"
                return MyFloat(y)+self
            else: 
                y=[0,0]; y[0]=other.t[0][:]; y[1]=other.t[1][:];
                y[0][-1]="+"
                return self+MyFloat(y)
        if not self==other.mayorabs(self): 
            y,x=self.tratar(other)
            if vy=="+": vx="-"
            else: vx="+"
        else: x,y=self.tratar(other); 
        x=x[0]+x[1]; ent=len(y[0]); y=y[0]+y[1]; r=[]
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
        z=MyFloat((e+[vx],d))
        z=z.sin0alaizquierda()
        z=z.sin0aladerecha()
        return z
    def __eq__(self,other):
        vx=self.t[0][-1]
        vy=other.t[0][-1]
        xm,ym=self.tratar(other)
        if xm==ym and vx==vy: 
            return True
        else:
            return False
    def __ne__(self,other):
        return not self==other
    def __truediv__(self,other,n=100):
        cero=MyFloat(([0,"+"],[]));
        if cero==other.mayorabs(cero): raise ZeroDivisionError
        if cero==self.mayorabs(cero): return cero
        vx=self.t[0][-1]
        vy=other.t[0][-1]
        vf="+" if vx==vy else "-" 
        self.sin0alaizquierda();other.sin0alaizquierda()
        self.sin0aladerecha();other.sin0aladerecha()
        [x,yr]=self.tratarsin0(other); 
        dx=len(x[1]) ;   dy=len(yr[1])
        yr=yr[0]+yr[1] ; x=x[0]+x[1] ; yr.reverse() ; x.reverse(); 
        dec0=dy-dx  ;   ly=len(yr) ; cociente=[]
        x=MyFloat([x+["+"],[]])  ;    r=x ;    y=MyFloat([yr+["+"],[]]); 
        from numpy import asarray as np
        yr=np(yr); diez=MyFloat(([0,1,"+"],[])) ; r1=1 ; j=0
        y10= y * diez
        while len(cociente)< n and not x==cero:
            if x!=y.mayorabs(x) and r1==0: 
                x.t=list(x.t); x.t[0]=[0]+x.t[0]; r=x; r1=1
            elif x==y10.mayorabs(x):
                x=x.t[0][-2::-1] ;  q=x[:ly] ;x=x[ly:] ;q=MyFloat([q[::-1]+["+"],[]]); 
                if y==y.mayorabs(q) and not q==y: 
                    q.t[0]=x[:1]+q.t[0];x=x[1:]; 
                while True:
                    if q!=y.mayorabs(q) and r1==0: 
                        if x==[]:
                            x=r; break
                        q.t[0]=x[:1]+q.t[0]; r=q;x=x[1:]; r1=1
                    else: 
                        i=0 ; j+=1
                        while i<10:
                            intento=yr*i;
                            intento=list(intento); 
                            intento=MyFloat((intento+["+"],[]));
                            intento=cero+intento;
                            r=q-intento;
                            if not r==y.mayorabs(r): break
                            i+=1
                        cociente+=[i]
                        q=r;r1=0
            else: 
                i=0 ; 
                if j==0: j=1
                while i<10:
                    intento=yr*i; 
                    intento=list(intento); 
                    intento=MyFloat((intento+["+"],[]))
                    intento=cero+intento;
                    r=x-intento; 
                    if not r==y.mayorabs(r):  break
                    i+=1
                cociente+=[i]; 
                x=r; r1=0
        com=dec0+j; 
        if com >= 0:e=cociente[:com];e.reverse(); cociente=e+[str(vf)[0]],cociente[com:]
        else: cociente=[0]+ [str(vf)[0]],[0]*abs(com)+cociente
        cociente=MyFloat(cociente)
        cociente.sin0alaizquierda()
        return cociente
    def __mul__(self,other):
        vx=self.t[0][-1]
        vy=other.t[0][-1]
        vf="+" if vx==vy else "-" 
        self.sin0alaizquierda();other.sin0alaizquierda()
        self.sin0aladerecha();other.sin0aladerecha()
        x,y=self.tratarsin0(other);
        d3=len(x[1]);d2=len(y[1]);x=x[0]+x[1];y=y[0]+y[1]
        lx=len(x) ; p=MyFloat(([0,"+"],[0]));d1=d2+d3; lt=lx+len(y); ent=lt-d1
        for i in range(lx):
            if x[-i-1]!=0:
                si=[]
                for j in range(len(y)):
                    si+=[y[j]*x[-i-1]]
                si=(lx-i)*[0]+si+[0]*i
                d=si[ent:]; 
                e=si[:ent];
                e=e[::-1];
                si=MyFloat((e+["+"],d));
                p=p+si; 
        l=p.t[0];l[-1]=vf
        p.sin0aladerecha()
        p.sin0alaizquierda()
        return p
    def __radd__(self,num):
        return self + MyFloat(num)
    def __rsub__(self,num):
        return self - MyFloat(num)
    def __rmul__(self,num):
        return self * MyFloat(num)
    def __rdiv__(self,num):
        return self / MyFloat(num)   
    def __repr__(self):
        num=""
        for i in range(2):
            for j in range(len(self.t[i])):
                if i==0: j=-j-1
                elif i==1 and j==0 and self.t[i]!=[]: num+="."
                num+=str(self.t[i][j])
        return num 
    def pi(x=10000):
        s=MyFloat(([0,"+"],[])) ; k=0 ; uno=MyFloat(([1,"+"],[])) ; 
        j=uno ; dos=MyFloat(([2,"+"],[]))
        for i in range(1,x):
            k=k%2 + 1 
            if k==1:
                j=j+dos;
                b=uno/j
                s=s-b; 
            else: 
                j=j+dos;
                b=uno/j
                s=s+b; 
        s=s+uno
        s=s*MyFloat(([4,"+"],[]))
        return s
    if __name__ == "__main__":
        print(pi())

y=MyFloat(([ 0,4, '+'], []))
x=MyFloat(([0,3, '+'],[]))
print(x);print(y,x)   



