# qunaer
# Python爬取去哪儿的攻略

## 入门教程

不需要html和css的相关知识也可以做

```html
代码实现的步骤
1.向目标网页发送网络请求
2.获取数据，网页源代码
3.筛选我们要的数据
4.向每一个详情页链接发送网络请求
5.获取数据 网络源代码
6.提取数据（数据清洗）
    时间 天数 人均费用 地点
```

### 需要用到的模块：

```python
import requests #发送请求
import parsel #筛选数据
```

### 我将按这六步来实现内容的爬取：

#### 1.向目标网页发送网络请求



```python
url='https://travel.qunar.com/travelbook/list.htm?order=hot_heat'
response=requests.get(url)#发送请求
```

#### 2.获取数据

```python
#print(response.text) 
#这个是打印出来看是否可以成功访问，若访问不了可能有反爬虫机制，这时我们要加一个自己浏览器的访问头
html_data=response.text#获取数据
```

##### 2.1访问头

邮寄页面检查/按12来打开开发者工具



拉到下面看user-agent：


```python
#请求头：把python的代码伪装成客户端给服务器发送请求
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/5 (KHTML, like Gecko) Chrome/107.'}
```

#### 3.筛选数据

```python
selectors=parsel.Selector(html_data)#筛选数据
url_list=selectors.css('body > div.qn_mainbox > div > div.left_bar > ul > li > h2 > a::attr(href)').getall()#css选择器选取网页内容
```




右击该部分代码选中copy selector



然后将该部分的代码改成列表就行，body > div.qn_mainbox > div > div.left_bar > ul > li:nth-child(1) > h2 > a，即将li:nth-child(1)修改为li，不用选中第几个子部分，即为列表

```python
url_list=selectors.css('body > div.qn_mainbox > div > div.left_bar > ul > li > h2 > a::attr(href)').getall()#css选择器选取网页内容
```

#### 4.向每一个详情页发送请求

```python
for detail_url in url_list:
    detail_id=detail_url.replace('/youji/','')
#replace是将不用的代码删掉，然后把有用的id加到url后面    detail_url='https://travel.qunar.com/travelbook/note/'+detail_id
    response_1=requests.get(detail_url)#向每一个详情页发送网络请求
```

#### 5.获取数据

```python
data_html_1=response_1.text#获取数据，网页源代码
```

#### 6.提取数据

数据的代码去网页的开发者工具找，选中要提取的部分然后copy selector，这个就是你要的数据的代码，但是我们要文本部分，所以用：：（两个冒号）来提取text部分，最后将提取的数据全都打印出来

```python
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
```

结果如下：
