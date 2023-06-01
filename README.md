# match3_autotest


Создание и активация вертуального окружения
https://pythonchik.ru/okruzhenie-i-pakety/virtualnoe-okruzhenie-python-venv

-- При первом скачивании проекта необходимо установить зависимости 
при активированном вертуальном окружении из файла

```sh
pip install -r requirements.txt
```

Обновленная библиотека airtest может вызывать конфлитк при установке из requirements.txt. Если установка прошла успешно, пропускаем шаги обновления менеджера и ручной установки либы. Если усатновить завивисмотсти из файла не получилось делаем следующее:
1. обновляем менеджер пакетов
```sh
python -m pip install --upgrade pip
```
2. пробуем установить пакет airtest c завиммостями напрямую из интернетов
```sh
pip install airtest
```

Для проверки установки выполняем 
```sh
pip freeze
```

Должен быть такой список библиотек:
```sh
airtest==1.2.10.2
cached-property==1.5.2
certifi==2023.5.7
charset-normalizer==3.1.0
comtypes==1.2.0
decorator==5.1.1
Deprecated==1.2.14
facebook-wda==1.4.6
ffmpeg-python==0.2.0
filelock==3.12.0
future==0.18.3
idna==3.4
Jinja2==3.1.2
MarkupSafe==2.1.2
mss==6.1.0
