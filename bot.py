import os
import requests
import discord
from discord.ext import commands, tasks
import time
from datetime import datetime
import schedule  

# GitHub API 토큰 및 디스코드 봇 토큰 설정
# ---------------------------------------------
GITHUB_TOKEN = "YOUR_GITHUB_TOKEN"
DISCORD_BOT_TOKEN = "YOUR_DISCORD_BOT_TOKEN"
DISCORD_CHANNEL_ID = "YOUR_DISCORD_CHANNEL_ID"


# 디스코드 봇 인스턴스를 생성, Intent 는 디폴트로 설정해주었다.
# ---------------------------------------------
client = discord.Client(intents=discord.Intents.default())


# 매일 깃허브 이슈를 체크하고 디스코드 채널에 메시지를 보내는 함수
# ---------------------------------------------
async def send_github_issue_count_once():
    # GitHub API를 사용하여 이슈 가져오기
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}"
    }
    response = requests.get("https://api.github.com/repos/fog-of-war/dev-fe/issues", headers=headers)

    # 응답의 상태코드가 200이라면 assignee 별로 내용을 가공하게 만들었다.
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

        # 디스코드 채널 ID를 정수로 변환
        channel = client.get_channel(int(DISCORD_CHANNEL_ID)) 

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

        # 채널에 가공 완료한 메시지 전송
        await channel.send(message)


# 매일 오전 9시에 이슈 카운트 함수 실행
# ---------------------------------------------
schedule.every().day.at("09:00").do(send_github_issue_count_once)


# discord.py 에서 제공하는 어노테이션으로 이벤트를 설정한다.
# ---------------------------------------------
@client.event
async def on_ready(): # 인스턴스가 준비 되었을 때
    print(f'Logged in as {client.user}')

    await client.change_presence(status=discord.Status.online, activity=discord.Game("감시"))

@client.event
async def on_message(message): # 메세지가 채널에 올라왔을 때 (해당 매세지)
    message_content = message.content 
    greet = message_content.find("인사해") 
    if greet >= 0:
        await message.channel.send("안녕하세요 감시동균입니다")
    if "누가진짜야" in message_content:
        await message.channel.send("제가 진짜 엉동균입니다")
    if "너누구야" in message_content:
        await message.channel.send("저는 엉동균입니다")
    await client.process_commands(message) # 메세지 중 명령어가 있을 경우 처리해주는 코드    


# 봇 실행
# ---------------------------------------------
client.run(DISCORD_BOT_TOKEN)


# 스케줄링 설정
# ---------------------------------------------
while True:
    schedule.run_pending()
    time.sleep(1)  # 스케줄링 루프의 반복 속도를 제어하기 위한 잠시 대기
