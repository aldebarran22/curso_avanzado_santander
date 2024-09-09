

class Time:

    def __init__(self,h=0,m=0,s=0):
        self.h = h
        self.m = m
        self.s = s

    def __str__(self):        
        return '%02d:%02d:%02d' % (self.h,self.m,self.s)
    
    def __add__(self,other):
        nuevo = Time(self.h+other.h,self.m+other.m,self.s+other.s)
        nuevo.ajustar()
        return nuevo
    
    def ajustar(self):
        minutos = self.s // 60
        self.s %= 60
        self.m += minutos

        horas = self.m // 60
        self.m %= 60

        self.h += horas

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


class DateTime(Date,Time):

    def __init__(self, dd=1, mm=1, yy=1970, h=0, m=0, s=0):
        Date.__init__(self,dd,mm,yy)
        Time.__init__(self,h,m,s)

    def __str__(self):
        return Date.__str__(self)+" "+Time.__str__(self)

if __name__ == '__main__':
    t1 = Time(12,3,56)
    t2 = Time(8,45,9)

    resul = t1 + t2 # resul = t1.__add__(t2)
    print(t1)
    print(t2)
    print(resul)

    fecha = Date(9,9,2024)
    print(fecha)

    
    dt = DateTime(9,9,2024, 12,28,10) 
    # 09/09/2024 12:28:10
    print("Datetime: ",dt)
    
