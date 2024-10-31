import schedule
import time
from test import print_temp

# 매월 25일 오전 9시에 스케줄링
def job():
    if time.localtime().tm_mday == 31:
        print_temp()

schedule.every().day.at("22:24").do(job)

# 스케줄러 실행
while True:
    schedule.run_pending()
    time.sleep(60)

