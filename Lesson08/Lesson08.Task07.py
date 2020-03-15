class ComplexNum:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        print_complex_number = f'{self.real} + {self.imag}j'
        return print_complex_number

    def __add__(self, other):
        return ComplexNum(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return ComplexNum(self.real * other.real - self.imag * other.imag,
                          self.real * other.imag + self.imag * other.real)


a = ComplexNum(4, 2)
b = ComplexNum(3, -1)

print(a+b)
print(4 + 2j + 3 - 1j)

print(a*b)
print((4 + 2j)*(3 - 1j))
