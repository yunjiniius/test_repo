from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# ChromeDriver의 경로를 지정합니다.
service = Service('D:/test_ssp/chromedriver-win64/chromedriver.exe')  # chromedriver의 실제 파일 경로를 넣어주세요.

# Chrome 브라우저를 사용하여 webdriver 인스턴스 생성
driver = webdriver.Chrome(service=service)

# 동행복권 홈페이지 메인으로 접속 (get 함수)
driver.get('https://dhlottery.co.kr/common.do?method=main')

# 이번 회차 번호를 확인해보겠습니다
# find_element는 () 안의 조건에 맞는 요소 중 첫번째를 반환합니다
num_view = driver.find_element(By.ID, 'numView')

# numView 아래에 있는 모든 요소들을 리스트로 받습니다
# 그리고 find_elements는 조건에 맞는 모든 요소를 반환합니다
num_comp = num_view.find_elements(By.XPATH, "*")

# text는 해당 요소에 포함된 텍스트를 반환합니다
numbers = [c.text for c in num_comp[1:7]] 
bonus = num_comp[-1].text # 보너스 숫자도 빼먹으면 안됨
print(numbers, bonus) # [21, 26, 27, 32, 34, 42], 31

# 브라우저 뒤로가기
driver.back()