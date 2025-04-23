#  Rate Limiting in Microservice API



## GOAL
Implement and demonstrate an efficient **rate-limiting system** within the microservice to:
- Protect against excessive load
- Enforce per-user or per-IP quotas
- Ensure fair usage among clients

---

## 🧠 Algorithm Used: **Token Bucket**

### ✅ Why Token Bucket?
- Allows short bursts while enforcing an average rate
- Simple to implement and supports replenishing requests over time
- Flexible and production-ready

### 🪣 How Token Bucket Works:
- Each user/IP has a bucket with tokens (e.g., 100 tokens)
- Every request consumes 1 token
- Tokens are refilled at a constant rate (e.g., 1 token/second)
- If no tokens are available → Request is rejected with HTTP 429

---

## ⚙️ Configuration
| Parameter        | Value                        |
|------------------|-------------------------------|
| Max Tokens       | 100 tokens/IP                 |
| Refill Rate      | 1 token/sec                   |
| Window           | Sliding, ~100 requests per 100 seconds |
| Storage          | In-memory (slowapi), Redis optional |
| Exceed Action    | HTTP 429: Too Many Requests   |

---

## 🏗️ Implementation Stack
- **Language**: Python 3.12
- **Framework**: FastAPI
- **Rate-limiter**: `slowapi` using Token Bucket logic
- **Local server**: `uvicorn`

---

## 📁 Project Structure
```
├── main.py              # Main application with rate limiting
├── requirements.txt     # Dependencies
├── .gitignore           # Files to exclude from Git
└── README.md            # This file
```

---

## 🚀 How to Run
### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the app
```bash
uvicorn main:app --reload
```

Visit in browser: [http://localhost:8000/api/v1/data](http://localhost:8000/api/v1/data)

---

## 🧪 Testing the Rate Limit
Try the endpoint multiple times or use a curl loop:
```bash
for i in {1..150}; do curl http://localhost:8000/api/v1/data; done
```
After 100 requests in 100 seconds, you’ll get:
```json
{"error":"Rate limit exceeded: 100 per 100 second"}
```

---

## 📦 GitHub Repository
[https://github.com/jaxylykovm/rate-limit-microservice](https://github.com/jaxylykovm/rate-limit-microservice)

---

## ✅ Conclusion
This microservice implements a simple but powerful Token Bucket-based rate limiter using `slowapi` to defend the API against request bursts and ensure fair usage. The architecture is extendable for distributed environments (via Redis) and ready for production scenarios.

