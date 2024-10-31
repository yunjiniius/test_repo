import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 가상의 사용자 데이터
data = {
    '사용자': ['사용자1', '사용자2', '사용자3', '사용자4'],
    '해당월 데이터 입력 여부': [True, False, True, False],
    '이메일': ['user1@example.com', 'user2@example.com', 'user3@example.com', 'user4@example.com']
}

df = pd.DataFrame(data)

# 필터링
missing_data_users = df[df['해당월 데이터 입력 여부'] == False]

# 이메일 전송 설정
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_user = "y@gmail.com"
smtp_password = "0000"

# 이메일 전송
def send_email(to_email, user_name):
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = to_email
    msg['Subject'] = "데이터 입력 요청"

    body = f"안녕하세요, {user_name}님.\n해당월의 데이터를 아직 입력하지 않으셨습니다. 빠른 시일 내에 데이터를 입력해 주시기 바랍니다."
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, to_email, msg.as_string())
            print(f"이메일이 {to_email}으로 성공적으로 전송되었습니다.")
    except Exception as e:
        print(f"이메일 전송 실패: {e}")

for _, row in missing_data_users.iterrows():
    send_email(row['이메일'], row['사용자'])
