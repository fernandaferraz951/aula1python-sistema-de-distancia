vTempo = int(input("Informe o tempo gasto do percurso (horas): "))
vMedia = float(input( "Velocidade média durante a viagem (Km/HR): "))

vdistancia = float(vTempo * vMedia)
vlitros = float(vdistancia/12)
vvalor = float(vlitros*3.50)

print("Velocidade Média :", vMedia, "KM/H")
print("Tempo gasto no percurso :", vTempo, "HRS")
print("Distancia Percorrida" , vdistancia, "KM")
print("Quantidade de litros de combustivel gastos: ", vlitros, "Litros")
print("Valor total gasto em combustivel:" , vvalor,)
if vTempo>2:
    print("é necessário realizar uma parada a cada 02 horas para descanso de pelo menos 10 minutos")

else: print("Pode Seguir direto sem paradas para seu destino")
(exit)

print("Boa Viagem")