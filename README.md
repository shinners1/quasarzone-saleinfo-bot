# Quasarzone sale info board alarm

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
