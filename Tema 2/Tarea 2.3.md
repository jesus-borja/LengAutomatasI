# Tarea 2.3 Expresiones Regulares

## Válida un password fuerte

Debe ser de 8 carácteres de longitud y tener al menos:

-   1 minúscula
-   1 mayúscula
-   1 número
-   1 caracter especial

Mi primera intención era usar esta expresión regular:

```python
r"[a-zA-Z0-9@^¡!#$%&/=_\-*+¿?]{8}"
```

Sin embargo, no solo válida contraseñas fuertes (`Pap4G#l0` o `pa$S3gur`), sino también contraseñas como: `abcedfgh` o `12345678`
Para solucionar ese problema usamos el operador lookahead positivo. Lo que hace es revisar toda la cadena y verificar que contenga algún carácter de los específicados, en caso de encontrarlos, podrá hacer match con el resto de la cadena, de no encontrarlos, ya no ignorará la cadena.

```python
r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\da-zA-Z\s]).{8}$"
```

De esta manera podemos hacer verificar contraseñas seguras como las anteriores, sin permitir aquellas que no cumplen con alguno de los requisitos.

## Válida un nombre de usuario

El nombre de usuario puede tener una longitud de 3 a 16 carácteres y debe estar formado por letras, números y guiones medios o bajos.

```python
r"[0-9a-zA-Z_-]{3,16}"
```
