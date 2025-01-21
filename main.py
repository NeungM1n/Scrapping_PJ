# 평택 내 초등학교 급식 정보를 가져오는 정적 스크래핑
# 2025.01.21. created by dHyun

# 1. 세교초등학교

import urllib.request as req
from bs4 import BeautifulSoup

url = "https://sekyo-e.goept.kr/sekyo-e/ad/fm/foodmenu/selectFoodMenuView.do?mi=2520"
date = "2025-12-02"
response = req.urlopen(url+date)
soup = BeautifulSoup(response, "html.parser")
print(soup)