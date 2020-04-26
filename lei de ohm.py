op = input("Digite qual lei de ohm voce deseja efetuar as contas: \n1 - Primeira Lei de Ohm (digite 1)\n2 - Segunda Lei de Ohm (digite 2)\n\n")

if op == "1":
    conta = input("Digite o valor que voce deseja encontrar: \nR - Resistencia\nV - Tensao\nI - Intensidade Corrente\nDigite a respectiva letra que voce deseja efetuar a conta: ")
    if conta.lower() == "r":
        v = int(input("Digite a tensao (volts): "))
        i = int(input("Digite a intensidade (amperes): "))
        r1 = v / i
        print("A resistencia ficou: ", int(r1))
    elif conta.lower() == "v":
        i = int(input("Digite a intensidade (amperes): "))
        r = int(input("Digite a resistencia (ohm): "))
        v = r * i
        print("A tensao calculada ficou: ", int(v))
    elif conta.lower() == "i":
        v = int(input("Digite a tensao (volts): "))
        r = int(input("Digite a resistencia (ohm): "))
        i = v / r
        print("A intensidade calculada ficou: ", int(i))
'''
l: m
p: ohm por m
a: mm2
'''
if op == "2":
    l = int(input("Digite o comprimento do fio: "))
    a = int(input("Digite a area transversal: "))
    p = int(input("Digite a resistividade do material: "))
    r2 = (p * l) / a
    print("A resistencia final ficou: ", int(r2))
