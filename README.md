# Lexicom Test


_👀 Инструкция по установке и запуску:_

[![](misc/demo.gif)](https://mkosir.github.io/react-parallax-tilt/?path=/story/react-parallax-tilt--glare-effect)

## [Тестовое Lexicom 💥](https://github.com/ivanIStereotekk/lexicom.git)

## Install
1 - Клонируем репозиторий к себе на локальную машину
```bash
gh repo clone ivanIStereotekk/lexicom
```
2 - Запускаем docker-compose скрипт
```bash
docker compose up
```

_👀 В течении минуты кластер дожен заработать._

## Features




# REDIS   
# FASTAPI
# PYDANTIC
# Docker-compose

----------------------------
# ЗАДАНИЕ 2 с SQL запросами на нормализацию данных

# Вариант 1

Копирование из двух таблиц в новую таблицу
```sql
SELECT short_names.status, full_name.name
INTO organised_names
FROM short_names
LEFT JOIN full_names ON full_names.name = short_names.name

```
...тем самым мы создаем новую нормализованную таблицу с нужными данными.

# Вариант 2
Копирование из одной таблицы набор данных где данные в колонках будут содержать паттерн имен 

```sql
INSERT INTO full_names (status)
SELECT status FROM short_names
WHERE full_names.names LIKE short_names.names;
```





