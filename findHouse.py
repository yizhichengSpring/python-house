import requests
from lxml import etree
import csv

class findHouse(object):
    # 模拟浏览器请求
    def getFakerRequestHeaders(self):
        headers = {
             'Accept': '* / *',
             'Accept - Encoding': 'gzip, deflate',
             'Accept - Language': 'zh - CN, zh;q = 0.9',
             'Connection': 'keep - alive',
             'Cookie': 'gr_user_id=bc7f0f06-29be-47d7-96af-619102605f07; BJ_nlist=%7B%2261618038%22%3A%7B%22id%22%3A%2261618038%22%2C'
                      '%22sell_price%22%3A3570%2C%22title%22%3A%22%5Cu660c%5Cu5e73%5Cu56de%5Cu9f99%5Cu89c28%5Cu53f7%5Cu7ebf%5Cu80b2%5'
                      'Cu77e5%5Cu8def%5Cu4e91%5Cu8da3%5Cu56ed%5Cu4e00%5Cu533a3%5Cu5c45%5Cu5ba4-%5Cu5357%5Cu5367%22%2C%22add_time%22%3A'
                      '1534826874%2C%22usage_area%22%3A15.4%2C%22floor%22%3A%223%22%2C%22floor_total%22%3A%226%22%2C%22room_photo%22%3'
                      'A%22g2m1%5C%2FM00%5C%2F29%5C%2F97%5C%2FChAFBltv8cmAYT2cAAMV6v8i0FQ786.JPG%22%2C%22city_name%22%3A%22%5Cu5317%5Cu'
                      '4eac%22%7D%2C%2261481144%22%3A%7B%22id%22%3A%2261481144%22%2C%22sell_price%22%3A2390%2C%22title%22%3A%22%5Cu660c%'
                      '5Cu5e73%5Cu56de%5Cu9f99%5Cu89c2%5Cu660c%5Cu5e73%5Cu7ebf%2C8%5Cu53f7%5Cu7ebf%5Cu6731%5Cu8f9b%5Cu5e84%5Cu4e03%5Cu71'
                      'd5%5Cu8def1%5Cu53f7%5Cu96623%5Cu5c45%5Cu5ba4-%5Cu5357%5Cu5367%22%2C%22add_time%22%3A1534826868%2C%22usage_area%22%'
                      '3A10.2%2C%22floor%22%3A%223%22%2C%22floor_total%22%3A%2221%22%2C%22room_photo%22%3A%22g2%5C%2FM00%5C%2F60%5C%2FA9%'
                      '5C%2FChAFD1tKDByAGgQEABa8dnaZRk4969.jpg%22%2C%22city_name%22%3A%22%5Cu5317%5Cu4eac%22%7D%2C%2261396269%22%3A%7B%22i'
                      'd%22%3A%2261396269%22%2C%22sell_price%22%3A4330%2C%22title%22%3A%22%5Cu660c%5Cu5e73%5Cu660c%5Cu5e73%5Cu5176%5Cu5b83'
                      '%5Cu660c%5Cu5e73%5Cu7ebf%5Cu660c%5Cu5e73+%5Cu6c34%5Cu5173%5Cu65b0%5Cu67512%5Cu5c45%5Cu5ba4-%5Cu5357%5Cu5367%22%2C%22'
                      'add_time%22%3A1534826824%2C%22usage_area%22%3A15.6%2C%22floor%22%3A%225%22%2C%22floor_total%22%3A%226%22%2C%22room_ph'
                      'oto%22%3A%22g2%5C%2FM00%5C%2F43%5C%2F3C%5C%2FChAFfVs8r8GAQi3UAATyGZ6mGBI703.JPG%22%2C%22city_name%22%3A%22%5Cu5317%5Cu'
                      '4eac%22%7D%2C%2261540760%22%3A%7B%22id%22%3A%2261540760%22%2C%22sell_price%22%3A9590%2C%22title%22%3A%22%5Cu671d%5Cu963'
                      '3%5Cu592a%5Cu9633%5Cu5bab10%5Cu53f7%5Cu7ebf%5Cu592a%5Cu9633%5Cu5bab%5Cu4e07%5Cu65b9%5Cu666f%5Cu8f691%5Cu5c45%5Cu5ba4-%5C'
                      'u4e1c%5Cu5357%5Cu5367%22%2C%22add_time%22%3A1534826641%2C%22usage_area%22%3A12.65%2C%22floor%22%3A%222%22%2C%22floor_tota'
                      'l%22%3A%2218%22%2C%22room_photo%22%3A%22g2%5C%2FM00%5C%2F83%5C%2F05%5C%2FChAFD1tYh5WAQAPGAAU5N4q4FwU967.JPG%22%2C%22city_'
                      'name%22%3A%22%5Cu5317%5Cu4eac%22%7D%2C%2261596030%22%3A%7B%22id%22%3A%2261596030%22%2C%22sell_price%22%3A2190%2C%22title%22'
                      '%3A%22%5Cu660c%5Cu5e73%5Cu660c%5Cu5e73%5Cu5176%5Cu5b83%5Cu660c%5Cu5e73%5Cu7ebf%5Cu660c%5Cu5e73%5Cu7ad9%5Cu91d1%5Cu9685%5Cu4e'
                      '07%5Cu79d1%5Cu57ce3%5Cu5c45%5Cu5ba4-%5Cu5357%5Cu5367%22%2C%22add_time%22%3A1534825786%2C%22usage_area%22%3A14.4%2C%22floor%22%3'
                      'A%2218%22%2C%22floor_total%22%3A%2228%22%2C%22room_photo%22%3A%22g2m1%5C%2FM00%5C%2F40%5C%2F09%5C%2FChAFB1t41HGAQNb8AAiL2WIG7D47'
                      '30.JPG%22%2C%22city_name%22%3A%22%5Cu5317%5Cu4eac%22%7D%2C%2261541760%22%3A%7B%22id%22%3A%2261541760%22%2C%22sell_price%22%3A2590%'
                      '2C%22title%22%3A%22%5Cu660c%5Cu5e73%5Cu56de%5Cu9f99%5Cu89c2%5Cu660c%5Cu5e73%5Cu7ebf%2C8%5Cu53f7%5Cu7ebf%5Cu6731%5Cu8f9b%5Cu5e84%5Cu'
                      '6731%5Cu8f9b%5Cu5e84%5Cu5317%5Cu533a4%5Cu5c45%5Cu5ba4-%5Cu5357%5Cu5367%22%2C%22add_time%22%3A1534825548%2C%22usage_area%22%3A13.6%2C'
                      '%22floor%22%3A%226%22%2C%22floor_total%22%3A%226%22%2C%22room_photo%22%3A%22g2m1%5C%2FM00%5C%2F3F%5C%2F71%5C%2FChAFB1t4LCqAdW3qAAh3xzt'
                      'dS8A374.JPG%22%2C%22city_name%22%3A%22%5Cu5317%5Cu4eac%22%7D%7D; gr_session_id_8da2730aaedd7628=4a80fe81-3448-4918-a026-022a74abb920; '
                      'gr_session_id_8da2730aaedd7628_4a80fe81-3448-4918-a026-022a74abb920=true; mapType=%20; CURRENT_CITY_CODE=110000; Hm_lvt_038002b56790c09'
                      '7b74c818a80e3a68e=1534825467,1535677908,1535677929,1535678266; passport_token=ac0be0e4-c0c8-420f-bd1f-11337e7e1efc; uid=8fd51f74-7928-4b'
                      'a4-8aff-2572f5de42bb; Hm_lpvt_038002b56790c097b74c818a80e3a68e=1535678400',
            'Host': 'www.ziroom.com',
            'Referer': 'http://www.ziroom.com/z/nl/z2-d23008611.html?p=1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        return headers

    def getData(self,page):
       findHous = findHouse()
       headers = findHous.getFakerRequestHeaders()
       r1 = requests.get('http://www.ziroom.com/z/nl/z2-d23008611.html?p='+str(page)+'',headers=headers)
       return r1.text



    def parseValue(self,result):
        html = etree.HTML(result,etree.HTMLParser())
        #小区
        house = html.xpath('//div[@class="txt"]//h3//a[@class="t1"]/text()')
        #小区地址
        address = html.xpath('//div[@class="txt"]//h4//a//text()')
        #详细信息
        detail = html.xpath('//div[@class="detail"]//p//span//text()')
        #缩略图
        img = html.xpath('//div[@class="img pr"]//a//img//@_src')
        #详情
        href = html.xpath('//div[@class="img pr"]//a//@href')
        houseInfo = {'house':house,'address':address,'detail':detail,'img':img,'href':href}
        return houseInfo

    def combinationValue(self,houseInfo,page):
        houseList =houseInfo.get("house")
        addressList = houseInfo.get("address")
        detailList = houseInfo.get("detail")
        imgList = houseInfo.get("img")
        hrefList = houseInfo.get("href")
        name = "自如房源"+str(page)+".csv"
        with open(name, 'w',newline= '') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['小区名称', '具体地址', '面积','楼层','户型','交通' '缩略图', '房源详情'])
            for i in range(0,18):
                detils = detailList[i * 4:(i * 4) + 4]
                writer.writerow([houseList[i], addressList[i], detils[0],detils[1],detils[2],detils[3], "http:"+imgList[i], "http:"+hrefList[i]])
        print("---------------------------------end-------------------------------------")


for i in range(1,7):
    house = findHouse()
    result = house.getData(i)
    houseInfo = house.parseValue(result)
    house.combinationValue(houseInfo,i)

