import os

def download(i):
	filename = base_filename + str(i)
	cmd = "you-get -o " + savepath + " -O " + filename + " " + base_url + str(i)
	os.system(cmd)

def get_filelist(path):
	return os.listdir(path)

def get_isexist():
	isexist = []
	for i in range(n+1):
		isexist.append(0)
	listdir = get_filelist(savepath)
	for filename in listdir:
		res = filename.split(".")[0].split("_")
		if len(res) == 2:
			isexist[int(res[1])] = 1
	return isexist

def redownload():
	isexist = get_isexist()
	for i in range(1,n+1):
		if isexist[i] == 0:
			print(str(i)+"正在重新下载")
			download(i)

base_url = "https://www.bilibili.com/video/av9647631/?p="
n = 58
base_filename = "zy_"
savepath = "H:\\zy"

while sum(get_isexist()) < n:
	redownload()
# for i in range(1,59):
# 	download(base_url, i)


print("finished!")
