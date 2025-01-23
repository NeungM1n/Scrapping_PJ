# 평택 내 초등학교 급식 정보를 가져오는 정적 스크래핑
# 2025.01.21. created by dHyun

from bs4 import BeautifulSoup
import urllib.request as req
import requests
requests.packages.urllib3.disable_warnings()
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

# 1. 세교초등학교

baseURL = "https://school.koreacharts.com/school/meals/B000009412/contents.html"
res = req.urlopen(baseURL)
soup = BeautifulSoup(res, "html.parser")
meals = soup.find_all(class_="text-center")

target = "요일"
for i, meal in enumerate(meals[28:-3], start=30):  # 인덱스를 1부터 시작
    text = meal.text.strip()
    print(text)

    if target in text:
        print("-" * 50)