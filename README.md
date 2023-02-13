# Проект YaCut и API к нему
Это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

## Ключевые возможности сервиса:
- генерация коротких ссылок и связь их с исходными длинными ссылками,
- переадресация на исходный адрес при обращении к коротким ссылкам.

## Пользовательский интерфейс сервиса — одна страница с формой. Эта форма состоит из двух полей:
- обязательного для длинной исходной ссылки;
- необязательного для пользовательского варианта короткой ссылки.
***
Пользовательский вариант короткой ссылки не должен превышать 16 символов.
Если пользователь предложит вариант короткой ссылки, который уже занят, то уведомление сообщит об этом. Существующая в базе ссылка остается неизменной.
Если пользователь не заполнит поле со своим вариантом короткой ссылки, то сервис сгенерирует её автоматически. Формат для ссылки по умолчанию — шесть случайных символов, в качестве в которых использованы:
- большие латинские буквы,
- маленькие латинские буквы,
- цифры в диапазоне от 0 до 9.
> Автоматически сгенерированная короткая ссылка добавляется в базу данных, но только если в ней уже нет такого же идентификатора. В противном случае генерируется идентификатор заново.
--- 
![screenshot of sample](https://pictures.s3.yandex.net/resources/S01_131_1649172105.png)

# Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/KaterinaSolovyeva/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/MacOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
