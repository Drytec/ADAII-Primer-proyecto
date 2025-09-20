from ADA_class import Materia, Estudiante

M1 = Materia("M1", 3)
M2 = Materia("M2", 4)
M3 = Materia("M3", 2)

M= [M1, M2, M3]
k= len(M)

E1 = Estudiante("e1", [("M1", 5), ("M2", 2), ("M3", 1)])
E2 = Estudiante("e2", [("M1", 4), ("M2", 1), ("M3", 3)])
E3 = Estudiante("e3", [("M2", 3), ("M3", 2)])
E4 = Estudiante("e4", [("M1", 2), ("M3", 3)])
E5 = Estudiante("e5", [("M1", 3), ("M2", 2), ("M3", 3)])
E=  [E1, E2, E3, E4, E5]
r= len(E)

def ponderacion(E, M, i):  # O(n log n)
    resultados = []
    for e in range(len(E)):
        for l in range(len(E[e].solicitudes)):
            if E[e].solicitudes[l][0] == M[i].codigo:
                materia = E[e].solicitudes[l][0]
                valor = E[e].solicitudes[l][1] / E[e].prioridadTotal()
                resultados.append((E[e].codigo, materia, valor))

    return sorted(resultados, key=lambda x: x[2], reverse=True)

def insatisfaccion(A,E,i): #O(n)
    D = E[i]
    a = set()
    insatisfaccionAcum = 0
    for j in range(len(A)):
        for l in range(len(E[i].solicitudes)):#Maximo 7
            if A[j][0] == E[i].codigo:
                a.add(A[j])
    for elem in a:
        insatisfaccionAcum += elem[1][1]
    difMaterias = 1 - (len(a)/len(E[i].solicitudes) )
    promInsatisfaccion= 1 - insatisfaccionAcum
    return difMaterias * promInsatisfaccion


def rocV(k,r,E,M): #Complejidad Total = O(N^2) el log de n se desprecia
    A=[]
    i=0
    insatisfaccionTotal=0
    while i < k:
        if M[i].cupo > 0:
            a = ponderacion(E,M,i) #O(n log n)
            for j in range(len(a)):#O(n log n)
                A.append((a[0][0],(a[0][1],a[0][2])))
                M[i].restarCupo()
                a.pop(0)
                if M[i].cupo == 0:
                    break
        else:
            i+=1
    print(A)
    for h in range(0,r): #O(n^2), O(n)*r
        insatisfaccionTotal += insatisfaccion(A,E,h)
    return insatisfaccionTotal/r

z = rocV(k,r,E,M)
print(z)
