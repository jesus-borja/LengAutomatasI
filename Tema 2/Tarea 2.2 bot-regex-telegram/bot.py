import logging
import re
import os

from dotenv import load_dotenv

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters



# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Expresión regular para detectar mensajes que contienen "Hola"
saludos = re.compile(r"hello|hi|hey|hola", re.IGNORECASE)

# Expresión regular para detectar mensajes que contienen "Buenos días" o "Buenas noches" en portugues
saludos_portugues = re.compile(r"(bom dia)|(boa noite)", re.IGNORECASE)

# Expresión regular para detectar mensajes relacionados con vuelos
patron_origen_destino_fecha = re.compile(r"volar de (.*) a (.*) el (\d{1,2} de .*)", re.IGNORECASE)
patron_precio               = re.compile(r"cu[a|á]nto cuesta un vuelo de (.*) a (.*)", re.IGNORECASE)
patron_ida_vuelta           = re.compile(r"un vuelo de ida y vuelta de (.*) a (.*)", re.IGNORECASE)

# Expresiones regulares para detectar numeros de la suerte
patron_numero_suerte_definicion = re.compile(r"qu[e|é] (.*) n[u|ú]meros? (.*) suerte", re.IGNORECASE)
patron_numero_de_la_suerte      = re.compile(r"es (\d+) un n[u|ú]mero de la suerte", re.IGNORECASE)

def esNumeroDeLaSuerte(string: str) -> bool:
    """Dada un cadena verifica si cumple el patrón de un número de la suerte (S = 8 ⋯ 86 ⋯ 6)"""
    numero_de_la_suerte = re.compile(r"^(8+6*|8*6+)$")
    return bool(numero_de_la_suerte.match(string=string))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message if it matches the regular expression."""
    message_text = update.message.text

    if saludos.search(message_text):
        await update.message.reply_text("¡Hola! ¿Cómo estás?")
    elif saludos_portugues.search(message_text):
        await update.message.reply_text("Olá, tudo bem?")
    elif patron_numero_suerte_definicion.search(message_text):
        await update.message.reply_text("Un número de la suerte es de la forma S = 8 ⋯ 86 ⋯ 6, donde S tiene al menos un dígito y el número de dígitos 6 y 8 pueden ser cero. Ejemplos de estos números son: 8,88,6,66,86,866,8866, etc. Ejemplos de números que no son de la suerte: 68,868,3,688.")
    elif resultado := patron_origen_destino_fecha.search(message_text):
        await update.message.reply_text(f"Buscando vuelos de {resultado.group(1)} a {resultado.group(2)} para la fecha {resultado.group(3)}...")
    elif resultado := patron_precio.search(message_text):
        await update.message.reply_text(f"Buscando el precio de vuelos de {resultado.group(1)} a {resultado.group(2)}...")
    elif resultado := patron_ida_vuelta.search(message_text):
        await update.message.reply_text(f"Buscando vuelos de ida y vuelta de {resultado.group(1)} a {resultado.group(2)}...")
    elif resultado := patron_numero_de_la_suerte.search(message_text):
        numero = resultado.group(1)
        await update.message.reply_text(f"{numero} {'es' if esNumeroDeLaSuerte(numero) else 'no es'} un número de la suerte")
    else:
        await update.message.reply_text("No entendí tu mensaje.")

def main() -> None:
    """Start the bot."""

    # Carga el archivo .env
    load_dotenv()
    # busca el token para un bot de telegram a la constante
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

# Ejecuta la aplicación si se ejecuta directamente este archivo
if __name__ == "__main__":
    main()
