"""
Ejemplo de sobrecarga de operadores aitméticos y poo múltiple
"""

class Time:

    def __init__(self,h=0,m=0,s=0):
        self.h = h
        self.m = m
        self.s = s

    def __str__(self):        
        return '%02d:%02d:%02d' % (self.h,self.m,self.s)

    def __add__(self, other):
        nuevo = Time(self.h+other.h, self.m+other.m, self.s+other.s)
        nuevo.__ajustar()
        return nuevo

    def __ajustar(self):
        minutos = self.s // 60
        self.s %= 60

        self.m += minutos        
        horas = self.m // 60
        self.m %= 60
        self.h += horas

        self.h %= 24


class Date:

    def __init__(self, dd,mm,yy):
        self.dd = dd
        self.mm = mm
        self.yy = yy

    def __str__(self):
        return "%02d/%02d/%04d" % (self.dd,self.mm,self.yy)

    def esBisiesto(self):
        anyo = self.yy    
        if  (anyo % 4 == 0 and anyo % 100 != 0) or (anyo%100 == 0 and anyo % 400 == 0):
            return True    
        else:
            return False

class DateTime(Time, Date):

    def __init__(self, d=1, m=1, y=1970, H=0, M=0, S=0):
        Date.__init__(self, d,m,y)
        Time.__init__(self, H,M,S )

    def __str__(self):
        return Date.__str__(self)+" "+Time.__str__(self)


class DateTime2:

    def __init__(self, d=1, m=1, y=1970, H=0, M=0, S=0):
        self.time = Time(H,M,S)
        self.date = Date(d,m,y)

    def __str__(self):
        return str(self.date)+" "+str(self.time)


if __name__=='__main__':
    t1 = Time(1,34,5)
    print(t1)

    t2 = Time(3,54,55)
    print(t2)

    suma = t1 + t2
    print(suma)

    dt = DateTime()
    print(dt)

    dt2 = DateTime2()
    print(dt2)

    # Las subclases de DateTime:
    L = Date.__subclasses__()
    print(L)