import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        # Microsoft Edge (Chromium 기반) 브라우저 실행
        browser = await p.chromium.launch(
            executable_path="C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",  # Edge 브라우저 실행 경로
            headless=False  # False로 설정하면 브라우저 창이 열립니다.
        )
        
        # 새로운 브라우저 컨텍스트 생성
        context = await browser.new_context()

        # 새로운 페이지 열기
        page = await context.new_page()

        # 네이버 뉴스 페이지로 이동
        await page.goto('https://news.naver.com')

        # 페이지가 로드될 때까지 대기 (뉴스 제목 클래스가 로드될 때까지)
        await page.wait_for_selector('.cjs_t')

        # 뉴스 제목 요소들 찾기
        headlines = await page.query_selector_all('.cjs_t')

        # 뉴스 제목 출력
        for headline in headlines:
            title = await headline.text_content()
            print(f"News Title: {title.strip()}")

        # 브라우저 종료
        # await browser.close()
        

# 비동기 함수 실행
asyncio.run(main())
