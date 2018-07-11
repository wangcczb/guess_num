import random
r = random.randint(1,100)
while True:
	num = input('請猜一個1~100的整數:' )
	num = int(num)
	if num == r:
		print('恭喜答對了')
		break
	elif num > r:
		print('太大囉，再小一點')
	else:
		print('太小囉，再大一點')