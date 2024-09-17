import discord
import random
import os

from discord import app_commands
from discord.ext import commands
from datetime import datetime, timedelta

import logging as log

# Configurar el sistema de logging
log.basicConfig(level=log.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# permissions
intents = discord.Intents.default()
# Allows the bot to read message content to process commands. This is essential if your bot will respond to messages.
intents.message_content = True

# Necessary if your bot needs to react to events related to members, such as when someone joins or leaves the server.
intents.members = True

# Required for handling events related to guilds, such as server configuration updates or when roles are added or
# removed.
intents.guilds = True

# Enables the bot to detect and respond to reactions on messages.
intents.reactions = True

DISCORD_TOKEN = "MTI4NTY1NjkxNTAwMjc4NTg2Mg.GY_3Hb.Ahek0pLlo020t2W35-RnC8O7mMd20-Ha8hgi9E" #os.environ["discord_token"]

# Configura tu bot con los intents y el prefijo
bot = commands.Bot(command_prefix='y!', intents=intents, help_command=None)



@bot.event
async def on_ready():
    log.info(f'{bot.user} está listo.')
    bot.start_time = datetime.now()
    try:
        synced = await bot.tree.sync()  # Sincroniza los comandos de barra (slash commands) con Discord
        log.info(f'Sincronizados {len(synced)} comando(s)')

    except Exception as e:
        log.error(f'Fallo al sincronizar los comandos: {e}')


@bot.tree.command(name="status")
async def status(interaction: discord.Interaction):
    """Muestra información detallada del estado del bot"""
    latency = bot.latency  # Latencia en segundos
    status = "En línea ✅️" if bot.is_ready() else "Desconectado ❌"
    uptime = datetime.now() - bot.start_time

    # Calcular días, horas, minutos y segundos
    days = uptime.days
    hours, remainder = divmod(uptime.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    embed = discord.Embed(
        title="Información del bot",
        description=f"Datos relevantes para el funcionamiento del bot \n\n"
                    f"**Estado del bot: **{status}\n"
                    f"**Latencia: **{latency * 1000:.2f} ms\n"
                    f"**Tiempo en línea: **{days} días, {hours} horas, {minutes} minutos, {seconds} segundos\n\n",
        color=discord.Color.from_rgb(239, 0, 5)
    )
    current_directory = os.getcwd()
    log.info(current_directory)
    image_path = os.path.join('img', 'yakuza-logo.PNG')
    complete_path = os.path.join(current_directory, image_path)
    log.info(image_path)
    embed.set_thumbnail(url=complete_path)
    embed.set_footer(text="Powered by: ⛩️Yakuza⛩️ - La Palma RP🌴")

    # Enviar el archivo y usarlo en el embed
    with open(complete_path, 'rb') as f:
        file = discord.File(f, filename='yakuza-logo.PNG')
        embed.set_thumbnail(url='attachment://yakuza-logo.PNG')
        await interaction.response.send_message(file=file, embed=embed)



def give_random_answer(command):
    '''if c.config is not None:
        bot_anwser = random.choice(c.config[command]["bot_answers"])
        print(f'Respuesta escogida: {bot_anwser}')
        return bot_anwser'''


def run_bot():
    bot.run(DISCORD_TOKEN)


if __name__ == "__main__":
    run_bot()
