# 書籍管理API

FastAPIを使用した書籍管理APIです。JWT認証とCRUD操作を提供します。

## 環境構築

必要なパッケージをインストール：

```bash
pip install "fastapi[all]"
```

## サーバーの起動

```bash
uvicorn main:app --reload
```

サーバーが起動したら、以下のURLでSwagger UIにアクセスできます：
http://127.0.0.1:8000/docs

## Swagger UIでの認証手順

### 1. ユーザー登録（SignUp）

1. `/auth/signup` エンドポイントを展開
2. "Try it out" ボタンをクリック
3. Request bodyに以下のJSONを入力：
   ```json
   {
     "username": "testuser",
     "email": "test@example.com",
     "password": "password123"
   }
   ```
4. "Execute" ボタンをクリック
5. Response bodyで登録されたユーザー情報を確認

### 2. ログイン（SignIn）

1. `/auth/signin` エンドポイントを展開
2. "Try it out" ボタンをクリック
3. フォームデータを入力：
   - username: testuser
   - password: password123
4. "Execute" ボタンをクリック
5. Response bodyで返されたトークンを確認：
   ```json
   {
     "access_token": "eyJhbGciOiJIUzI1...",
     "refresh_token": "eyJhbGciOiJIUzI1...",
     "token_type": "bearer"
   }
   ```
6. `access_token`の値をコピー

### 3. 認証の設定

1. Swagger UI右上の "Authorize" ボタンをクリック
2. 表示されたダイアログに以下の形式でトークンを入力：
   ```
   Bearer eyJhbGciOiJIUzI1...
   ```
   ※ "Bearer "の後に、コピーした`access_token`を貼り付け
3. "Authorize" ボタンをクリック
4. "Close" ボタンをクリック

### 4. 書籍の操作（認証必須）

これ以降の操作には認証が必要です。上記の手順で認証を行ってから実行してください。

#### 書籍の登録

1. `/books/` (POST) エンドポイントを展開
2. "Try it out" ボタンをクリック
3. Request bodyに以下のJSONを入力：
   ```json
   {
     "title": "テスト書籍",
     "description": "これはテスト用の書籍です"
   }
   ```
4. "Execute" ボタンをクリック
5. Response bodyで登録された書籍情報を確認

#### 書籍一覧の取得

1. `/books/` (GET) エンドポイントを展開
2. "Try it out" ボタンをクリック
3. "Execute" ボタンをクリック
4. Response bodyで書籍一覧を確認

### 5. ログアウト（SignOut）

1. `/auth/signout` エンドポイントを展開
2. "Try it out" ボタンをクリック
3. "Execute" ボタンをクリック
4. ログアウト後、トークンは無効になります

## トークンの更新

アクセストークンの有効期限が切れた場合（30分後）：

1. `/auth/refresh` エンドポイントを展開
2. "Try it out" ボタンをクリック
3. Request bodyにリフレッシュトークンを入力：
   ```json
   {
     "refresh_token": "eyJhbGciOiJIUzI1..."
   }
   ```
4. "Execute" ボタンをクリック
5. 新しいアクセストークンとリフレッシュトークンを取得

## エラー対処

### 401 Unauthorized

このエラーが発生する場合：
1. ログインしているか確認
2. トークンが正しく設定されているか確認
3. トークンの有効期限が切れていないか確認

### 403 Forbidden

このエラーが発生する場合：
- 他のユーザーのリソースにアクセスしようとしている

### 404 Not Found

このエラーが発生する場合：
- 指定したIDのリソースが存在しない

## セキュリティ情報

- アクセストークン有効期限: 30分
- リフレッシュトークン有効期限: 7日間
- パスワードはbcryptでハッシュ化
- JWTによる認証
- CORS対応済み
