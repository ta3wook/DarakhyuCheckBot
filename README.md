# DarakhyuCheckBot

> ** 다락휴 예약 확인 봇**  
> Playwright 기반 자동화 스크립트로 특정 날짜의 예약 가능 여부를 확인하고, 결과를 Telegram으로 알림 전송합니다.

---

## 📌 기능

- **Playwright**를 사용해 웹사이트에 자동 접속 및 예약 페이지 탐색
- 지정한 날짜(`target_date`)에 대해 **예약 가능 여부 확인**
- **Telegram Bot API**를 통해 실시간 알림 발송 (다중 사용자 지원)

---

## 📁 프로젝트 구조

```
DarakhyuCheckBot/
├── check_booking_playwright.py    # 예약 확인 및 알림 전송 메인 스크립트
├── requirements.txt               # 의존 패키지 목록
└── .github/
    └── workflows/
        └── booking-check.yml     # GitHub Actions 자동 실행 설정 (CI)
```

---

## ⚙️ 설치 및 실행

### 1. Python 패키지 설치

```bash
pip install -r requirements.txt
```

### 2. 환경 변수 설정

다음 환경 변수를 `.env` 또는 시스템에 설정해 주세요:

- `TELEGRAM_TOKEN`: 텔레그램 봇 토큰
- `TELEGRAM_CHAT_ID`: 수신할 사용자 ID (여러 명은 `;`로 구분)

예시:

```env
TELEGRAM_TOKEN=123456:ABCDEF...
TELEGRAM_CHAT_ID=111111111;222222222
```

### 3. 예약 확인 실행

```bash
python check_booking_playwright.py
```

스크립트 실행 시 지정한 날짜(`target_date`)의 예약 가능 여부를 자동 확인하고, 알림을 전송합니다.

---

## 🤖 GitHub Actions 자동 실행

`.github/workflows/booking-check.yml` 워크플로우를 통해 GitHub Actions에서 주기적으로 스크립트를 실행하도록 설정할 수 있습니다.

---

## 🧾 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다.
