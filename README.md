# Chatting_Room_channels
![Image](https://github.com/user-attachments/assets/04a70ae8-6fa6-4d9b-b554-f108183d9f6f)

---

## 🌟 **Project Goals**

**_Django + Channels로 간단 채팅방 Toy Project._**

---

## 🛠️ **Technology Stack**

- **Backend**: Django (Python) + Channels
- **Frontend**: HTML, CSS, JavaScript, Bootstrap5
- **Database**: SQLite3 (-> PostgreSQL soon...)
- **Real-Time Communication**: WebSockets (for real-time communication)

---

## 🖥️ **Getting Started**

Clone the repository and set up locally:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/ChanLim-BD/Chatting_Room_channels.git
   ```

2. **Install Dependencies**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set Up the Database**

   ```bash
   python manage.py migrate
   ```

4. **Run the Server**

   ```bash
   python manage.py runserver            # 개발 서버
   uvicorn ChatRoom.asgi:application     # 운영 서버 
   ```

5. Open your browser and navigate to: `http://localhost:8000/`.
---

## 📷 ScreenShot

![Image](https://github.com/user-attachments/assets/34156ae1-5231-4738-98f7-b65daae1ec0e)

---

## 🌍 **Future Enhancements**

* DB 변경 (SQLite3 to PostgreSQL)
* Containerized
* Github Action을 통한 CI 적용

<br>

* 채팅 로비에서 유저수 노출
* 채팅방에서 마지막 유저가 나가면 채팅방 자동 삭제
* 각 메세지에 시각, 유저명, 유저 아바타 노출
* 채팅방에 새로운 유저가 들어오면, 최근 메세지 5개 보여주기
* 메세지 수정/삭제
* 메세지 입력 중에 "{유저명}님이 메세지 입력 중입니다." 메세지
* 메세지 리액션 : 좋아요.
* 파일/사진 업로드
* 채팅방에 비밀번호 설정하기
* 채팅방 입장신청하고, 허용한 유저만 입장하기
* 유저 로그아웃 시에, 참여 중인 채팅방에서 자동 나가기