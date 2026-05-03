import sys
from pathlib import Path

_root = Path(__file__).resolve().parent.parent
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.users import router as users_router

app = FastAPI(title="MKYrii-App")

app.include_router(auth_router)
app.include_router(users_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}

