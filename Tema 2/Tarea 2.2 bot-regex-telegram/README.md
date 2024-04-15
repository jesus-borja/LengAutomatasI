# Inicio rápido

Para replicar el funcionamiento de este bot, es necesario instalar los paquetes `python-telegram-bot` y `python-dotenv`.

```console
$ pip install python-telegram-bot
$ pip install python-dotenv
```

También es necesario contar con el archivo `.env` y guardar en él el token de acceso a un bot de Telegram. Para ello se proporciona el archivo `.env.example` con la estructura necesaria para ello.

Finalmente, basta con ejecutar el archivo `bot.py`.

```console
$ python bot.py
```

# Ejemplos de uso

## Inicio

![Inicio del chat](./img/1%20Inicio.jpg)

## Saludos en español

![Saludos en español](./img/2%20Saludos.jpg)

Para esta respuesta se usó la siguiente expresión regular que detecta las palabras "Hola", "Hey", "Hello", "Hi". Se usa la bandera `IGNORECASE` para detectar letras mayúsculas y minúsculas.

```python
re.compile(r"hello|hi|hey|hola", re.IGNORECASE)
```

## Saludos en portugues

### Bom dia

![Bom dia](./img/4%20Bom%20dia.jpg)

Para esta respuesta se usó la siguiente expresión regular que detecta las frases "Bom dia" y "Boa noite", con la bandera `IGNORECASE` para que detecta tanto letras mayúsculas como minúsculas.

```python
re.compile(r"(bom dia)|(boa noite)", re.IGNORECASE)
```

### Boa noite

![Bom noite](./img/3%20Boa%20noite.jpg)

Para esta respuesta se usó la misma expresión regular que en el ejemplo anterior.

```python
re.compile(r"(bom dia)|(boa noite)", re.IGNORECASE)
```

## Mensajes relacionados con los vuelos

### Quiero volar de ... a ... el ...

![Vuelos con fecha](./img/5%20Vuelos%20con%20fecha.jpg)

Para generar esta respuesta se usó la siguiente expresión regular que detecta las frases similares a "Volar de Cualquier país/lugar a Cualquier otro país/lugar".

```python
re.compile(r"volar de (.*) a (.*) el (\d{1,2} de .*)", re.IGNORECASE)
```

### ¿Cuánto cuesta un vuelo de ... a ...?

### ¿Cuánto cuesta un vuelo de ... a ...?

![Precio de un vuelo](./img/6%20Precio%20de%20un%20vuelo.jpg)

Para esta respuesta se usó la siguiente expresión regular que detecta las oraciones parecidas a "¿Cuánto cuesta un vuelo de Cualquier país/lugar a Cualquier otro país/lugar".

```python
re.compile(r"cu[a|á]nto cuesta un vuelo de (.*) a (.*)", re.IGNORECASE)
```

### Me gustaria un vuelo de ida y vuelta de ... a ...?

![Vuelos de ida y vuelta](./img/7%20Vuelos%20de%20ida%20y%20vuelta.jpg)

Para esta respuesta se usó la siguiente expresión regular que detecta las frases parecidas a "Un vuelo de ida y vuelta de Cualquier lugar/país a Cualquier otro lugar/país".

```python
re.compile(r"un vuelo de ida y vuelta de (.*) a (.*)", re.IGNORECASE)
```

## Mensajes relacionados a los números de la suerte

### ¿Qué es un número de la suerte?

![Definicion número de la suerte](./img/8%20Definición%20número%20de%20la%20suerte.jpg)

Para esta respuesta se usó la siguiente expresión regular que detecta las frases parecidas a "¿Qué son los números de la suerte?" o "¿Qué es un número de la suerte?".

```python
re.compile(r"qu[e|é] (.*) n[u|ú]meros? (.*) suerte", re.IGNORECASE)
```

### ¿Es ... un número de la suerte?

![Número de la suerte](./img/9%20Número%20de%20la%20suerte.jpg)

Para esta respuesta se usó la siguiente expresión regular que detecta frases como "¿Es # un número de la suerte?" donde # puede ser un número con al menos un dígito

```python
re.compile(r"es (\d+) un n[u|ú]mero de la suerte", re.IGNORECASE)
```

#### Comprobación

Para comprobar si el número que se envío es o no un número de la suerte con la definición dada, se usa la siguiente función que evalua una cadena con la expresión regular `8+6*|8*6+` y retorna un valor boleano de acuerdo si se detecta dicho patrón o no.

```python
def esNumeroDeLaSuerte(string: str) -> bool:
    """Dada un cadena verifica si cumple el patrón de un número de la suerte (S = 8 ⋯ 86 ⋯ 6)"""
    numero_de_la_suerte = re.compile(r"^(8+6*|8*6+)$")
    return bool(numero_de_la_suerte.match(string=string))
```

## Otras cadenas

![Otros mensajes](./img/10%20Otros%20mensajes.jpg)

Para las cadenas que no cumplen ninguna de las expresiones regulares se envia un mensaje indicando que no se reconoció el mensaje anterior.
