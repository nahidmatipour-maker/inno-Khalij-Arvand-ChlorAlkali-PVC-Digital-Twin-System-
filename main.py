# main.py
# نقطه ورود اصلی برنامه

from fastapi import FastAPI

app = FastAPI(
    title="سامانه سلامت زنجیره اروند",
    description="سامانه پایش سلامت سلول‌های الکترولیز و پیش‌بینی فولینگ",
    version="0.1.0"
)

@app.get("/")
def read_root():
    return {"message": "سامانه سلامت زنجیره اروند فعال است."}

@app.get("/health")
def health_check():
    return {"status": "سالم"}
