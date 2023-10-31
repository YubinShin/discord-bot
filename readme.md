


# 프로젝트 실행 가이드

이 프로젝트는 Discord 봇을 실행하는 데 사용됩니다. 아래의 단계를 따라 프로젝트를 설정하고 실행하세요.

## 환경설정

디스코드 봇 생성<br/>
https://discord.com/developers/applications<br/>
https://velog.io/@dombe/문제-해결-그리고-기본적인-Discord-bot-만들기<br/>

디스코드 개발자모드 및 채널id 구하는 법<br/>
https://helpdeskgeek.com/how-to/how-to-enable-and-use-developer-mode-on-discord/<br/>

깃허브 access_token 생성<br/>
https://hoohaha.tistory.com/37<br/>

## 실행 가이드

1. 이 저장소를 클론합니다

   ```sh
    git clone https://github.com/YubinShin/discord-bot.git
    cd discord-bot
   ```
   
2. 가상 환경을 생성&활성화 후 의존성들을 설치합니다.

     Mac/linux
     ```sh
     python -m venv myenv
     source myenv/bin/activate
     pip install -r requirements.txt
     ```
   
     Window
     ```sh
     python -m venv myenv
     myenv\Scripts\activate
     pip install -r requirements.txt
     ```

3. 터미널에 하단 내용을 입력하여 Discord 봇 토큰 및 다른 환경 변수를 설정합니다.

     ```sh
     set GITHUB_TOKEN=your_github_token
     set DISCORD_BOT_TOKEN=your_discord_bot_token
     set DISCORD_CHANNEL_ID=your_discord_channel_id
     ```

4. 봇을 실행합니다.

     ```sh
     python bot.py
     ```
### 백그라운드 세션에서 실행

1. 새로운 screen 세션을 시작합니다.

   ```sh
   screen -S my_session_name
   ```

2. Python 스크립트를 실행합니다.

   ```sh
   python bot.py
   ```

3. 스크린 세션을 종료합니다.<br/>
   Ctrl + A, 그리고 누른 다음, d 키를 누르면 세션을 백그라운드로 보낼 수 있습니다.<br/>
   스크린 세션을 나중에 다시 찾으려면 "screen -r my_session_name"을 사용합니다.

## 봇 사용

- 봇이 실행되면 Discord 서버에 오전 9시마다 깃허브 저장소의 이슈를 트래킹 해줍니다.

<img width="643" alt="스크린샷 2023-10-31 오후 11 17 01" src="https://github.com/YubinShin/discord-bot/assets/68121478/5ee25f7b-f26b-4646-aefc-5dffac010a16"><br/>

- 봇이 실행되면 Discord 봇이 항상 감시하는 중이라는 표시를 띄워 서버에 긴장감을 줄 수 있습니다.

<img width="240" alt="스크린샷 2023-10-31 오후 11 23 42" src="https://github.com/YubinShin/discord-bot/assets/68121478/282570ae-7669-4a9c-89c8-7a5c002fa26e"><br/>

- 봇이 실행되면 Discord 서버에서 다음과 같이 명령어를 입력할 수 있습니다.

   인사해: 봇이 인사합니다. <br/>
   누가진짜야: 봇이 팀원을 사칭합니다.<br/>
   너누구야: 봇이 팀원을 사칭합니다.<br/>

<img width="505" alt="스크린샷 2023-10-31 오후 10 44 33" src="https://github.com/YubinShin/discord-bot/assets/68121478/bffe0c13-90cc-4095-a011-721e7f12d16c"><br/>
