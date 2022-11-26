'''
1.确定目标需求
2.发送请求
3.获取数据
4。解析数据
5.保存数据
'''
'''
#发送请求，导入第三方文件模块
import requests
import parsel
url='https://travel.qunar.com/travelbook/list.htm?order=hot_heat'
#请求头：把python的代码伪装成客户端给服务器发送请求
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
response=requests.get(url=url,headers=headers)
print(response.text)
#解析数据
selector=parsel.Selector(response.text)
#提取北京所有的景区的内容，返回的是一个列表对象
lis=selector.css('#search-list.sight_item_detail')#css选择器，根据标签提取数据内容
for li in lis:
    li.css('')
    print(li)
    break'''
#去哪儿热门景点攻略的爬取
'''
代码实现的步骤
1.向目标网页发送网络请求
2.获取数据，网页源代码
3.筛选我们要的数据
4.向每一个详情页链接发送网络请求
5.获取数据 网络源代码
6.提取数据（数据清洗）
    时间 天数 人均费用 地点
7.保存数据
8.多页爬取
9.做一个可视化分析旅游景点推荐
'''
import requests #发送请求
import parsel #筛选数据
url='https://travel.qunar.com/travelbook/list.htm?order=hot_heat'
response=requests.get(url)#发送请求
#print(response.text)
html_data=response.text#获取数据
selectors=parsel.Selector(html_data)#筛选数据
url_list=selectors.css('body > div.qn_mainbox > div > div.left_bar > ul > li > h2 > a::attr(href)').getall()#css选择器选取网页内容
for detail_url in url_list:
    detail_id=detail_url.replace('/youji/','')
    detail_url='https://travel.qunar.com/travelbook/note/'+detail_id
    response_1=requests.get(detail_url)#向每一个详情页发送网络请求
    data_html_1=response_1.text#获取数据，网页源代码
    #提取数据
    #出发日期 天数 人均费用 人物 玩法 地点 浏览量
    selector_1=parsel.Selector(data_html_1)
    #book=selector_1.css('#booktitle::text').get()#::是属性提取器
    title=selector_1.css('.b_crumb_cont *:nth-child(3)::text').get()#标题
    comment=selector_1.css('.title.white::text').get()#短评
    count=selector_1.css('.view_count::text').get() #浏览量
    date=selector_1.css('#js_mainleft > div.b_foreword > ul > li.f_item.when > p::text').get()#出发日期
    time=selector_1.css('#js_mainleft > div.b_foreword > ul > li.f_item.when > p > span.data::text').get()
    day=selector_1.css('#js_mainleft > div.b_foreword > ul > li.f_item.howlong > p::text').get()
    da=selector_1.css('#js_mainleft > div.b_foreword > ul > li.f_item.howlong > p > span.data::text').get()
    money=selector_1.css('#js_mainleft > div.b_foreword > ul > li.f_item.who > p::text').get()
    people=selector_1.css('#js_mainleft > div.b_foreword > ul > li.f_item.who > p > span.data::text').get()
    play=selector_1.css('#js_mainleft > div.b_foreword > ul > li.f_item.how > p::text').get()
    feel=selector_1.css('#js_mainleft > div.b_foreword > ul > li.f_item.how > p > span.data > span:nth-child(1)::text').get()
    print(title,comment,count,date,time,day,da,money,people,play,feel)
