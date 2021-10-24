# Quasarzone sale info board alarm
[퀘이사존 지름/할인정보 게시판](https://quasarzone.com/bbs/qb_saleinfo) 새 글 알림입니다.  
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fnerdroid-labs%2Fquasarzone-saleinfo-bot&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

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
