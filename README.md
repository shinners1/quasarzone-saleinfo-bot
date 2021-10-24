# Quasarzone sale info board alarm
퀘이사존(https://quasarzone.com)의 할인 정보 게시판 새 글 알림입니다.  
게시판 주소: https://quasarzone.com/bbs/qb_saleinfo

### Install Dependency
```shell
python3 -m pip install -r requirements.txt
```

### Run
```shell
python3 check_saleinfo_board.py
```

### CONFIGCancel changes
+ configure your crawler before you run the script
+ check_saleinfo_board.py, line:81-84
```python
CHECK_INTERVAL_MIN = 10

telegram_bot_id = ''
telegram_bot_token = ''
```
