from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db.database import engine
from db import models
from router import users, books, auth

# データベースのテーブルを作成
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="書籍管理API",
    description="FastAPIを使用した書籍管理システムのAPI",
    version="1.0.0"
)

# CORSの設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 本番環境では適切なオリジンを指定する
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ルーターの登録
app.include_router(auth.router)  # 認証関連のルーター
app.include_router(users.router)  # ユーザー関連のルーター
app.include_router(books.router)  # 書籍関連のルーター
