# Основные шаги после создания удалённого сервера

1. зайти на сервер и создать открытый и частный ключи ```ssh-keygen -t ed25519 -C "mail@mail.ru"```
2. скопировать содержимое root/.ssh/id_ed25519.pub и вставить в конец root/.ssh/authorized_keys
3. выполнить команды
- *обновления* ```sudo apt update```
- *установка postgres и инструмент для вирт.окружения* ```apt install python3-venv postgresql postgresql-contrib nginx```
<br><br>
#### *рекомендация: выполнить остановку и запрет на поднятие nginx, так как он будет занимать 80 порт который нам понадобится*
```systemctl stop nginx && systemctl disable nginx```

4. Установить docker. **<a href="https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository">Инструкция</a>**
5. Установить docker-compose **<a href="https://docs.docker.com/compose/install/linux/">Инструкция</a>**
6. 