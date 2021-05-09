#最多輸入三次
#如果正確就印出"登入成功"
#如果印出不正確 就印出"密碼錯誤! 還有_次機會"

password ='a123456'  #都將變數在這邊定義好處是以後修改都知道在這裡找就好
i = 3 # 變數用來當作剩餘機會
while True:  #記得True是大寫
	pwd = input('請輸入密碼:')
	if pwd == password:  #判斷不是與預設密碼相同
		print('登入成功')
		break  #逃出迴圈
	else:
		i = i - 1 #每次進來就扣1
		print('登入失敗,你還有', i ,'次機會') # 'str' , int , 'str'
		if i == 0:   #else 裡面還是可以放if的,其實都可以嘗試跑看看
			break    #逃離迴圈
