# Тестовое задание About me
## Описание
---
Простой REST-сервис, через которой можно рассказать о себе.

---
## Установка и запуск для тестирования
- Скачайте репозиторий
- Для тестирования необходим k8s
- Создайте пространство имен
  - ```kubectl create ns about```
- Выполните
  - ```kubectl -n about apply =f .kube/```
- Узнайте наименования пода
  - ```kubectl -n about get pods```
- Прокиньте порт
  - ```kubectl -n about port-forward <НАИМЕНОВАНИЕ_ПОДА> 5000:5000```
- Через Postman, выберите метод и выполните запрос на адрес: **localhost:5000/api/aboutme**

---
## Доступные методы
- **GET** */api/aboutme/<nickname>/*
- **POST** */api/aboutme/* со следующими полями:
  - name
  - surname
  - nickname
  - age
  - about_author
- **DELETE** */api/aboutme/<nickname>/*
- **PATCH** */api/aboutme/<nickname>/* c полями, аналогичными post-методу

---
## Автор: Semyonov-K
