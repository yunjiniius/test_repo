from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
import time

# IEDriverServer의 경로를 지정합니다.
service = Service('D:/test_ssp/IEDriverServer.exe')  # IEDriverServer의 실제 파일 경로를 넣어주세요.

# IE 브라우저를 사용하여 webdriver 인스턴스 생성
driver = webdriver.Ie(service=service)

# 네이버 뉴스 페이지로 이동
driver.get('https://news.naver.com')

# 페이지가 완전히 로드될 때까지 기다리기
time.sleep(5)  # 네트워크 상황에 따라 로딩 시간을 조정하세요

try:
    # 최신 뉴스 제목 요소를 찾기 (네이버 뉴스 페이지의 HTML 구조에 따라 클래스 이름을 사용)
    news_headlines = driver.find_elements(By.CLASS_NAME, 'cjs_t')

    # 뉴스 제목 출력
    for headline in news_headlines:
        title = headline.text
        print(f"News Title: {title}")

except Exception as e:
    print("오류 발생:", e)

# 브라우저 종료
driver.quit()
