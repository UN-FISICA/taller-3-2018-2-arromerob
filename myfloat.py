class MyFloat:
    def __init__(self,t):
        self.t=t
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
        i=2
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
        z= MyFloat((e+[vf],d))
        z=z.sin0aladerecha()
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
            #print("son iguales")
            return True
        else:
            #print("no son iguales")
            return False

y=MyFloat(([4, 3, 4, 2, 1, '-'], [1, 2, 3, 4]))
x=MyFloat(([4, 2, 1, '+'], [2, 3, 4]))
print(x+y);print(y,x)
"""
    def __mul__(self,otro):
        return multiplicacion(self.t,otro.t)

    def __div__(self,otro):
        return division(self.t,otro.t)

    def __radd__(self,otro):
        return suma(self.t,tupla(otro))

    def __rsub__(self,otro):
        return resta(self.t,tupla(otro))

    def __rmul__(self,otro):
        return multiplicacion(self.t,tupla(otro))

    def __rdiv__(self,otro):
        return division(self.t,tupla(otro))

    def __repr__(self):
        return imprimir(self.t)

    def __ne__(self):
        return not comparacion(self,otro)"""

"""if __name__ == "__main__":
    # Escribir aca el codigo para calcular pi. Al finalizar el calculo solo
    # debe imprimir el valor de pi, sin otros textos ni nada
    print(imprimir(pi()))"""

