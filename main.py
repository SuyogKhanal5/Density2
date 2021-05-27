import discord
from discord.ext import commands

import requests
HEADERS = {"X-API-Key":'649ea8eecf5543c0a4c29bd2b175f5ba'}

client = commands.Bot(command_prefix = '$')
token = 'ODIwNDAzNDMxODU5ODE0NDMw.YE0qPA.K2LVr3Ed7wP4cyoQGTr_MVvcD3Q'

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game('Destiny 2'))
    print('Bot is online')

@client.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

@client.command()
async def leave(ctx):
    guild = ctx.message.guild
    voice_client = guild.voice_client
    await voice_client.disconnect()

@client.command()
async def joinChannel(ctx, *, given_name):
    channel = discord.utils.get(ctx.guild.channels, name=given_name)
    await channel.connect()

@client.command()
async def move(ctx, *, given_name):
    guild = ctx.message.guild
    voice_client = guild.voice_client
    await voice_client.disconnect()

    channel = discord.utils.get(ctx.guild.channels, name=given_name)
    await channel.connect()

@client.command()
async def gjallarhorn(ctx):
    #make request for Gjallarhorn
    r = requests.get("https://www.bungie.net/platform/Destiny/Manifest/InventoryItem/1274330687/", headers=HEADERS)

    #convert the json object we received into a Python dictionary object
    #and print the name of the item
    inventoryItem = r.json()
    await ctx.send(inventoryItem['Response']['data']['inventoryItem']['itemName'])

@client.command()
async def d1xur(ctx):
    xur_url = "https://www.bungie.net/Platform/Destiny/Advisors/Xur/"

    hashType = "6"

    res = requests.get(xur_url, headers=HEADERS)

    print("\n\n\nConnecting to Bungie: " + xur_url + "\n")
    print("Fetching data for: Xur's Inventory!")

    error_stat = res.json()['ErrorStatus']
    print("Error status: " + error_stat + "\n")
    
    res = requests.get(xur_url, headers=HEADERS)

    for saleItem in res.json()['Response']['data']['saleItemCategories']:
        mysaleItems = saleItem['saleItems']

        for myItem in mysaleItems:
            hashID = str(myItem['item']['itemHash'])

    base_url = "https://www.bungie.net/platform/Destiny/"
    
    for saleItem in res.json()['Response']['data']['saleItemCategories']:
        mysaleItems = saleItem['saleItems']
        
        for myItem in mysaleItems:
            hashID = str(myItem['item']['itemHash'])
            hashReqString = base_url + "Manifest/" + hashType + "/" + hashID
            res = requests.get(hashReqString, headers=HEADERS)
            item_name = res.json()['Response']['data']['inventoryItem']['itemName']
            await ctx.send(item_name)

client.run(token)