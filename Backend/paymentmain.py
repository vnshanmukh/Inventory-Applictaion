from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Routers import inventory,payment
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(payment.router)