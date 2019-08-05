from urllib import request
import urllib
import time
import re
import random

agent1="Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36"
agent2="Mozilla/5.0 (Linux; Android 8.1; PAR-AL00 Build/HUAWEIPAR-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044304 Mobile Safari/537.36 MicroMessenger/6.7.3.1360(0x26070333) NetType/WIFI Language/zh_CN Process/tools"
agent3="Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044207 Mobile Safari/537.36 MicroMessenger/6.7.3.1340(0x26070332) NetType/4G Language/zh_CN Process/tools"
agent4="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
agent5="Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)"
list1=[agent1,agent2,agent3,agent4,agent5]
agent=random.choice(list1)
print(agent)
#构造请求头信息
header={
"User-Agent": agent
}

# url="http://tieba.baidu.com/f?ie=utf-8&kw=python"#第一页(1-1)*50
# url="http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50"#第二页(2-1)*50
# url="http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=100"#第三页(3-1)*50
# url="http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=150"#第四页(4-1)*50
# for i in range(1,5):
#     url = "http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=" +str((i-1)*50)
#     print(url)

def loadpage(fullurl,filename):
    print("正在下载:",filename)
    req=request.Request(fullurl,headers=header)
    res=request.urlopen(req).read()
    return res


def writepage(html,filename):
    print("正在保存:",filename)

    with open(filename,"wb")as f:
        f.write(html)
    print("-"*20)





def tiebaSpider(url,begin,end):
    for page in range(bagin,end+1):
        pn=str((page-1)*50)
        fullurl=url+"&pn="+pn#每次请求的完整url
        filename="D:\chrome\第"+str(page)+"页.html"#每次请求后保存文件名

        html=loadpage(fullurl,filename)#调用爬虫，爬取网页
        writepage(html,filename)#把获取到的网页信息写入本地


if __name__ =='__main__':
    kw=input("请输入贴吧名称")
    bagin=int(input("请输入起始页："))
    end=int(input("请输入结束页："))
    url="http://tieba.baidu.com/f?"
    key =urllib.parse.urlencode({"kw":kw})
    url=url+key
    tiebaSpider(url,bagin,end)

    time.sleep(30)