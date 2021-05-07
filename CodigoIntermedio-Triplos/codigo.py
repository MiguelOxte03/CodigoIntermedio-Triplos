import re

print("Jose Isaac Che Teh")
print("Gaspar Melchor Caamal Aban")
print("Miguel Aurelio Oxte Tzuc")
print("Jesus Reyes Tuz Acosta")
print("==================================================================")
print("Posibles Entradas")
print("OJO: INTRODUCIR LAS EXPRESION COMO EN LOS EJEMPLOS, RESPETANDO ESPACIOS")
print("EJEMPLO  2 + 5 * y")
print("EJEMPLO  a / a + b * b")
print("EJEMPLO  (a + 2) / 3 + b")
print("EJEMPLO  (a + 2) / (3 - b)")
print("EJEMPLO  2 * y - ((4 * y) + z)")
#sOLO ACEPTA NUMEROS DE UN DIGITO
expresion=str(input("Ingrese la expresion: X = "))
#Analiza la expresion para hacer el caso segun la entrada
#Para entradas de 2 simbolos aritmeticos con diferente prioridad
opcion1 = len(re.findall("[\d|\w]\s([\+|\-|\*|/])\s[\d|\w]\s([\+|\-|\*|/])\s[\d|\w]", expresion))
if opcion1 == 1:
    x=1
#Para entradas de 3 simbolos aritmeticos con diferente prioridad
opcion2 = len(re.findall("[\d|\w]\s([\+|\-|\*|/])\s[\d|\w]\s([\+|\-|\*|/])\s[\d|\w]\s([\+|\-|\*|/])\s[\d|\w]", expresion))
if opcion2 == 1:
    x=2
#Para entradas de 2 simbolos aritmeticos con parentesis
opcion3 = len(re.findall("\([\w|\d]\s([\+|\-|\*|/])\s[\d|\w]\)", expresion))
if opcion3 == 1:
    x=3
#Para entradas de 3 simbolos aritmeticos con parentesis
opcion4 = len(re.findall("\([\w|\d]\s[\+|\-|\*|\/]\s[\w|\d]\)\s[\+|\-|\*|\/]\s\([\w|\d]\s[\+|\-|\*|\/]\s[\w|\d]\)", expresion))
if opcion4 == 1:
    x=4
#Al menos 2 simbolos aritmeticos con anidamiento de parentesis
opcion5 = len(re.findall("[\w|\d]\s[\+|\-|\*|\/]\s[\w|\d]\s[\+|\-|\*|\/]\s\(\([\w|\d]\s[\+|\-|\*|\/]\s[\w|\d]\)\s[\+|\-|\*|\/]\s[\w|\d]\)", expresion))
if opcion5 == 1:
    x=5

if x==1:
    p = []
    vs = []
    valor =expresion
    suma = -1
    for i in valor:
        if i != " ":
            p.append(i)
    temporalCero = ""
    for i in p: # MULTIPLICACION O DIVISION
        suma +=1
        if i =="*" or i=="/":
            #STRING TEMPORAL CERO
            # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
            temporalCero = "_t0 = " + p[suma-1] + " " +  p[suma] + " " + p[suma+1]  #LA LISTA P VAN DESGLOZANDO LA EXPRESION EN PARTES
            p.remove(p[suma])
            p.remove(p[suma-1])
            p.remove(p[suma-1])
    print(temporalCero)
    temporalUno = ""
    for i in p:
        if i == "+" or i == "-": # SUMA O RESTA
            if p[-1] == "+" or p[-1]=="-":
                temporalUno = "_t1 ="+ p[0] + " "+ p[-1] + " " +"_t0"
                
            else:
                temporalUno = "_t1 = "+ p[-1] + " "+ p[-2] + " " +"_t0"
    print(temporalUno)
#=====================================================================================================
elif x==2:
    p = []
    vs = []
    valor =expresion
    suma = -1
    for i in valor:
        if i != " ":
            p.append(i)
    temporalCero = ""
    for i in p: # MULTIPLICACION O DIVISION
        suma +=1
        if i =="*" or i=="/":
            #STRING TEMPORAL CERO
            # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
            temporalCero = "_t0 = " + p[suma-1] + " " +  p[suma] + " " + p[suma+1] 
            p.remove(p[suma-1])
            p.remove(p[suma])
            p.remove(p[suma-1])
            break  
    print(temporalCero)

    #======================================================================================================
   
    temporalUno = ""
    for i in p: # MULTIPLICACION O DIVISION
        if p[3] =="+":
            if p[suma-4]=="/" or p[suma-4]=="*":
                 temporalUno = "_t1 = " + p[suma-5] + " " +  p[suma-4] + " " + p[suma-3] 
            elif p[suma-4]  != "/" or p[suma-4] !="*":
                if p[suma-4] == "+" or p[suma-4]=="-":
                    temporalUno = "_t1 = " + p[suma-3] + " " +  p[suma-2] + "_t0"
        elif p[3] !="+":
            if p[suma+1]=="/" or p[suma+1]=="*":
                #STRING TEMPORAL CERO
                # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
                temporalUno = "_t1 = " + p[suma] + " " +  p[suma+1] + " " + p[suma+2]   
            elif p[suma+1]  != "/" or p[suma+1] !="*":
                if p[suma+1] == "+" or p[suma+1]=="-":
                    temporalUno = "_t1 = _t0 " + p[suma-1] + " " +  p[suma]
    
    print(temporalUno)

    #==========================================================================

    temporalDos = ""
    for i in p: # MULTIPLICACION O DIVISION
        if p[3] =="+":
            if p[suma-4]=="/" or p[suma-4]=="*":
                 temporalDos = "_t2 = " + temporalCero[0:3] + " " +  p[suma-4] + " " + temporalUno[0:3]
            elif p[suma-4]  != "/" or p[suma-4] !="*":
                if p[suma-4] == "+" or p[suma-4]=="-":
                    temporalDos = "_t2 = " + p[suma-5] + " " +  p[suma-4] + "_t1"
        elif p[3] !="+":
            if p[suma+1]=="/" or p[suma+1]=="*":
                #STRING TEMPORAL CERO
                # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
                temporalDos = "_t2 = " + temporalCero[0:3] + " " +  p[suma-1] + " " + temporalUno[0:3]  
            elif p[suma+1]  != "/" or p[suma+1] !="*":
                if p[suma+1] == "+" or p[suma+1]=="-":
                    temporalDos = "_t1 = _t0 " + p[suma+1] + " " +  p[suma+2]
    print(temporalDos)
elif x==3:
    p = []
    vs = []
    valor =expresion
    suma = -1
    for i in valor:
        if i != " ":
            p.append(i)

    #=============================================================================
    temporalCero = ""
    for i in p: 
        suma +=1
        if i =="(" or i == ")":
            #STRING TEMPORAL CERO
            # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
            temporalCero = "_t0 = " + p[suma-4] + " " +  p[suma-3] + " " + p[suma-2] + " " + p[suma-1] + " " + p[suma]
            
    #===========================================================================================
    temporalUno = ""
    for i in p:
        if i == "*" or i == "/":
            if p[4] == "(" :
                temporalUno = "_t1 ="+ " _t0 " + p[suma-5] + " " +  p[suma-6] + " " 
            else:
                temporalUno = "_t1 = " + p[suma-2] + " " +  p[suma-3] + " " +  "_t0"
    #================================================================================================
    temporalDos = ""
    for i in p:
        if i == "+" or i == "-": 
            if p[4] == "(" :
                temporalDos = "_t2="+ " _t1 " + p[suma-7] + " " +  p[suma-8] + " " 
            else:
                temporalDos = "_t2 = " + p[suma] + " " +  p[suma-1] + " " +  "_t1"
    print(temporalCero)
    print(temporalUno)
    print(temporalDos)
   
#===========================================================================================================
#===========================================================================================================
elif x==4:
    p = []
    vs = []
    valor =expresion
    suma = -1
    for i in valor:
        if i != " ":
            p.append(i)
    temporalCero = ""
    for i in p: # MULTIPLICACION O DIVISION
        suma +=1
        if i =="*" or i=="/":
            #STRING TEMPORAL CERO
            # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
            temporalCero = "_t0 = " + p[suma-2] + " " + p[suma-1] + " " +  p[suma] + " " + p[suma+1] + " " + p[suma+2] 
            p.remove(p[suma-1])
            p.remove(p[suma])
            p.remove(p[suma-1])
            break 
        else: 
                if i == "+" or i=="-":
                    temporalCero = "_t0 = " + p[suma-2] + " " + p[suma-1] + " " +  p[suma] + " " + p[suma+1] + " " + p[suma+2]
                    p.remove(p[suma-1])
                    p.remove(p[suma])
                    p.remove(p[suma-1])
                    break      
    print(temporalCero)

#============================================================================================================================
    temporalUno = ""
    for i in p: # MULTIPLICACION O DIVISION
        suma +=1
        if i =="*" or i=="/":
            #STRING TEMPORAL CERO
            # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
            try:
                temporalUno = "_t1 = " + p[suma-2] + " " + p[suma-1] + " " +  p[suma] + " " + p[suma+1] + " " + p[suma+2] 
                p.remove(p[suma-1])
                p.remove(p[suma])
                p.remove(p[suma-1])
            except:
                IndexError: temporalUno = 'null'
                print("===============================================================================")
                print("ERROR")
                print("caso invalido")
                print("===============================================================================")
            break 
        else: 
                if i == "+" or i=="-":
                        try:
                            temporalUno = "_t1 = " + p[suma-2] + " " + p[suma-1] + " " +  p[suma] + " " + p[suma+1] + " " + p[suma+2] 
                            p.remove(p[suma-1])
                            p.remove(p[suma])
                            p.remove(p[suma-1])
                        except:
                            IndexError: temporalUno = 'null'
                            print("===============================================================================")
                            print("ERROR")
                            print("caso invalido")
                            print("===============================================================================")
                        break
    print(temporalUno)

#=========================================================================================================================================
    temporalDos = ""
    for i in p: # MULTIPLICACION O DIVISION
        suma +=1
        if i =="*" or i=="/":
            #STRING TEMPORAL CERO
            # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
            temporalDos = "_t2 = " + temporalCero[0:3] + " " +  p[suma-6] + " " + temporalUno[0:3]
            break 
        else: 
                if i == "+" or i=="-":
                    temporalDos = "_t2 = " + temporalCero[0:3] + " " +  p[suma-6] + " " + temporalUno[0:3]
                    break      
    print(temporalDos)

elif x==5:
    p = []
    S = []
    TC= []
    valor =expresion
    suma = -1
    suma2 = -1
    for i in valor:
        if i != " ":
            p.append(i)

    #=============================================================================
    for i in p: 
        suma +=1
        if i =="(" or i ==")":
            if i =="(" or i ==")":
                p.remove(p[suma-13])
                TC.append(p[suma-12])
                p.remove(p[suma-12])
                TC.append(p[suma-11])
                p.remove(p[suma-11])
                TC.append(p[suma-10])
                p.remove(p[suma-10])
                TC.append(p[suma-9])
                p.remove(p[suma-9])
                TC.append(p[suma-8])
                p.remove(p[suma-8])
                TC.append(p[suma-7])
                p.remove(p[suma-7])
                TC.append(p[suma-6])
                p.remove(p[suma-6])
                p.remove(p[suma-5])
                #TC = p[suma-12] + " " + p[suma-11] + " " + p[suma-10] + " " + p[suma-9] + " " + p[suma-8] + " " +  p[suma-7] + " " + p[suma-6]
                break
    #================================================================================
    #print(p)
    #print(TC)
    #print(S)


    temporalCero = ""
    for x in TC: 
        suma +=1
        if x =="(" or x ==")":
            if TC[0]=="(":
                temporalCero = "_t0 = " + TC[suma2-6] + " " +  TC[suma2-5] + " " + TC[suma2-4] + " " + TC[suma2-3] + " " + TC[suma2-2]
                #temporalCero = "_t0 = " + TC[suma2-4] + " " +  TC[suma2-3] + " " + TC[suma2-2] + " " + TC[suma2-1] + " " + TC[suma2]
            else:
                temporalCero = "_t0 = " + TC[suma2-4] + " " +  TC[suma2-3] + " " + TC[suma2-2] + " " + TC[suma2-1] + " " + TC[suma2]
    print(temporalCero)
    #=====================================================================================================
    temporalUno = ""
    for x in TC: 
        suma2 +=1
        if x =="+" or x =="-" or x =="*" or x =="/":
            if TC[0]=="(":
                temporalUno = "_t1 = t0 "  + TC[suma2-7] + " " +  TC[suma2-6]  
            else:
                temporalUno = "_t1 = t0 "  + TC[suma2-3] + " " +  TC[suma2-4]    

            #temporalCero = "_t1 = " + TC[suma-8] + " " +  TC[suma-7] + " " +  TC[suma-6] + " " +  TC[suma-5] + " " +  TC[suma-4]    
    print(temporalUno)
    #============================================================================================
    temporalDos = ""
    for i in p: 
        suma +=1
        if p[0]=="-" or p[0]=="+" or p[0]=="*" or p[0]=="/":
            temporalDos = "_t2 = " + p[1] +  " " + p[2] + " " + p[3]  
            break
        else:
            if p[3]=="*" or p[3]=="/" or p[3]=="+" or p[3]=="-":
                if p[2] =="*" or p[2]=="/" or p[2]=="+" or p[2]=="-":
                    temporalDos = "_t2 = " + " " +p[0]  + " " + p[3] + " " + p[1] 
                else:
                    temporalDos = "_t2 = " + " " +p[0]  + " " + p[1] + " " + p[2]
                #temporalCero = "_t1 = " + TC[suma-8] + " " +  TC[suma-7] + " " +  TC[suma-6] + " " +  TC[suma-5] + " " +  TC[suma-4]    
    print(temporalDos)

    temporalTres = ""
    for i in p: 
        suma +=1
        if p[0]=="-" or p[0]=="+" or p[0]=="*" or p[0]=="/":
            temporalTres = "_t3 = " + temporalUno[0:3] +  " " + p[0] + " " + temporalDos[0:3]
            break
        else:
            if p[2] =="*" or p[2]=="/" or p[2]=="+" or p[2]=="-":
                temporalTres = "_t3 = " + temporalUno[0:3] +  " " + p[2] + " " + temporalDos[0:3]
                break
            else:
                temporalTres = "_t3 = " + temporalUno[0:3] +  " " + p[3] + " " + temporalDos[0:3]
                break
                #temporalCero = "_t1 = " + TC[suma-8] + " " +  TC[suma-7] + " " +  TC[suma-6] + " " +  TC[suma-5] + " " +  TC[suma-4]    
    print(temporalTres)
