import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import index
from app.routes.emotion import emotion

def create_app():
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],  # 필요에 따라 특정 origin만 허용하도록 설정 가능
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(index.router, tags=['index'])
    app.include_router(emotion.router, tags=['emotion'])

    return app
    
app = create_app()

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)