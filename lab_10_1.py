class Number:
    def __init__(self, a=0):
        self.a=a
    def get_sum(self):
        suma=0
        b=self.a
        for i in range(len(str(self.a))):
            suma+=b%10
            b=b//10
        return suma
    def get_len(self):
        return len(str(self.a))
    #метод для вводу значень з клавіатури
    def input_properties_from_kbd(self):
        self.a=int(input('a='))
    def __str__(self):
        return 'Number (a={0})'.format(self.a)

num1=Number()
num1.input_properties_from_kbd()
print(num1)
