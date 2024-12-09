

class Time:

    def __init__(self,hh=0,mm=0,ss=0):
        self.hh = hh
        self.mm = mm
        self.ss = ss 
   
    def __str__(self):  
        # 1, 2, 33 => 01:02:33      
        return '%02d:%02d:%02d' % (self.hh,self.mm,self.ss)

    def __add__(self, other):
        nuevo = Time(self.hh+other.hh,self.mm+other.mm, self.ss+other.ss)
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

class DateTime(Date, Time):
    pass

if __name__ =="__main__":
    t1 = Time(12,33,4)
    print(t1)
    t2 = Time(8,56,2)
    print(t2)
    suma = t1 + t2
    print(suma)