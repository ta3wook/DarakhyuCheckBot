from playwright.sync_api import sync_playwright
from datetime import datetime
import requests
import os

# 설정
target_date = "2025-06-21"
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
# TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID").split(";")

def send_telegram_message(message):
    for chat_id in TELEGRAM_CHAT_ID:
        chat_id = chat_id.strip()
        if not chat_id:
            continue
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        data = {"chat_id": chat_id, "text": message}
        try:
            requests.post(url, data=data)
        except Exception as e:
            print(f"❗ {chat_id}에게 메시지 전송 실패:", e)

def check_booking():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            viewport={"width": 1920, "height": 1080},
            locale="ko-KR",
            extra_http_headers={
                "Accept-Language": "ko-KR,ko;q=0.9",
                "Referer": "https://www.google.com/",
            }
        )
        page = context.new_page()
        page.goto("https://be4.wingsbooking.com/IAT2", timeout=60000)

        # 디버그용 출력
        page.screenshot(path="headless_bypass.png")
        with open("headless_bypass.html", "w", encoding="utf-8") as f:
            f.write(page.content())

        # 달력 트리거 시도
        try:
            page.click('#start-day', force=True)
        except Exception:
            pass

        page.wait_for_timeout(3000)

        selector = f'td[data-enabledate="{target_date}"]'

        try:
            page.wait_for_selector(selector, timeout=10000)
            td = page.query_selector(selector)
            class_attr = td.get_attribute("class") if td else "missing"

            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if "disabled" in class_attr:
                msg = f"❌ [{now}] {target_date} 예약 불가"
            else:
                msg = f"✅ [{now}] {target_date} 예약 가능! 🎉"

            print(msg)
            send_telegram_message(msg)

        except Exception as e:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            msg = f"⚠️ [{now}] 날짜 셀 탐색 실패: {e}"
            print(msg)
            send_telegram_message(msg)

        browser.close()

if __name__ == "__main__":
    check_booking()