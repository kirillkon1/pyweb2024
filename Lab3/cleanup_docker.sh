#!/bin/bash

echo "Начинаем очистку Docker..."

# 1. Удаление конкретного контейнера по его ID или имени
docker rm my_container 2>/dev/null

# 2. Удаление нескольких контейнеров по их ID
docker rm container_id1 container_id2 container_id3 2>/dev/null

# 3. Автоматическое удаление контейнера после его завершения
docker run --rm ubuntu:latest echo "Запущен временный контейнер Ubuntu"

# 4. Удаление висячих образов (неиспользуемые и нетегированные)
docker image prune -f

# 5. Удаление неиспользуемых сетей
docker network prune -f

# 6. Удаление образов по имени или ID
docker rmi my_image 2>/dev/null

# 7. Удаление всех контейнеров, созданных до определённой даты (старше 24 часов)
docker ps -a --filter "until=24h" -q | xargs -r docker rm

# 8. Удаление всех контейнеров (включая остановленные)
docker ps -a -q | xargs -r docker rm

# 9. Остановка всех запущенных контейнеров
# shellcheck disable=SC2046
docker stop $(docker ps -q) 2>/dev/null

# 10. Удаление всех завершённых контейнеров
# shellcheck disable=SC2046
docker rm $(docker ps -a -f status=exited -q) 2>/dev/null

# 11. Удаление контейнера и всех связанных с ним анонимных томов
docker rm -v my_container 2>/dev/null

echo "Очистка Docker завершена."
