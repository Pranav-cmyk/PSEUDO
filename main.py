from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routers import generate_router


templates = Jinja2Templates(directory="./templates")
app = FastAPI()
app.mount("/static", StaticFiles(directory="./static"), name="static")
app.include_router(generate_router)

origins = [
    "http://localhost:8000", 
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

