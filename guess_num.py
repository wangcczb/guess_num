import random
start = input('請決定隨機數字範圍開始值: ')
end = input('請決定隨機數字範圍結束值: ')
start = int(start)
end = int(end)
r = random.randint(start,end)
i = 0 #猜了幾次
while True:
	num = input('請猜一個數字:' )
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
