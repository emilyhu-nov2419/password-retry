# Test password
password = 'a123'
totalCount = 4
i = totalCount
while i > 0:
	pwd = input('請輸入密碼:')
	if pwd == password:
		print ('登入成功!')
		break #逃出迴圈
	else:
		i = i - 1
		print ('密碼錯誤', totalCount - i, '次')