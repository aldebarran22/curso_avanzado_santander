
class Time:

    def __init__(self,hh=0,mm=0,ss=0):
        self.hh = hh
        self.mm = mm
        self.ss = ss 
   
    def __str__(self):  
        # 1, 2, 33 => 01:02:33      
        return '%02d:%02d:%02d' % (self.hh,self.mm,self.ss)
    
    def __add__(self, other):
        nuevo = Time(self.hh+other.hh,self.mm+other.mm,self.ss+other.ss)
        nuevo.__ajustar()
        return nuevo
    
    def __ajustar(self):
        minutos = self.ss // 60
        self.ss %= 60
        self.mm += minutos

        horas = self.mm // 60
        self.mm %= 60
        self.hh += horas
        
class Date:

    def __init__(self, dd,mm,yy):
        self.d = dd
        self.m = mm
        self.y = yy

    def __str__(self):
        return "%02d/%02d/%04d" % (self.d,self.m,self.y)

    def esBisiesto(self):
        anyo = self.y
        if  (anyo % 4 == 0 and anyo % 100 != 0) or (anyo%100 == 0 and anyo % 400 == 0):
            return True    
        else:
            return False 


class DateTime(Time, Date):          

    def __init__(self, d=1, m=1, y=1970, hh=0, mm=0, ss=0):
        Date.__init__(self, d, m, y)
        Time.__init__(self, hh, mm, ss)

    def __str__(self):
        return Date.__str__(self) + " " + Time.__str__(self) 

if __name__=='__main__':
    t1 = Time(12,34,45)
    t2 = Time(5, 55, 34)
    suma = t1 + t2 # suma = t1.__add__(t2)
    print(t1)
    print(t2)
    print(suma)

    dt = DateTime(10,12,2024, 13,59,5)
    print(dt) # 10/12/2024 13:59:05
