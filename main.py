from fastapi import FastAPI, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

app = FastAPI()

# Token Bucket: 100 запросов на 100 секунд на IP
limiter = Limiter(key_func=get_remote_address, default_limits=["100/100seconds"])
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.get("/api/v1/data")
@limiter.limit("100/100seconds")
async def get_data(request: Request):
    return {"message": "✅ Success! You are within the rate limit."}
