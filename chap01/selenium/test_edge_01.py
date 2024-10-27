

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

# EdgeDriver의 경로를 지정합니다.
service = Service('D:/test_ssp/msedgedriver.exe')  # msedgedriver의 실제 파일 경로를 넣어주세요.

# Edge 브라우저를 사용하여 webdriver 인스턴스 생성
driver = webdriver.Edge(service=service)

# Timetree 캘린더 페이지로 이동
driver.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%8B%AC%EB%A0%A5')

# 페이지가 완전히 로드될 때까지 기다리기
time.sleep(10)  # 페이지 로딩 시간을 여유롭게 잡습니다.

try:
    # 일정 항목을 찾기 (실제 HTML 구조를 분석하여 적절한 클래스나 ID를 사용해야 합니다)
    # 예를 들어, 모든 일정 항목을 가진 클래스가 'event-item'이라고 가정합니다.
    events = driver.find_elements(By.CLASS_NAME, 'event-item')  

    # 일정 내용 추출
    for event in events:
        # 각 일정의 제목과 시간 가져오기 (예를 들어, 'title' 및 'time' 클래스가 있다고 가정)
        title = event.find_element(By.CLASS_NAME, 'title').text
        time_element = event.find_element(By.CLASS_NAME, 'time').text
        print(f"Title: {title}, Time: {time_element}")

except Exception as e:
    print("오류 발생:", e)

# 브라우저 종료
driver.quit()
