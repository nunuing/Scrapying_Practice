# import requests
# from bs4 import BeautifulSoup

# # # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
# # url = "https://brand.naver.com/espoir/products/10123826918"
# # req = Request(url,headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'})
# # webpage = urlopen(req)
# # soup = BeautifulSoup(webpage, 'html5lib')

# # # objects = soup.select("._2L3vDiadT9")
# # # print(len(objects))

# headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
# url = "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000184222&t_page=%ED%86%B5%ED%95%A9%EA%B2%80%EC%83%89%EA%B2%B0%EA%B3%BC%ED%8E%98%EC%9D%B4%EC%A7%80&t_click=%EA%B2%80%EC%83%89%EC%83%81%ED%92%88%EC%83%81%EC%84%B8&t_search_name=%EC%97%90%EC%8A%A4%EC%81%98%EC%95%84&t_number=5&dispCatNo=1000001000200010009&trackingCd=Result_5"
# response = requests.get(url, headers=headers)
# response.raise_for_status()

# soup = BeautifulSoup(response.text, "html5lib")
# print(soup.find('title').string)

# tags = soup.select(".review_cont")
# print(len(tags))
# # tags = soup.select(attrs = {'class':'_2L3vDiadT9'})
# # for t in tags :
# #     print(t.text)
# # tags = soup.select('span')

# # tags = soup.select("#REVIEW > div > div._2LvIMaBiIO > div._2g7PKvqCKe > ul > li > div > div > div > div._3-1uaKhzq4 > div > div > div._3z6gI4oI6l > div > span")
# #REVIEW > div > div._2LvIMaBiIO > div._2g7PKvqCKe > ul > li:nth-child(2) > div > div > div > div._3-1uaKhzq4 > div > div > div._3z6gI4oI6l > div > span

# # for t in tags :
# #     print(t.text)

