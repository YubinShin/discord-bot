import os
import requests
import discord
from discord.ext import commands, tasks
import time
from datetime import datetime
import schedule  # 스케줄링을 위한 라이브러리 추가

# GitHub API 토큰 및 디스코드 봇 토큰 설정
GITHUB_TOKEN = "YOUR_GITHUB_TOKEN"
DISCORD_BOT_TOKEN = "YOUR_DISCORD_BOT_TOKEN"
DISCORD_CHANNEL_ID = "YOUR_DISCORD_CHANNEL_ID"

client = discord.Client(intents=discord.Intents.default())

async def send_github_issue_count_once():
    # GitHub API를 사용하여 이슈 가져오기
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}"
    }
    response = requests.get("https://api.github.com/repos/fog-of-war/dev-fe/issues", headers=headers)
    if response.status_code == 200:
        issues = response.json()
        assignee_count = {}
        issue_messages = []  # 이슈 정보를 담을 리스트
        current_date = datetime.now().strftime("%Y-%m-%d")

        for issue in issues:
            assignee = issue["assignee"]["login"] if issue["assignee"] else "담당자 없음"
            if assignee in assignee_count:
                assignee_count[assignee] += 1
            else:
                assignee_count[assignee] = 1

        # 디스코드로 보내기
        channel = client.get_channel(int(DISCORD_CHANNEL_ID))  # 디스코드 채널 ID를 정수로 변환

        # 메시지 생성
        message = f"## 📅 **{current_date}**\n "
        for assignee, count in assignee_count.items():
            message += f"💡 **{assignee}**: {count}개의 이슈가 남아있습니다.\n"
            # message += f"https://github.com/fog-of-war/dev-fe/issues/assigned/{assignee}\n"
            # Collect issue titles within a single code block
            code_block = "```md\n"
            for issue in issues:
                if issue["assignee"] and issue["assignee"]["login"] == assignee:
                    issue_title = issue["title"]
                    code_block += f"{issue_title}\n"
            code_block += "```"
            
            message += code_block
            message += "\n"


        await channel.send(message)

schedule.every().day.at("09:00").do(send_github_issue_count_once)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    
    # 봇 실행 후 한 번만 작업 실행
    await client.change_presence(status=discord.Status.online, activity=discord.Game("감시"))
    # 작업이 완료되면 봇 종료

@client.event
async def on_message(message): # 메세지가 채널에 올라왔을 때 (해당 매세지)
    message_content = message.content 
    greet = message_content.find("인사해") 
    print(greet)
    if greet >= 0:
        await message.channel.send("안녕하세요 감시동균입니다")
    if "누가진짜야" in message_content:
        await message.channel.send("제가 진짜 엉동균입니다")
    if "너누구야" in message_content:
        await message.channel.send("저는 엉동균입니다")
    await client.process_commands(message) # 메세지 중 명령어가 있을 경우 처리해주는 코드    

# 봇 실행
client.run(DISCORD_BOT_TOKEN)
# Run the scheduling loop
while True:
    schedule.run_pending()
    time.sleep(1)  # 스케줄링 루프의 반복 속도를 제어하기 위한 잠시 대기