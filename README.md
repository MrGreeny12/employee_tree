## Организационная структура. Domio

### Задание:

- Необходимо разработать веб-страницу, которая будет отображать иерархию сотрудников в древовидной форме, с ФИО и должностью. У каждого сотрудника есть один и только один руководитель.
- База данных должна содержать не менее 50 000 сотрудников и 5 уровней иерархии. Заполнить её можно случайными данными.
- Редактирование/добавление сущностей с проверкой корректности введённых данных.
- Требований по оформлению самой страницы — нет. Приемлем любой опрятный вариант.
- Проект необходимо развернуть на любом желаемом хостинге для демонстрации.


### Развёртывание системы

- Скопировать репозиторий на локальную машину
- Установить пакеты ```pip3 install requirements.txt```
- Запустить миграции ```./manage.py migrate```
- Запустить локальный сервер ```./manage.py runserver```


### Демонстрация на Heroku

Ссылка - https://ancient-atoll-02784.herokuapp.com/