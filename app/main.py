import uvicorn
from fastapi import FastAPI
from app.routers import main_router
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI(middleware=[
 Middleware(SessionMiddleware, secret_key='super-secret')

])
app.include_router(main_router)



if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
