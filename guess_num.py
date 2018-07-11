import random
r = random.randint(1,100)
i = 0 #猜了幾次
while True:
	num = input('請猜一個1~100的整數:' )
	num = int(num)
	i += 1 #i = i + 1
	if num == r:
		print('恭喜猜對了')
		print('你猜了第', i, '次')
		break
	elif num > r:
		print('猜錯惹，再小一點')
	else:
		print('再大一點')
	print('你猜了第', i, '次')
