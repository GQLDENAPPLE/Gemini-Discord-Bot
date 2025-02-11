import discord
import os
import google.generativeai as genai
import datetime

# Gemini APIの設定
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-2.0-flash')
chat = model.start_chat(history=[])

# Discordの設定
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

# 許可されたチャンネルIDのリストを環境変数から取得
allowed_channels_str = os.getenv("ALLOWED_CHANNELS", "")
ALLOWED_CHANNELS = [int(ch) for ch in allowed_channels_str.split(",") if ch.isdigit()]

# Botの起動時間を記録
start_time = datetime.datetime.utcnow()

def split_text(text, chunk_size=1500):
    """長いテキストを分割する関数"""
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

@client.event
async def on_ready():
    print(f'{client.user} がオンラインになりました')
    await client.change_presence(activity=discord.Game(name="🍎"))
    await tree.sync()  # スラッシュコマンドを同期

@client.event
async def on_message(message):
    if message.author == client.user or message.author.bot:
        return

    # 許可されたチャンネル以外では無視
    if message.channel.id not in ALLOWED_CHANNELS:
        return

    # 生成中のメッセージを送信
    reply = await message.channel.send("生成中...")

    # Gemini AIにメッセージを送信
    answer = chat.send_message(message.content)

    # 回答を分割し、最初の部分だけ編集、残りは追加送信
    splitted_text = split_text(answer.text)
    await reply.edit(content=splitted_text[0])  # 最初のメッセージを編集
    for chunk in splitted_text[1:]:
        await message.channel.send(chunk)

@tree.command(name="status", description="Botの現在のステータスを表示")
async def status(interaction: discord.Interaction):
    """Botのステータスを表示するスラッシュコマンド"""
    uptime = datetime.datetime.utcnow() - start_time
    latency = round(client.latency * 1000, 2)  # 秒単位なのでミリ秒に変換
    
    embed = discord.Embed(title="ステータス", color=discord.Color.green())
    embed.add_field(name="オンライン時間", value=str(uptime).split('.')[0], inline=False)
    embed.add_field(name="応答速度", value=f"{latency} ms", inline=False)

    await interaction.response.send_message(embed=embed)

client.run(os.environ['DISCORD_TOKEN'])
