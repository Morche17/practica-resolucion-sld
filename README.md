# Práctica de Resolución SLD con Python

- Autor: Emanuel Alejandro Tavares Medina
- Equipo: LegalMente (temática *legal*)

### Resumen
Este programa trata de realizar una práctica de Resolución SLD a través del lenguaje python, o lo que es lo mismo, hacer un motor de inferencia capaz de simular un sistema experto que pueda responder a consultas a través de cláusulas de horn, con el respaldo de una base del conocimiento ya establecida.

## Base del Conocimiento
Dentro del fichero `knowledge_base_pasaporte.py` se encuentra contenida dentro tuplas la base del conocimiento, esta se compone de los hechos y reglas utilizadas en la práctica. En este caso, son hechos y reglas en el contexto del **trámite de un pasaporte**.

### Hechos (afirmaciones indiscutibles)
* El pasaporte con vigencia de un año, solamente se expide a menores de 3 años.
* Los adultos mayores de 60 años, personas con discapacidad y trabajadores agrícolas (con Canadá) dispondrán del 50% de descuento del costo final del trámite.
* El costo del pasaporte de 1 año es de $885 mxn.
* El costo del pasaporte de 3 años es de $1730 mxn.
* El costo del pasaporte de 6 años es de $2350 mxn.
* El costo del pasaporte de 10 años es de $4120 mxn.
* La vigencia de 10 años de pasaporte no aplica para trabajadores agrícolas.
* Las personas con discapacidad deberán comprobar que cuentan con dicha discapacidad para aplicar al descuento del precio del trámite del pasaporte.
* El pago del pasaporte se puede realizar en las oficinas consulares o en los bancos autorizados.
* El trámite de pasaporte solamente puede realizarse de manera presencial.
* El trámite de pasaporte para menores de edad sólo puede realizarlo la o las persona que ejerzan la patria potestad o tutela del menor y bajo su autorización.
* Los bancos autorizados para el pago del pasaporte son banjército, banorte, bbva, banamex, banbajío, hsbc, santander, scotiabank, tesorería de la federación, banco multiva, afirme, banregio, banca mifel, inbursa, mufg, rbs, banco interacciones, ing, bank of america y bansi.
* Solamente la persona interesada puede realizar el trámite de su pasaporte.

### Reglas (situaciones que solo pueden ocurrir cuando las condicionales se cumplen)
* Si el solicitante es mayor de 60 años, cuenta con una discapacidad o es trabajador agrícola en Canadá entonces puede acceder al descuento del 50% del costo total del trámite.
* Si el solicitante es trabajador agrícola entonces no puede tramitar el pasaporte con vigencia de 10 años.
* Si el solicitante pide el pasaporte por primera vez y es mayor de edad entonces requiere acreditar la nacionalidad mexicana y presentar una identificación oficial vigente en original.
* Si el solicitante está renovando el pasaporte y es mayor de edad entonces deberá presentar el pasaporte original vencido, acreditar la nacionalidad mexicana y presentar una identificación oficial vigente en original.
* Si el solicitante pide el pasaporte por primera vez y es menor de edad entonces deberá acreditar la nacionalidad mexicana, presentar una identificación oficial vigente en la que sus datos coincidan con los del acta de nacimiento, presentar identificación oficial de la o las personas que ejerzan la patria potestad o tutela del menor de edad y presentar su autorización.
* Si el solicitante está renovando el pasaporte y es menor de edad entonces deberá presentar el pasaporte original vencido y presentar identificación oficial de la o las personas que ejerzan la patria potestad o tutela del menor de edad y presentar su autorización.
* Si el pasaporte vencido fue extraviado, destruido, o robado entonces deberá realizar el trámite como si fuera la primera vez.
* Si el solicitante no realiza el pago del trámite entonces no podrá realizarlo.

## Ejecución del programa
1. Este programa fue probado con Python 3.13.7
2. Los ficheros `sld_practice.py` y `knowledge_base_pasaporte.py` deben estar en la misma ubicación, de no ser así, no funcionarán.
3. Ejecuta a través de una terminal el comando:
``` shell
python3 sld_practice.py
```

> Posdata:
> Pienso que también debería poder ejecutarse con `python` sin el 3.
