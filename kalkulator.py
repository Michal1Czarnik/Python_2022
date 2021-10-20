#!/usr/bin/python3

class liczbyZespolone:
    def __init__(self, re, im):
        self.re = re
        self.im = im
    def __addition__(self, number):
        return liczbyZespolone(self.re + number.re, self.im + number.im)
    def __substraction__(self, number):
        return liczbyZespolone(self.re - number.re, self.im - number.im)
    def __multiplication__(self, number):
        return liczbyZespolone(self.re * number.re, self.im * number.im)
    def __division__(self, number):
        return liczbyZespolone(self.re / number.re, self.im / number.im)
    def __format__(self):
        if (self.im >= 0):
            print("{}+{}i".format(self.re, self.im))
        else:
            print("{}-{}i".format(self.re, abs(self.im)))
if __name__ == '__main__':
    print("Czesc rzeczywista pierwszej liczby: ")
    num1re = input()
    print("\nCzesc urojona pierwszej liczby: ")
    num1im = input()
    print("\nCzesc rzeczywista drugiej liczby: ")
    num2re = input()
    print("\nCzesc urojona druhgiej liczby: ")
    num2im = input()
    print("\nDzialanie (+ - * /)")
    sign = input()
    num1 = liczbyZespolone(int(num1re), int(num1im))
    num2 = liczbyZespolone(int(num2re), int(num2im))
    print("\nWynik:")
    if (sign == '+'):
        liczbyZespolone.__addition__(num1, num2).__format__()
    elif (sign == '-'):
        liczbyZespolone.__substraction__(num1, num2).__format__()
    elif (sign == '*'):
        liczbyZespolone.__multiplication__(num1, num2).__format__()
    elif (sign == '/'):
        liczbyZespolone.__division__(num1, num2).__format__()