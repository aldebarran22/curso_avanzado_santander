

class Time:

    def __init__(self,h=0,m=0,s=0):
        self.h = h
        self.m = m
        self.s = s

   
   
    def __str__(self):        
        return '%02d:%02d:%02d' % (self.h,self.m,self.s)


   

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

 

