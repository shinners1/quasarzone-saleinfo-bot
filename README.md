# Quasarzone sale info board alarm
퀘이사존(https://quasarzone.com) 의 할인 정보 게시판 새 글 알림입니다.  
게시판 주소: https://quasarzone.com/bbs/qb_saleinfo

### Install Dependency
```shell
python3 -m pip install -r requirements.txt
```

### Run
```shell
python3 check_saleinfo_board.py
```

### Configuration
사용 전에 **check_saleinfo_board.py, line:81-84**에서 알람을 전송할 텔레그램의 id와 token을 입력하고 알림 주기를 설정해주세요.  
  
```python
CHECK_INTERVAL_MIN = 10

telegram_bot_id = ''
telegram_bot_token = ''
```
