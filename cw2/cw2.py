from math import cos, sin, acos, degrees, radians


def rd(x):
    return round(x, 4)


class Complex:
    def __init__(self, a, b=0.0):
        self.a = rd(a)
        self.b = rd(b)

        self.r = rd((a*a + b*b)**0.5)
        self.phi = rd(degrees(acos(self.a / self.r)))
        if b < 0:
            self.phi *= (-1)

    def __add__(self, other):
        """Сложение"""
        if Complex.__is_real_x(other):
            return Complex(self.a + other, self.b)
        elif isinstance(other, Complex):
            return Complex(self.a + other.a, self.b + other.b)
        raise TypeError("Add")

    def __sub__(self, other):
        """Вычитание"""
        return self + -other

    def __mul__(self, other):
        """Умножение"""
        if Complex.__is_real_x(other):
            return Complex(other * self.a, other * self.b)
        elif isinstance(other, Complex) and other.is_real():
            return Complex(other.a * self.a, other.a * self.b)
        elif isinstance(other, Complex):
            return Complex(self.a*other.a - self.b*other.b, self.a*other.b + self.b*other.a)
        raise TypeError("Mul")

    def __truediv__(self, other):
        """Деление"""
        if Complex.__is_real_x(other):
            return Complex(self.a / other, self.b / other)
        raise TypeError("Div")

    def __neg__(self):
        """Унарный минус"""
        return Complex(-self.a, -self.b)

    def sopr(self):
        """Сопряженное"""
        return Complex(self.a, -self.b)

    def trigonom(self):
        return f"{self.r}(cos({self.phi}) + isin({self.phi}))"

    def sqrt(self):
        if self.is_real():
            if self.a >= 0:
                return Complex(self.a ** 0.5)
            return Complex(0, abs(self.a) ** 0.5)
        raise TypeError("Sqrt")

    def is_real(self):
        return self.b == 0

    def __str__(self):
        znak = "+" if self.b >= 0 else "-"
        return f"{self.a} {znak} {abs(self.b)}i"

    @staticmethod
    def __is_real_x(x):
        return isinstance(x, int) or isinstance(x, float)


def positive_d(p, a33):
    a1: float = rd(a33.a ** (1/3))
    b1: float = rd(-p.a / (3*a1))
    print(f"a1 = cqrt(a^3) =", a1)
    print(f"b1 = -p / (3*a1) = {-p.a} / (3*{a1}) =", b1)
    print(f"x1 = a1 + b1 =", rd(a1+b1), end="\n\n")

    a2 = Complex(a1*cos(radians(120)), a1*sin(radians(120)))
    b2 = (-p * Complex(cos(radians(120)), sin(radians(120))).sopr()) / (3*a1)
    print(f"a2 = a1(cos(120) + isin(120)) = {a1}(-0.5 + sqrt(3)/2*i) =", a2)
    print(f"b2 = -p / (3*a2) = -p*(cos(120) - isin(120) / (3*a1) = "
          f"{-p.a}*(cos(120) - isin(120) / (3*{a1}) =", b2)
    print(f"x2 = a2 + b2 =", a2 + b2, end="\n\n")

    print(f"Корень x3 находим как сопряженный к x2")
    print("x3 =", (a2+b2).sopr())


def negative_d(p, a33):
    def x12(i):
        add_corner = 0 if i == 1 else 120
        corner = radians(a33.phi / 3 + add_corner)
        ai = Complex(r * cos(corner), r * sin(corner))
        bi = (-p * Complex(cos(corner), sin(corner)).sopr()) / (3*ai.r)

        print(f"a{i} = cqrt(|a^3|)(cos({a33.phi} / 3 + 120) "
              f"+ isin({a33.phi} / 3 + 120) =", ai)
        print(f"b{i} = -p / (3*a1) = -p * (cos({a33.phi} / 3 + 120) "
              f"+ isin({a33.phi} / 3 + 120) / (3*|a1|) =", bi)

        return ai + bi

    r = rd(a33.r ** (1 / 3))
    print(f"|a^3| = {a33.r}; cqrt(|a^3|) = {r}")
    x1 = x12(1)
    print(f"x1 = {x1}", end="\n\n")
    x2 = x12(2)
    print(f"x2 = {x2}", end="\n\n")

    print("Так как коэффициент перед x^2 равен 0, то по теореме Виета можно найти x3 = - x2 - x1")
    print(f"x3 = {-x1-x2}")


print("Введите через пробел коэффициенты p и q кубического уравнения x^3 + px + q = 0")
p, q = map(float, input().split())
p, q = Complex(p), Complex(q)
D = p*p*p / 27 + q*q / 4
a33 = -q/2 + D.sqrt()
print(f"D = p^3/27 + q^2/4 = {D}")
print(f"a^3 = -q/2 + sqrt(D) =", a33, "=", a33.trigonom())
if D.a > 0:
    print("Так как дискриминант положительный, то у уравнения будет 1R и 2C корня", end="\n\n")
    positive_d(p, a33)
else:
    print("Так как дискриминант неположительный, то у уравнения будет 3R корня")
    print("Это значит, что коэффициент перед i всегда 0. Если в программе это не так, то это погрешность, на которую не нужно обращать внимания)", end="\n\n")
    negative_d(p, a33)
