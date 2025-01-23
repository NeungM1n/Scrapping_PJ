# 평택 내 중학교 급식 정보를 가져오는 정적 스크래핑
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
baseURL = "https://school.koreacharts.com/school/meals/B000009412/202412.html"
res = req.urlopen(baseURL)
soup = BeautifulSoup(res, "html.parser")

def find_target(target):
    meals = soup.find_all(class_="text-center")
    found = False

    for i, meal in enumerate(meals):
        if meal.text.strip() == target:
            found = True
            try:
                print(meal.text.strip())
                print(meals[i + 1].text.strip())
                print(meals[i + 2].text.strip())
            except IndexError:
                print("급식 정보가 충분하지 않습니다.")
            break

    if not found:
        print("해당 날짜의 급식 정보가 없습니다.")

day_food = input("어떤 날짜의 급식을 알고 싶나요? ").strip()
find_target(day_food)