Algoritmo sin_titulo
	Definir N, i como entero
	Definir Nombre como Cadena
	Definir horasTrabajo, SueldoBruto, eps, pension, SueldoNeto Como Real
	Definir totalBruto, totalEPS, totalPension, totalNeto Como Real
	Definir promedioBruto, promedioNeto Como Real
	Definir nombreMayor, nombreMenor como cadena
	Definir mayorSueldo, menorSueldo Como Real
	
	totalBruto <- 0
	totalEPS <- 0
	totalPension <- 0
	mayorSueldo <- 0
	menorSueldo <- 0
	
	Escribir "ingrese la cantidad de Empleados"
	leer N
	
	Para i <-1 hasta N Hacer
		Escribir "empleado", i
		Escribir "nombre"
		Leer nombre
		Escribir "cuantas horas trabajaste?"
		leer horasTrabajo
		
		SueldoNeto <- horasTrabajo + 20000
		eps <- SueldoBruto * 0.04
		pension <- SueldoBruto * 0.04
		SueldoNeto <- SueldoBruto - eps - pension
		
		Escribir "El SueldoBruto es: "
		Escribir "el descuento de eps: $", eps
		Escribir "descuento de la pension: $", pension
		Escribir "Sueldo Neto $: ", SueldoNeto
		
		totalBruto <- totalBruto + SueldoBruto
		totalEPS <- totalEPS + eps
		totalPension <- totalPension + pension
		totalNeto <- totalNeto + SueldoNeto
		
		si SueldoNeto > mayorSueldo Entonces
			mayorSueldo <- SueldoNeto
			nombreMayor <- nombre
		FinSi
		
		promedioBruto <- totalBruto / N
		promedioNeto <- totalNeto / N
		
		Escribir "total sueldo bruto: $", totalBruto
		Escribir "total descuento eps $", totalEPS
		Escribir "total pension $", totalPension
		Escribir "total Sueldo Neto $", totalNeto
		Escribir "promedio de sueldo Bruto: $", promedioBruto
		Escribir "promedio sueldo Neto: $", promedioNeto
		Escribir "Empleado que mas gana: $", nombreMayor, " ($", nombreMayor, ")"
		Escribir "empleado que menos gana: $", nombreMenor, " ($", nombreMenor, ")"
	FinPara
FinAlgoritmo
