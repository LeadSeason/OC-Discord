import discord
from discord.ext import commands

import json
import threading
import socket

import time

##### discord stuff #####
"""
with open("./configs/discord_conf.json") as discord_conf:
    token = json.load(discord_conf)["token"]

bot = commands.Bot(command_prefix=";")
"""

##### scoket stuff #####

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 42069))
s.listen(5)
clientsocket, address = s.accept()

def background():
    while True:
        clientsocket, address = s.accept()
        print(address[0] + ':' + str(address[1]) + ' connected')


def foreground():
    global clientsocket, address
    while True:
        time.sleep(2)
        print("sending")
        clientsocket.send(bytes("Test", encoding="utf-8"))

    #recv_data = str(clientsocket.recv(1024), encoding='utf-8')

    """
    @bot.event
    async def on_ready():
        print(f"logged in as {bot.user}")
    """


bg = threading.Thread(name='background', target=background)
fg = threading.Thread(name='foreground', target=foreground)

bg.start()
fg.start()
"""
bot.run(token)
"""