# Настройка секретов репозитория
#### Заполните GitHub Secrets (Settings → Secrets and variables → Action)
- D_SECRET_KEY = Секретный ключ django
- ENV_DIR = Путь до папки с .env файлами
- SSH_IP_ADDRESS = IP адрес удалённого сервера 
- SSH_KEY = SSH ключ (который начинается на -----BEGIN OPENSSH PRIVATE KEY-----)
- SSH_USER = Имя юзера машины (обычно root)
- WORK_DIR = Путь до папки с проектом (включительно с названием проекта)

# Основные шаги после создания удалённого сервера

1. зайти на сервер и создать открытый и частный ключи ```ssh-keygen -t ed25519 -C "mail@mail.ru"```
2. скопировать содержимое root/.ssh/id_ed25519.pub и вставить в конец root/.ssh/authorized_keys
3. выполнить команды:
- *обновления* 
```commandline
sudo apt update
```
- *установка postgres и инструмент для вирт.окружения* 
```commandline
apt install python3-venv postgresql postgresql-contrib nginx
```

#### *рекомендация: выполнить остановку и запрет на поднятие nginx, так как он будет занимать 80 порт который мы поднимим в контейнере*
```commandline
systemctl stop nginx && systemctl disable nginx
```

4. Установить docker. **<a href="https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository">Инструкция</a>**
5. Установить docker-compose **<a href="https://docs.docker.com/compose/install/linux/">Инструкция</a>**
6. Создать папку для .env файла
```commandline
mkdir /<путь>/<имя папки>
```
7. Скопировать конф.данные из файла .env и поместить в папку шага 6
```commandline
nano /<путь>/<имя папки>/.env
```
8. Для тестов создать отдельный файл с конф данными(единственное отличие от .env это POSTGRES_HOST=localhost)
```commandline
nano /<путь>/<имя папки>/.testenv
```

### Далее можно следовать шагам из титульного README