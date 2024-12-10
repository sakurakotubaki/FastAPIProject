# 書籍管理API仕様書

## ベースURL
```
http://localhost:8000
```

## 認証

### 認証方式
Bearer認証（JWTトークン）を使用

### リクエストヘッダー
保護されたエンドポイントにアクセスする際は、以下のヘッダーが必要：
```
Authorization: Bearer <access_token>
```

## エンドポイント一覧

### 認証関連

#### ログイン（アクセストークン取得）
```
POST /token
```

**リクエスト（application/x-www-form-urlencoded）**
```
username: string
password: string
```

**レスポンス**
```json
{
  "access_token": "string",
  "token_type": "bearer"
}
```

**ステータスコード**
- 200: 成功
- 401: 認証失敗

### ユーザー関連

#### ユーザー登録
```
POST /users/
```

**リクエスト**
```json
{
  "username": "string",
  "email": "string",
  "password": "string"
}
```

**レスポンス**
```json
{
  "id": "integer",
  "username": "string",
  "email": "string",
  "books": []
}
```

**ステータスコード**
- 200: 成功
- 400: メールアドレスまたはユーザー名が既に使用されている

#### 現在のユーザー情報取得
```
GET /users/me/
```

**認証**: 必要

**レスポンス**
```json
{
  "id": "integer",
  "username": "string",
  "email": "string",
  "books": [
    {
      "id": "integer",
      "title": "string",
      "description": "string",
      "owner_id": "integer"
    }
  ]
}
```

**ステータスコード**
- 200: 成功
- 401: 認証失敗

#### ユーザー一覧取得
```
GET /users/
```

**クエリパラメータ**
```
skip: integer (デフォルト: 0) - スキップする件数
limit: integer (デフォルト: 100) - 取得する最大件数
```

**レスポンス**
```json
[
  {
    "id": "integer",
    "username": "string",
    "email": "string",
    "books": []
  }
]
```

### 書籍関連

#### 書籍登録
```
POST /books/
```

**認証**: 必要

**リクエスト**
```json
{
  "title": "string",
  "description": "string"
}
```

**レスポンス**
```json
{
  "id": "integer",
  "title": "string",
  "description": "string",
  "owner_id": "integer"
}
```

**ステータスコード**
- 200: 成功
- 401: 認証失敗

#### 書籍一覧取得
```
GET /books/
```

**クエリパラメータ**
```
skip: integer (デフォルト: 0) - スキップする件数
limit: integer (デフォルト: 100) - 取得する最大件数
```

**レスポンス**
```json
[
  {
    "id": "integer",
    "title": "string",
    "description": "string",
    "owner_id": "integer"
  }
]
```

#### 特定の書籍取得
```
GET /books/{book_id}
```

**パスパラメータ**
```
book_id: integer - 書籍ID
```

**レスポンス**
```json
{
  "id": "integer",
  "title": "string",
  "description": "string",
  "owner_id": "integer"
}
```

**ステータスコード**
- 200: 成功
- 404: 書籍が見つからない

#### 書籍更新
```
PUT /books/{book_id}
```

**認証**: 必要

**パスパラメータ**
```
book_id: integer - 書籍ID
```

**リクエスト**
```json
{
  "title": "string",
  "description": "string"
}
```

**レスポンス**
```json
{
  "id": "integer",
  "title": "string",
  "description": "string",
  "owner_id": "integer"
}
```

**ステータスコード**
- 200: 成功
- 401: 認証失敗
- 403: 権限なし（他のユーザーの書籍）
- 404: 書籍が見つからない

#### 書籍削除
```
DELETE /books/{book_id}
```

**認証**: 必要

**パスパラメータ**
```
book_id: integer - 書籍ID
```

**レスポンス**
```json
{
  "message": "Book deleted successfully"
}
```

**ステータスコード**
- 200: 成功
- 401: 認証失敗
- 403: 権限なし（他のユーザーの書籍）
- 404: 書籍が見つからない

## エラーレスポンス

すべてのエラーレスポンスは以下の形式で返されます：

```json
{
  "detail": "エラーメッセージ"
}
```

## レート制限
現在、レート制限は実装されていません。

## CORS
すべてのオリジンからのリクエストを許可しています（開発環境向け）。
本番環境では適切なオリジンの設定が必要です。
