import discord  # Importa la librería principal de Discord.py
from discord.ext import commands  # Importa la extensión de comandos de Discord.py
from modelo import *

intents = discord.Intents.default()  # Crea un objeto de intenciones por defecto
intents.message_content = True  # Habilita la intención de leer el contenido de los mensajes

bot = commands.Bot(command_prefix='$', intents=intents)  # Crea un objeto de bot con el prefijo '$' y las intenciones configuradas

@bot.event  # Decorador para definir un evento
async def on_ready():  # Evento que se ejecuta cuando el bot se conecta
    print(f'We have logged in as {bot.user}')  # Imprime un mensaje en la consola indicando que el bot se ha conectado

@bot.command()  # Decorador para definir un comando
async def upload_image(ctx):  # Comando para subir imágenes
    if len(ctx.message.attachments) == 0:  # Si no hay archivos adjuntos
        await ctx.send("No se ha encontrado ninguna imagen adjunta.")  # Envía un mensaje indicando que no hay imágenes
    else:  # Si hay archivos adjuntos
        # Itera sobre los archivos adjuntos
        for attachment in ctx.message.attachments:
            if attachment.filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):  # Si el archivo es una imagen
                # Guarda la imagen en el sistema de archivos local
                filepath = f"images/{attachment.filename}"
                await attachment.save(filepath)
                # Envía un mensaje con la URL de la imagen guardada
                await ctx.send(f"Imagen {attachment.filename} guardada con éxito. Disponible en: {attachment.url}")

                resultado = get_class(filepath)
                await ctx.send(f"La raza de este gato es: {resultado}")
            else:  # Si el archivo no es una imagen
                await ctx.send(f"El archivo {attachment.filename} no es una imagen válida.")

bot.run("407d990e7341be4d407f3d185591aa8119c28f5bb8f1bfee80866225fc7415b1")  # Ejecuta el bot con tu token