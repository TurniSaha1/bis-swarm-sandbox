from fastapi import FastAPI

from app.routers import quizzes


def create_app() -> FastAPI:
    application = FastAPI(title="bis-swarm-sandbox")
    application.include_router(quizzes.router)
    return application


app = create_app()
