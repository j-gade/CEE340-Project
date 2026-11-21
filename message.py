"""
Dependencies include discord and requests
run the commands below to in RPI terminal 
to install discord and requests

Commands:
sudo apt update
sudo apt install -y python3-pip python3-requests
pip install --break-system-packages discord.py 

Note --break-system-packages is required becauses pip conflicts apt, and this allows pip to bypass it


Additionally API keys are in discord
as I don't want them to be public and 
please for rapid testing use only the
Discord bot due to the message limits
on the textbelt API key.
"""
import discord
import requests
DiscordAPIKey = "Get From Discord Server"
textBeltAPIkey = "Get From Discord Server"

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as{self.user}!')
        channel = discord.utils.get(self.get_all_channels(),name="bot")
        if channel:
            await channel.send(self.message)
        await self.close()

def sendDiscordMessage(message):
    intents = discord.Intents.default()
    client = Client(intents=intents)
    client.message = message
    client.run(DiscordAPIKey)

def sendTextMessage(message, phoneNumber):
    resp = requests.post('https://textbelt.com/text', {
        'phone': phoneNumber,
        'message': message,
        'key': textBeltAPIkey, 
    })
    return(resp.json().get('success'))

def sendMessage(message, phoneNumber):
        sendDiscordMessage(message)
        sendTextMessage(message,phoneNumber)
