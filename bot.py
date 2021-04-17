import re
from random	import randint
from os			import getenv as env

import discord

class Discord(discord.Client):
	async def on_ready(self):
		print(f'Logged in as {client.user}', flush=True)
		
	async def on_message(self, msg):
		if msg.author == self.user:	return 0

		username	= msg.author.name
		txt	= msg.content.split()[0]

		if '/coin' in txt: 
			answer = await coin(username)
		elif re.search(r'\/\d*d\d', txt):
			answer = await dice(txt, username)
		else:
			answer = False

		if answer:
			await msg.reply(answer)
							
async def coin(username):
	coin = " **орёл**" if randint(0, 1) == 1 else "а **решка**"
	return f'{username} подкинул(а) монетку и выпал{coin}.'

async def dice(txt, username):
	txt = txt.replace('/', '')
	txt_len = len(txt)

	dice			= lambda dice: str(randint(1, dice))

	if txt_len > 2:	
		txt = txt.split('d')

		dices	=	int(txt[0])
		dices_txt = f'{dices} кубик{"а" if 2 <= dices <= 4 else "ов"}'
		
		polygons	= int(txt[1])
		answer		= ', '.join([dice(polygons) for i in range(dices)])

	else:							
		txt = txt.replace('d', '')

		dices_txt = f'один кубик'
		polygons	= int(txt)
		answer		= dice(polygons)

	return f"{username} кинул(а) {dices_txt} на {polygons}.\nВыпало **{answer}**."

client = Discord()
client.run(env('DC_TOKEN'))