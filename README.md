# Gemini Discord Bot

DiscordでAIと会話ができるBotのソースコードです。\
Gemini APIを利用して、リアルタイムで応答するBotを構築しています。

Discord Botの作成から実行までのチュートリアルも用意していますので、ぜひ参考にしてください！

---

## ✨ 機能

- Gemini 2.0 Flashを使用した自然な会話
- 指定したチャンネルでのみ動作する機能
- スラッシュコマンド `/status` によるBotのステータス確認

---

## 🗂️ ファイル構成

| ファイル名              | 説明                          |
| ------------------ | --------------------------- |
| `main.py`          | Gemini Discord Botのメインスクリプト |
| `Dockerfile`       | Dockerコンテナとして実行するための設定ファイル  |
| `requirements.txt` | 必要なPythonライブラリのリスト          |

---

## ⚙️ 環境変数

このBotを動作させるには、以下の環境変数を設定する必要があります。

| 変数名                | 説明                         |
| ------------------ | -------------------------- |
| `DISCORD_TOKEN`    | Discord Botのトークン           |
| `GEMINI_API_KEY`   | Gemini APIのキー       |
| `ALLOWED_CHANNELS` | DiscordのチャンネルID（カンマ区切りで指定） |

---

## 🤖 Discord Botの作成方法

### 1️⃣ Discord Developer Portalでアプリケーションを作成

1. [Discord Developer Portal](https://discord.com/developers/applications) にアクセスし、Discordアカウントでログイン。
2. `New Application` をクリックし、Botの名前を入力して `Create` をクリック。

### 2️⃣ Botの作成

1. 左側のメニューから `Bot` を選択。
2. `Reset Token` をクリックしてトークンを取得。（後で使用するためメモしておく）
3. `Privileged Gateway Intents` の `MESSAGE CONTENT INTENT` を有効化。

### 3️⃣ Botの招待

1. 左側の `OAuth2` → `OAuth2 URL Generator` を開く。
2. `SCOPES` で `bot` にチェックを入れる。
3. `BOT PERMISSIONS` で以下の権限を選択。（必要に応じて他の権限も選択）
   - View Channels
   - Send Messages
4. 生成されたURLをコピーし、ブラウザで開いてBotをサーバーに追加。

---

## 🔑 DiscordのチャンネルIDの取得方法

1. Discordの `設定` → `詳細設定` で `開発者モード` を有効化。
2. IDを取得したいチャンネルを右クリックし、`IDをコピー` を選択。

---

## 🔑 Google Gemini APIキーの取得方法

1. [Google AI Studio](https://aistudio.google.com/) にアクセスし、Googleアカウントでログイン。
2. `Get API Keys` をクリック。
3. APIキーを作成をクリックし、`Gemini API` を選択。
4. 作成されたAPIキーをコピーする（後で使用するためメモしておく）。

---

## 🚀 実行方法

### 💻 ローカル環境で実行する場合

1. 必要なライブラリをインストール。
   ```sh
   pip install -r requirements.txt
   ```
2. 環境変数を設定（`.env` ファイルを作成するか、ターミナルで設定）。
   ```sh
   export DISCORD_TOKEN='あなたのDiscordトークン'
   export GEMINI_API_KEY='あなたのGemini APIキー'
   export ALLOWED_CHANNELS='チャンネルID,チャンネルID'
   ```
3. Botを起動。
   ```sh
   python main.py
   ```
4. DiscordでBotがオンラインになっているか確認。

---

### 🚀 Replitで一時的に実行させたい場合（練習環境向け）

1. [Replit](https://replit.com/) にログインし、`Create App` をクリック。
2. `Python` テンプレートを選択し、プロジェクト名を入力して `Create App` をクリック。
3. `main.py` の中身のコードをコピー＆ペースト。
4. 左側の `Secrets (環境変数)` を開き、以下の3つを追加。
   - `DISCORD_TOKEN`: Discord Botのトークン
   - `GEMINI_API_KEY`: Google Gemini APIキー
   - `ALLOWED_CHANNELS`: 許可するチャンネルID（カンマ区切り）
5. `Run` ボタンをクリックしてBotを起動。
6. DiscordでBotがオンラインになっているか確認。

⚠ **注意:** Replitのブラウザページを閉じるとBotがオフラインになります。

---

### 🌍 Koyeb & Northflankで24時間稼働させたい場合（本番環境向け）

24時間常時稼働させたい場合は、GitHubと連携してセットアップできる `Koyeb` または `Northflank` がおすすめです。\
どちらも無料のホスティングサービスですが、Northflankではアカウント認証のためにクレジットカードの登録が必要です。

🔗 **参考記事:**

- [【Koyeb】Discord Botを無料で24時間運用](https://zenn.dev/amano_spica/articles/24c5f288cf9595)
- [NorthflankでDiscord Botを無料で常時起動](https://zenn.dev/radian462/articles/22ab327b58dda9)

---

## 📚 参考資料

- [Gemini API  |  Google AI for Developers](https://ai.google.dev/gemini-api/docs?hl=ja)

---

## 📜 ライセンス

このプロジェクトは `MITライセンス` の下で提供されています。詳細については `LICENSE` ファイルをご確認ください。
