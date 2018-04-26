f = open("xx珍藏.txt","w")
f.write("原谅我一生放荡不羁爱自由\n")
f.close()

file_name = input("请输入文件名")
old_name = open(file_name,"r")

position = file_name.rfind(".")
new_name = file_name[0:position]+"复制"+file_name[position:],"w"
while True:
	content = old_name.read(1024)
	if len(content) ==0:
		break
	new_name.write(content)
old_name.close()
new_name.close()
