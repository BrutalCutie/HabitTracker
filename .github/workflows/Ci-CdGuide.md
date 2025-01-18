# Основные шаги после создания удалённого сервера

1. зайти на сервер и ввести ```ssh-keygen -t ed25519 -C "mail@mail.ru"```
2. скопировать содержимое root/.ssh/id_ed25519.pub в root/.ssh/authorized_keys
3. выполнить команды
4. ```sudo apt update```
5. ```apt install python3-venv postgresql postgresql-contrib nginx```


#### описать установку докера 