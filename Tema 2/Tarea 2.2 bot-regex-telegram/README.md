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

<img src="./img/1 Inicio.jpg" alt="Inicio del chat" width="300px"></img>

## Saludos en español

<img src="./img/2 Saludos.jpg" alt="Saludos en español" width="300px"></img>

Para esta respuesta se usó la siguiente expresión regular que detecta las palabras "Hola", "Hey", "Hello", "Hi". Se usa la bandera `IGNORECASE` para detectar letras mayúsculas y minúsculas.

```python
re.compile(r"hello|hi|hey|hola", re.IGNORECASE)
```

## Saludos en portugues

### Bom dia

<img src="./img/4 Bom dia.jpg" alt="Bom dia" width="300px"></img>

Para esta respuesta se usó la siguiente expresión regular que detecta las frases "Bom dia" y "Boa noite", con la bandera `IGNORECASE` para que detecta tanto letras mayúsculas como minúsculas.

```python
re.compile(r"(bom dia)|(boa noite)", re.IGNORECASE)
```

### Boa noite

<img src="./img/3 Boa noite.jpg" alt="Bom noite" width="300px"></img>

Para esta respuesta se usó la misma expresión regular que en el ejemplo anterior.

```python
re.compile(r"(bom dia)|(boa noite)", re.IGNORECASE)
```

## Mensajes relacionados con los vuelos

### Quiero volar de ... a ... el ...

<img src="./img/5 Vuelos con fecha.jpg" alt="Vuelos con fecha" width="300px"></img>

Para generar esta respuesta se usó la siguiente expresión regular que detecta las frases similares a "Volar de Cualquier país/lugar a Cualquier otro país/lugar".

```python
re.compile(r"volar de (.*) a (.*) el (\d{1,2} de .*)", re.IGNORECASE)
```

### ¿Cuánto cuesta un vuelo de ... a ...?

<img src="./img/6 Precio de un vuelo.jpg" alt="Precio de un vuelo" width="300px"></img>

Para esta respuesta se usó la siguiente expresión regular que detecta las oraciones parecidas a "¿Cuánto cuesta un vuelo de Cualquier país/lugar a Cualquier otro país/lugar".

```python
re.compile(r"cu[a|á]nto cuesta un vuelo de (.*) a (.*)", re.IGNORECASE)
```

### Me gustaria un vuelo de ida y vuelta de ... a ...?

<img src="./img/7 Vuelos de ida y vuelta.jpg" alt="Vuelos de ida y vuelta" width="300px"></img>

Para esta respuesta se usó la siguiente expresión regular que detecta las frases parecidas a "Un vuelo de ida y vuelta de Cualquier lugar/país a Cualquier otro lugar/país".

```python
re.compile(r"un vuelo de ida y vuelta de (.*) a (.*)", re.IGNORECASE)
```

## Mensajes relacionados a los números de la suerte

### ¿Qué es un número de la suerte?

<img src="./img/8 Definición número de la suerte.jpg" alt="Definición de un número de la suerte" width="300px"></img>

Para esta respuesta se usó la siguiente expresión regular que detecta las frases parecidas a "¿Qué son los números de la suerte?" o "¿Qué es un número de la suerte?".

```python
re.compile(r"qu[e|é] (.*) n[u|ú]meros? (.*) suerte", re.IGNORECASE)
```

### ¿Es ... un número de la suerte?

<img src="./img/9 Número de la suerte.jpg" alt="Número de la suerte" width="300px"></img>

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
