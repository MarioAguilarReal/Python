def compare(string1, string2):  
    if len(string1) == len(string2):
        x=list(map(str,string1))
        y=list(map(str,string2))
        x.sort()
        y.sort()
        if x == y:
            return True

def inString():
    string1 = input("ingresa el primer string:").upper().replace(" ", "")
    string2 = input("Ingresa el segundo string: ").upper().replace(" ", "")
    print(compare(string1, string2))

print("Elige la opcion")
op = 1
while op != 0:
    op = int(input("opcion:\n1: usar programa\n2: salir\n->"))
    match op:
        case 1:
            inString()
        case 2:
            op=0