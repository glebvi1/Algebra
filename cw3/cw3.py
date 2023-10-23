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
        sqrt_r = self.r**0.5
        return Complex(sqrt_r * cos(radians(self.phi / 2)), sqrt_r * sin(radians(self.phi / 2)))

    def is_real(self):
        return self.b == 0

    def __str__(self):
        znak = "+" if self.b >= 0 else "-"
        return f"{self.a} {znak} {abs(self.b)}i"

    @staticmethod
    def __is_real_x(x):
        return isinstance(x, int) or isinstance(x, float)


def discriminant(p, q):
    D = p * p * p / 27 + q * q / 4
    print(f"\nD = p^3 / 27 + q^4 / 4 = {D} = {D.trigonom()}")
    print("Извлечем из D корень:")
    print(f"sqrt(D) = sqrt(|D|)(cos({D.phi}/2) + isin({D.phi}/2))")
    print(f"sqrt(D) = {D.sqrt().trigonom()} = {D.sqrt()}", end="\n\n")
    return D.sqrt()


def get_xi(a33: Complex, i):
    add_corner = 0 if i == 1 else 120
    corner = round(a33.phi / 3 + add_corner, 4)
    rcorner = radians(a33.phi / 3 + add_corner)
    ai = Complex(cos(rcorner), sin(rcorner)) * (a33.r ** (1 / 3))
    bi = Complex(cos(rcorner), -sin(rcorner)) * (-p) / (3 * ai.r)
    print(f"a{i} = cqrt(|a^3|)(cos({corner}) + isin({corner})) = {ai.trigonom()} = {ai}")
    print(f"b{i} = -p / (3*a{i}) = {-p} * ({bi.trigonom()}) / (3*{ai.r}) = {bi.trigonom()} = {bi}")
    print(f"z{i} = a{i} + b{i} = {ai + bi}", end="\n\n")
    return ai + bi


print("Введите коэффициенты p и q кубического уравнения z^3 + pz + q = 0")
print("Введите через пробел действительную и мнимую часть p:")
a, b = map(float, input().split())
p = Complex(a, b)
print("Введите через пробел действительную и мнимую часть q:")
a, b = map(float, input().split())
q = Complex(a, b)

D = discriminant(p, q)
a33 = -q/2 + D

print(f"a^3 = -q / 2 + sqrt(D) = ({-q / 2}) + ({D}) = {a33} = {a33.trigonom()}", end="\n\n")
x1 = get_xi(a33, 1)
x2 = get_xi(a33, 2)
print("Так как коэффициент перед z^2 равен 0, то по теореме Виета можно найти z3 = - z2 - z1")
print(f"x3 = {-x1 - x2}")
