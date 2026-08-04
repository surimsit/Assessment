# Stumble Guys Web Automation Framework

This project is an automated test framework for the Stumble Guys website using Python, Playwright, and Pytest.

## Tech Stack

- Python 3.8+
- Playwright
- Pytest
- Page Object Model (POM)
- Gmail IMAP (OTP Retrieval)

---

## Project Structure

```text
Assessment/
│
├── pages/
│   ├── home_page.py
│   ├── login_page.py
│   ├── scopely_login_page.py
│   ├── otp_page.py
│   ├── shop_page.py
│   ├── payment_page.py
│   └── game_page.py
│
├── utils/
│   ├── config.py
│   └── email_helper.py
│
├── tests/
│   └── test_flows.py
│
├── conftest.py
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## Features

- Email OTP Login Automation
- Purchase Flow Validation
- Desktop Web Testing
- Android Mobile Web Testing
- Page Object Model Design
- Automatic OTP Retrieval from Gmail
- Reusable Page Components
- Playwright Browser Automation

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd Assessment
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Playwright Browsers

```bash
playwright install
```

---

## Configuration

Update `utils/config.py` with your test credentials:

```python
TEST_EMAIL = "your_email@gmail.com"
EMAIL_APP_PASSWORD = "your_gmail_app_password"
```

### Gmail App Password Setup

1. Enable 2-Step Verification on your Google Account.
2. Go to Google Account → Security.
3. Open App Passwords.
4. Generate a Mail App Password.
5. Copy the generated password into `EMAIL_APP_PASSWORD`.

---

## Running Tests

### Run All Tests

```bash
pytest
```

### Run Login Test

```bash
pytest tests/test_flows.py::test_login_flow -v
```

### Run Purchase Test

```bash
pytest tests/test_flows.py::test_purchase_flow -v
```

### Run Mobile Login Test

```bash
pytest tests/test_flows.py::test_login_flow_mobile -v
```

### Run WebGL Test

```bash
pytest tests/test_flows.py::test_user_can_launch_webgl_game -v
```

---

## Test Scenarios

### Login Flow

- Open Login Menu
- Continue with Email
- Enter Email Address
- Retrieve OTP from Gmail
- Submit OTP
- Verify Successful Login
- Verify Logout Button Visibility

### Purchase Flow

- Login via OTP
- Navigate to Shop
- Select Item
- Open Purchase Popup
- Verify Purchase Button

### Mobile Login Flow

- Launch Android Mobile Browser
- Login Using Email OTP
- Verify Successful Authentication

### WebGL Game Flow

- Open Play Page
- Wait for Game Load
- Launch WebGL Game
- Complete Age Verification
- Handle Update Popup

---

## Design Principles

### Page Object Model

All locators and page actions are encapsulated within page classes.

Example:

```python
home = HomePage(page)
home.click_login()
```

### Reusable Components

- HomePage
- LoginPage
- ScopelyLoginPage
- OtpPage
- ShopPage
- PaymentPage
- GamePage
- CookieBanner
- EmailHelper

---

## OTP Handling

The framework automatically retrieves OTPs from Gmail using IMAP.

Flow:

1. Capture OTP request timestamp.
2. Poll mailbox for new emails.
3. Read emails received after timestamp.
4. Extract OTP.
5. Submit OTP automatically.

---

## Author

Suresh Chirra

QA Automation Engineer