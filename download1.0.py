import os

def download(base_url, i):
	filename = "zy_" + str(i)
	os.system("you-get -o H:/zy -O " + filename + " " + base_url + str(i))

base_url = "https://www.bilibili.com/video/av9647631/?p="

for i in range(1,59):
	download(base_url, i)

print("finished!")
