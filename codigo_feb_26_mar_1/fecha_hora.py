class Time:

    def __init__(self, hh=0, mm=0, ss=0):
        self.h = hh
        self.m = mm
        self.s = ss

    def __add__(self, other):
        if not isinstance(other, Time):
            raise TypeError("Se requieren dos instancias de Time")
        else:
            nuevo = Time(self.h + other.h, self.m + other.m, self.s + other.s)
            nuevo.ajustar()
            return nuevo

    def ajustar(self):
        minutos = self.s // 60
        self.s %= 60
        self.m += minutos
        horas = self.m // 60
        self.m %= 60
        self.h += horas

    def __str__(self):
        return "%02d:%02d:%02d" % (self.h, self.m, self.s)


class Date:

    def __init__(self, dd, mm, yy):
        self.dd = dd
        self.mm = mm
        self.yy = yy

    def __str__(self):
        return "%02d/%02d/%04d" % (self.dd, self.mm, self.yy)

    def esBisiesto(self):
        anyo = self.yy
        if (anyo % 4 == 0 and anyo % 100 != 0) or (anyo % 100 == 0 and anyo % 400 == 0):
            return True
        else:
            return False


class DateTime(Date, Time):

    def __init__(self, d=1, m=1, y=1970, hh=0, mm=0, ss=0):
        Date.__init__(self, d, m, y)
        Time.__init__(self, hh, mm, ss)

    def __str__(self):
        return Date.__str__(self) + " " + Time.__str__(self)


if __name__ == "__main__":
    t = Time(1, 2, 44)
    print(t)

    t2 = Time(10, 12, 34)
    print(t2)

    try:
        resul = "03:07:10" + t  # error en str
    except Exception as e:
        print(e.__class__.__name__, e)

    try:
        resul = t + "03:07:10"  # error en Time
        print(resul)
    except Exception as e:
        print(e.__class__.__name__, e)

    dt = DateTime(1, 5, 2024, 1, 2, 44)  # 01/05/2024 01:02:44
    print(dt)
