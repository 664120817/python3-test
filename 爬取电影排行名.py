import requests
import re
import xlsxwriter

workbook = xlsxwriter.Workbook("豆瓣电影排行.xlsx")
worksheet = workbook.add_worksheet()
headers={

"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)"
}
begin= int(input ("请输入爬取起始页"))
end= int (input ("请输入爬去结束页"))
num=0
for i in range(begin,end):
        n=str(20*i)
        url="https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start="+n+"&limit=20"
        # https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=20&limit=20
        # https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=40&limit=20
        req=requests.get(url,headers)
        res=(req.text)
        # print(res)
        pat1=re.compile(r'"title":"(.*?)"',re.I)
        pat2=re.compile(r'"rating":\["(.*?)","\d+"\]',re.I)
        res1=pat1.findall(res)
        res2=pat2.findall(res)
        # print(res1,res2)
        for i in range(len(res1)):
            print("电影名：",res1[i], "豆瓣评分：",res2[i])
            num+=1
            worksheet.write("A" + str(num),"电影名："+res1[i])
            worksheet.write("B" + str(num), "豆瓣评分："+res2[i])
            print(num)
workbook.close()