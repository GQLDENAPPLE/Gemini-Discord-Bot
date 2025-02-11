FROM python:3.9-slim

WORKDIR /app

# 必要なパッケージをインストール
COPY requirements.txt .
RUN pip install -r requirements.txt

# コードをコンテナにコピー
COPY . .

# アプリケーションの起動
CMD ["python", "main.py"]