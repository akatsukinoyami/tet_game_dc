from random	import randint

def coin(username):
	coin = " **орёл**" if randint(0, 1) == 1 else "а **решка**"
	return f'{username} подкинул(а) монетку и выпал{coin}.'