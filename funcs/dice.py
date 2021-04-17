from random	import randint

def dice(txt, username):
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