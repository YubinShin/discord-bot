<img width="505" alt="스크린샷 2023-10-31 오후 10 44 33" src="https://github.com/YubinShin/discord-bot/assets/68121478/bffe0c13-90cc-4095-a011-721e7f12d16c">


# 프로젝트 실행 가이드

이 프로젝트는 Discord 봇을 실행하는 데 사용됩니다. 아래의 단계를 따라 프로젝트를 설정하고 실행하세요.

## 환경 설정

1. 이 저장소를 클론합니다:

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

## 봇 사용

봇이 실행되면 Discord 서버에서 다음과 같이 명령어를 입력할 수 있습니다.

인사해: 봇이 인사합니다.
누가진짜야: 봇이 진짜 팀원을 사칭합니다.
너누구야: 봇이 팀원을 사칭합니다.
