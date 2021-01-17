import requests
import re
from bs4 import BeautifulSoup

# 기업에 대한 정보를 크롤링하는 함수입니다.
def crawling(soup):
    #1.주어진 url 내의 데이터를 크롤링하여 종목명,현재가,전일비,등락률이 담긴 리스트 stock을 출력
    stock = []
    stock_list = soup.find("table", attrs={"class": "type_5"}).find("tbody").find_all("tr")

    for st in stock_list:
        st = st.get_text().split()
        stock.append(st)
    for i in range(35):
        del stock[i][1] #*제거
        stock[i] = stock[i][0:4] #종목명, 현재가, 전일비, 등락률만 
    
    #빈리스트제거
    stock = [x for x in stock if x]
    #print(stock)
    
    #2. 등락률이 +인 종목을 찾아 종목명과 현재가로 이루어진 딕셔너리 data
    data = dict()
    for i in range(35):
        if stock[i][3][0]=='+':
            #print(result[i][0],result[i][1])
            data[stock[i][0]] = int(stock[i][1].replace(",",""))#정수 자료형
            
    #3.현재가가 오름차순이 되도록 
    data = sorted(data.items(), key=lambda x:x[1]) 
    #print(data)
    return data
    
    
def main() :
    url = "https://finance.naver.com/sise/sise_group_detail.nhn?type=upjong&no=235"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    print(crawling(soup))

if __name__ == "__main__" :
    main()
