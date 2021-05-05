#peso
peso = input('¿Cual es tu peso (kg))?')
peso = float (peso)

#estatura
estatura = input('¿Cual es tu estatura (m))?')
estatura = float (estatura)

#imc = peso/ estatura*estatura
imc = round (peso / (estatura*estatura), 2)

print ("Tu indice de masa corporal es" , imc)

