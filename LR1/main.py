from connection import init_db
from controllers.user_controller import router as user_router

app = FastAPI()


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/")
def hello():
    return "Hello, [username]!"


app.include_router(user_router)