Algoritmo sin_titulo
	Definir numHamb, Pan, Carne, pollo, PolloDesmechado, Tocineta, PapaFrita, Bebidas Como Entero
	Definir totalPagar, Subtotal, Servicio Como Real
	Escribir 'Bienvenido a Custom Rappid'
	Escribir 'Por favor eliga cuantas hamburguesas quieres comprar: '
	Subtotal <- 0
	Leer numHamb
	Para i<-1 Hasta numHamb Con Paso 1 Hacer
		Escribir 'Tipo de pan'
		Escribir '1) Avena     $1000'
		Escribir '2) Centeno   $1500'
		Leer Pan
		Si Pan==1 Entonces
			Subtotal <- Subtotal+1000
		SiNo
			Subtotal <- Subtotal+1500
		FinSi
		Escribir 'Carne'
		Escribir '1) 250G    $5000'
		Escribir '2) 350G    $7000'
		Leer Carne
		Si Carne==1 Entonces
			Subtotal <- Subtotal+5000
		SiNo
			Subtotal <- Subtotal+7000
		FinSi
		Escribir 'Pollo'
		Escribir '1) 250G    $4500'
		Escribir '2) 350G    $5500'
		Leer Pan
		Si pollo==1 Entonces
			Subtotal <- Subtotal+4500
		SiNo
			Subtotal <- Subtotal+5500
		FinSi
		Escribir 'Pollo desmechado'
		Escribir '1) 250G    $5000'
		Escribir '2) 350G    $7000'
		Leer Carne
		Si PolloDesmechado==1 Entonces
			Subtotal <- Subtotal+6500
		SiNo
			Subtotal <- Subtotal+7500
		FinSi
		Escribir 'Tocineta'
		Escribir '1) lonja de tocineta    $1500'
		Escribir '2) lonjas de tocineta   $2500'
		Leer Carne
		Si Tocineta==1 Entonces
			Subtotal <- Subtotal+1500
		SiNo
			Subtotal <- Subtotal+2500
		FinSi
		Escribir 'PapaFrita'
		Escribir '1) Francesas    $5000'
		Escribir '2) Cascos       $6000'
		Leer Carne
		Si PapaFrita==1 Entonces
			Subtotal <- Subtotal+5000
		SiNo
			Subtotal <- Subtotal+6500
		FinSi
		Escribir 'Bebidas UwU'
		Escribir 'Gaseosa     $5000'
		Escribir 'Cervezas    $8000'
		Escribir 'Naranjada   $9000'
		Leer Bebidas
		Según Bebidas Hacer
			1:
				Subtotal <- Subtotal+5000
			2:
				Subtotal <- Subtotal+8000
			3:
				Subtotal <- Subtotal+9000
		FinSegún
		
		Servicio <- Subtotal * 0.10
		totalPagar <- Subtotal + Servicio
		Escribir "el total a pagar es ", Subtotal
		Escribir "Mas el servicio es un adicional de: ", Servicio
		Escribir "El subtotal: ", Subtotal " Mas el Servicio: ", Servicio " Es un total de: ", totalPagar
	FinPara
FinAlgoritmo
