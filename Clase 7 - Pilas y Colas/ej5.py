#Dada una lista de expresiones aritméticas simples, escribe un programa que calcule el resultado de cada una. Las expresiones pueden contener operadores +, -, * y /, además de paréntesis ( y ). El programa debe utilizar una pila para llevar un registro de las operaciones pendientes y de los resultados parciales.

class Pila():
    def __init__(self):
        self.items=[]
        
    def vacia(self):
        return len(self.items)==0

    def apilar(self,elemento):
        self.items.append(elemento)
    
    def desapilar(self):
        return self.items.pop()
        
    def tope(self):
        return self.items[-1]
    
    def tamano(self):
        return len(self.items)
    
def aplicar(a, b, op):
    if op == '+':
        return b + a
    elif op == '-':
        return b - a
    elif op == '*':
        return b * a
    elif op == '/':
        return b / a

def calc(ec):
    operadores = Pila()
    operandos = Pila()
    i = 0
    while i < len(ec):
        c = ec[i]
        if c.isdigit():
            # números de varios dígitos o decimales
            num = ''
            while i < len(ec) and (ec[i].isdigit() or ec[i]=='.'):
                num += ec[i]
                i += 1
            operandos.apilar(float(num))
            continue
        elif c in "+-*/":
            while (not operadores.vacia() and operadores.tope() in "*/" and c in "+-"):
                op = operadores.desapilar()
                a = operandos.desapilar()
                b = operandos.desapilar()
                operandos.apilar(aplicar(a, b, op))
            operadores.apilar(c)
        elif c == '(':
            operadores.apilar(c)
        elif c == ')':
            while operadores.tope() != '(':
                op = operadores.desapilar()
                a = operandos.desapilar()
                b = operandos.desapilar()
                operandos.apilar(aplicar(a, b, op))
            operadores.desapilar()  # quitar '('
        i += 1

    while not operadores.vacia():
        op = operadores.desapilar()
        a = operandos.desapilar()
        b = operandos.desapilar()
        operandos.apilar(aplicar(a, b, op))

    return operandos.tope()
            
    
print(calc("4*(4/2)*5+3*5"))