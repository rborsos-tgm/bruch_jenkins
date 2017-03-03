'''
Created for SEW
A02 - TDD with Python

@author: Borsos Robert
@date: 23.10.2016
@version: 1.0.0
'''
from __future__ import division, print_function, unicode_literals


class Bruch(object):
    """
    Bruch Class

    :param int nenner: denominator
    :param int zaehler: numerator
    :ivar int nenner: denominator
    :ivar int zaehler: numerator
    """

    def __iter__(self):
        """
        make class iterable
        """
        return (self.zaehler, self.nenner).__iter__()

    def __init__(self, zaehler=0, nenner=1):
        """
        constructor for Bruch Class with zaehler=0 und nenner=1

        :raise TypeError: Incompatible types if zaehler or nenner is not int
        :param zaehler: Bruch or int
        :param nenner: int - not zero
        """
        if isinstance(zaehler, Bruch):
            self.zaehler, self.nenner = zaehler
            return
        elif type(zaehler) is not int:
            raise TypeError('Incompatible type ' + type(zaehler).__name__)
        elif type(nenner) is not int:
            raise TypeError('Incompatible type ' + type(nenner).__name__)
        if nenner == 0:
            raise ZeroDivisionError
        self.zaehler = zaehler
        self.nenner = nenner


    def __float__(self):
        """
        Overrides float() Method
        zaehler/nenner

        :return: float
        """
        return self.zaehler/self.nenner


    def __int__(self):
        """
        Overrides int() Method
        zaehler/nenner

        :return: int
        """
        return int(self.__float__())


    def __neg__(self):
        """
        Negation Method
        calls Bruch with negated zaehler

        :return: Bruch
        """
        return Bruch(-self.zaehler, self.nenner)

    def __radd__(self, zaehler):
        """
        Right one of add Method

        :raise TypeError: incompatible types
        :param zaehler: int or Bruch
        :return: Bruch
        """
        return self.__add__(zaehler)

    def __add__(self, zaehler):
        """
        Add Method

        :raise TypeError: incompatible types
        :param zaehler: int or Bruch
        :return: Bruch
        """
        if isinstance(zaehler, Bruch):
            z2, n2 = zaehler
        elif type(zaehler) is int:
            z2, n2 = zaehler, 1
        else:
            raise TypeError('incompatible types:' + type(zaehler).__name__ + ' + Bruch()')
        nennerNeu = self.nenner * n2
        zaehlerNeu = z2 * self.nenner + n2 * self.zaehler
        return Bruch(zaehlerNeu, nennerNeu)

    def __complex__(self):
        """
        overrides comPlex() MEthod
        Complex Math i, j

        :return: complex
        """
        return complex(self.__float__())

    def __rsub__(self, left):
        """
        Right one of sub MEthod

        :raise TypeError: incompatible types
        :param zaehler: int or Bruch
        :return: Bruch
        """
        if type(left) is int:
            z2 = left
            nennerNeu = self.nenner
            zaehlerNeu = z2 * self.nenner - self.zaehler
            return Bruch(zaehlerNeu, nennerNeu)
        else:
            raise TypeError('incompatible types:' + type(left).__name__ + ' - Bruch()')

    def __sub__(self, zaehler):
        """
        sub Method for substraction

        :raise TypeError: incompatible types
        :param zaehler: int or Bruch
        :return: Bruch
        """
        return self.__add__(zaehler * -1)

    def __rmul__(self, zaehler):
        """
        right one of mul Method for multiply

        :raise TypeError: incompatible types
        :param zaehler: int or Bruch
        :return: Bruch
        """
        return self.__mul__(zaehler)

    def __mul__(self, zaehler):
        """
        mul Method for multiply

        :raise TypeError: incompatible types
        :param zaehler: int or Bruch
        :return: Bruch
        """
        if isinstance(zaehler, Bruch):
            z2, n2 = zaehler
        elif type(zaehler) is int:
            z2, n2 = zaehler, 1
        else:
            raise TypeError('incompatible types:' + type(zaehler).__name__ + ' * Bruch()')
        z2 *= self.zaehler
        n2 *= self.nenner
        return Bruch(z2, n2)

    def __pow__(self, p):
        """
        Bruch power for "quadrieren"

        :raise TypeError: incompatible types
        :param int p: power
        :return: Bruch
        """
        if type(p) is int:
            return Bruch(self.zaehler ** p, self.nenner ** p)
        else:
            raise TypeError('incompatible types:' + type(p).__name__ + ' is not int')

    def __rdiv__(self, any):
        """
        right one of division method
        made for python compatibility with 2.x

        :param zaehler: int or Bruch
        :return: Bruch
        """
        return self.__rtruediv__(any)

    def __rtruediv__(self, left):
        """
        right one of division method
        made for python compatibility with 3.x

        :raise TypeError: incompatible types
        :param zaehler: int or Bruch
        :return: Bruch
        """
        if type(left) is int:
            z2 = left * self.nenner
            if self.zaehler == 0:
                raise ZeroDivisionError
            return Bruch(z2, self.zaehler)
        else:
            raise TypeError('incompatible types:' + type(left).__name__ + ' / Bruch()')

    def __div__(self, any):
        """
        division method
        made for python compatibility with 2.x

        :param any: int or Bruch
        :return: Bruch
        """
        return self.__truediv__(any)

    def __truediv__(self, zaehler):
        """
        division method
        made for python compatibility with 3.x

        :raise TypeError: incompatible types
        :param zaehler: Bruch or int
        :return: Bruch
        """
        if isinstance(zaehler, Bruch):
            z2, n2 = zaehler
        elif type(zaehler) is int:
            z2, n2 = zaehler, 1
        else:
            raise TypeError('incompatible types:' + type(zaehler).__name__ + ' / Bruch()')
        if z2 == 0:
            raise ZeroDivisionError
        return self.__mul__(Bruch(n2, z2))

    def __invert__(self):
        """
        invert a Bruch

        :return: Bruch
        """
        return Bruch(self.nenner, self.zaehler)

    def __repr__(self):
        """
        Representation of the Bruch Object Method
        before output  result gets shortened

        :return: string representation
        """
        shorten = Bruch.gcd(self.zaehler, self.nenner)
        self.zaehler //= shorten
        self.nenner //= shorten

        if self.nenner < 0:
            self.nenner *= -1
            self.zaehler *= -1

        if self.nenner == 1:
            return "(%d)" % self.zaehler
        else:
            return "(%d/%d)" % (self.zaehler, self.nenner)

    def __makeBruch(any):
        """
        Make Bruch
        create a Bruch from int or return the reference

        :raise TypeError: incompatible types
        :param any: Bruch or int
        :return: Bruch
        """
        if isinstance(any, Bruch):
            return any
        elif type(any) is int:
            b = Bruch(any, 1)
            return b
        else:
            raise TypeError('incompatible types:' + type(any).__name__ + ' not int and Bruch')

    def __eq__(self, any):
        """
        equal to

        :param Bruch any: any Bruch
        :return: boolean
        """
        any = Bruch.__makeBruch(any)
        return self.zaehler * any.nenner == any.zaehler * self.nenner

    def __ne__(self, any):
        """
        not equal to

        :param Bruch any: any Bruch
        :return: boolean
        """
        return not self.__eq__(any)

    def __gt__(self, any):
        """
        greather than

        :param Bruch any: any Bruch
        :return: boolean
        """
        any = Bruch.__makeBruch(any)
        return self.zaehler * any.nenner > any.zaehler * self.nenner

    def __lt__(self, any):
        """
        lower than

        :param Bruch any: any Bruch
        :return: boolean
        """
        any = Bruch.__makeBruch(any)
        return self.zaehler * any.nenner < any.zaehler * self.nenner

    def __ge__(self, any):
        """
        greather or equal to

        :param Bruch any: any Bruch
        :return: boolean
        """
        any = Bruch.__makeBruch(any)
        return self.zaehler * any.nenner >= any.zaehler * self.nenner

    def __le__(self, any):
        """
        lower or equal to

        :param Bruch any: any Bruch
        :return: boolean
        """
        any = Bruch.__makeBruch(any)
        return self.zaehler * any.nenner <= any.zaehler * self.nenner

    def __abs__(self):
        """
        abs(Bruch)

        :return: positive Bruch
        """
        return Bruch(abs(self.zaehler), abs(self.nenner))

    def __iadd__(self, any):
        """
        intern add

        :param Bruch any: Bruch
        :return: self
        """
        any = Bruch.__makeBruch(any)
        self = self + any
        return self

    def __isub__(self, any):
        """
        intern sub

        :param Bruch any: Bruch
        :return: self
        """
        any = Bruch.__makeBruch(any)
        self = self - any
        return self

    def __imul__(self, any):
        """
        intern mul

        :param Bruch any: any Bruch
        :return: self
        """
        any = Bruch.__makeBruch(any)
        self = self * any
        return self

    def __itruediv__(self, any):
        """
        intern division
        made for python compatibility with 3.x

        :param Bruch any: any Bruch
        :return: self
        """
        any = Bruch.__makeBruch(any)
        self = self / any
        return self

    def __idiv__(self, any):
        """
        intern division
        made for python compatibility with 2.x

        :param Bruch any: any Bruch
        :return: self
        """
        return self.__itruediv__(any)

    @classmethod
    def gcd(cls, x, y):
        """
        euclid's algorithmus
        Am anfang mit abs() zu positiven Werten machen ("Betrag" berechnen)

        :param int x: value 1
        :param int y: value 2
        :return: greatest common divisor
        """
        x, y = abs(x), abs(y)
        if x < y: x, y = y, x
        # Berechnung des Ergebnisses
        while y != 0:
            x, y = y, x % y
        return x