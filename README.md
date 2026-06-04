# TradeBridge Python SDK

The TradeBridge Python SDK provides a simple way to integrate with TradeBridge APIs and access authentication, portfolio, order, reports, chart, and contract master services.

---

# Prerequisites

Before using the SDK, ensure you have:

- Python 3.8 or later installed
- A valid TradeBridge API Key
- Valid Client Credentials
- Internet connectivity to access TradeBridge APIs

---

# Installation

Clone the repository and install dependencies:

```bash
pip install -r requirements.txt
```

---

# SDK Configuration

Open the example file:

```text
swagger_client/sample/example.py
```

Update the API Key:

```python
api_key = "YOUR_API_KEY"
source = "SDK"
```

Replace:

```text
YOUR_API_KEY
```

with the API Key provided by Arihant.

---

# Authentication

Most APIs require a valid Access Token.

## Step 1: Login

Open:

```text
swagger_client/sample/example.py
```

Update your credentials:

```python
login_body = LoginRequest(
    userId="YOUR_CLIENT_ID",
    password="YOUR_PASSWORD"
)
```

Enable the Login API block and corresponding print statement.

Run:

```bash
python swagger_client/sample/example.py
```

The response will contain:

```text
txnId
```

Copy the `txnId`.

---

## Step 2: Verify OTP

Update the Verify OTP request with:

```python
userId
txnId
otp
```

Enable the Verify OTP API block and corresponding print statement.

Run:

```bash
python swagger_client/sample/example.py
```

The response will contain:

```text
accessToken
refreshToken
```

Copy the Access Token.

---

## Step 3: Configure Access Token

Update:

```python
accessToken = "YOUR_ACCESS_TOKEN"
```

Replace:

```text
YOUR_ACCESS_TOKEN
```

with the token received from OTP verification.

Authenticated APIs require:

```python
accessToken
```

to be configured before execution.

---

# Running API Examples

All API examples are available in:

```text
swagger_client/sample/example.py
```

Open the example file and update the required credentials and request parameters.

To test an API:

1. Enable the API request block.
2. Enable the corresponding print statement.
3. Run the example file.

Example:

```python
# Holdings API
holdings_response = positionControllerAPI.do_holdings(
    accessToken,
    api_key,
    source
)[0]
```

Enable the corresponding print statement:

```python
print("HOLDINGS_RESPONSE: \n", holdings_response, "\n\n")
```

Run:

```bash
python swagger_client/sample/example.py
```

The response will be printed in the console.

---

# Updating Request Parameters

Before running an API, update the request parameters according to your account and use case.

Common parameters include:

```text
userId
password
otp
txnId
accessToken
refreshToken
symbol
exchange
instrument
excToken
quantity
price
orderId
fromDate
toDate
```

Refer to the corresponding API example in:

```text
swagger_client/sample/example.py
```

---

# Typical Usage Flow

```text
1. Configure API Key
2. Open swagger_client/sample/example.py
3. Run Login API
4. Copy txnId
5. Run Verify OTP API
6. Copy accessToken
7. Update accessToken in swagger_client/sample/example.py
8. Enable the API you want to test
9. Enable the corresponding print statement
10. Run python swagger_client/sample/example.py
11. The response will be printed in the console
```

---

# Notes

- Ensure a valid Access Token is configured before calling authenticated APIs.
- Access Tokens may expire and need to be regenerated using Login and OTP verification.
- All request and response examples are available in:

```text
swagger_client/sample/example.py
```

- Update request values before execution based on your trading account and requirements.
- Enable the API and its corresponding print statement before execution.
