import re

import discord

from funcs.coin import coin
from funcs.dice import dice
from funcs.help	import help

class Discord(discord.Client):
	async def on_ready(self):
		print(f'Logged in as {client.user}', flush=True)
		
	async def on_message(self, msg):
		if msg.author == self.user:	return 0

		username	= msg.author.name
		txt	= msg.content.split()[0]

		if   '/coin' in txt: 							answer = coin(username)
		elif '/help' in txt:							answer = help()
		elif re.search(r'\/\d*d\d', txt):	answer = dice(txt, username)
		else:															answer = False

		if answer:
			await msg.reply(answer)