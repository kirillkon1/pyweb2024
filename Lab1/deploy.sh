#!/bin/bash

# Конфигурация
HOST="se.ifmo.ru"
PORT=2222
USER="s000000"
PASSWORD=""
LOCAL_BUILD_DIR="my-project-docs/site"
REMOTE_DIR="public_html/mkdocs-test"


# Выполнение сборки документации
mkdocs build

# Проверка успешности сборки
if [ $? -ne 0 ]; then
    echo "Ошибка при сборке MkDocs."
    exit 1
fi

# Проверка наличия sshpass
if ! command -v sshpass &> /dev/null
then
    echo "sshpass не установлен. Пожалуйста, установите sshpass и попробуйте снова."
    exit 1
fi

# Проверка наличия директории билда
if [ ! -d "$LOCAL_BUILD_DIR" ]; then
    echo "Директория билда '$LOCAL_BUILD_DIR' не найдена. Выполняю сборку..."
    mkdocs build
    if [ $? -ne 0 ]; then
        echo "Ошибка при сборке MkDocs."
        exit 1
    fi
fi

# Создание удалённой директории
echo "Создаю удалённую директорию '$REMOTE_DIR' (если не существует)..."
sshpass -p "$PASSWORD" ssh -p $PORT $USER@$HOST "mkdir -p $REMOTE_DIR"
if [ $? -ne 0 ]; then
    echo "Не удалось создать директорию на удалённом сервере."
    exit 1
fi

# Копирование файлов на сервер
echo "Копирую файлы в '$REMOTE_DIR'..."
sshpass -p "$PASSWORD" scp -P $PORT -r $LOCAL_BUILD_DIR/* $USER@$HOST:$REMOTE_DIR
if [ $? -ne 0 ]; then
    echo "Не удалось скопировать файлы на удалённый сервер."
    exit 1
fi

echo "Деплой завершён успешно."
