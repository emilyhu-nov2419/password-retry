# Test password
password = 'a123'
p = 3
while True:
	pwd = input('請輸入密碼:')
	if pwd == password:
		print ('登入成功!')
		break #逃出迴圈
	else:
	   p = p - 1
       print ('密碼錯誤!', p ,'次機會')
       if p == 0:
       	break