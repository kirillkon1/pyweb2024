# Лабораторная работа №3. Анализ команд для автоматизации работы с Docker

## Топ-10 (11) команд Docker для очистки и оптимизации

1. **Удаление конкретного контейнера по его ID или имени**:
   ```bash
   docker rm my_container
   ```
   
2. **Удаление нескольких контейнеров по их ID**:
   ```bash
   docker rm container_id1 container_id2 container_id3
   ```

3. **Автоматическое удаление контейнера после его завершения:**
   ```bash
   docker run --rm ubuntu:latest
   ```

4. **Удаление висячих образов:** Удаляет образы без тегов и неиспользуемые.
   ```bash
   docker image prune -f
   ```

5. **Удаление неиспользуемых сетей**: Удаляет Docker-сети, которые не используются.
   ```bash
   docker network prune -f
   ```

6. **Удаление образов по имени или ID**: Например, удаление всех версий образа my_image, не затрагивая другие образы.
   ```bash
   docker rmi my_image
   ```

7. **Удаление всех контейнеров, созданных до определённой даты**: Например, удаление контейнеров, созданных более 24 часов назад.
   ```bash
   docker ps -a --filter "until=24h" -q | xargs docker rm
   ```

8. **Удаление всех контейнеров**: Полностью удаляет все контейнеры, включая остановленные.
   ```bash
   docker ps -a -q | xargs docker rm
   ```

9. **Остановить один и более контейнеров**:
   ```bash
   docker stop
   ```
   **Остановить все запущенные контейнеры**:   
   ```bash
    docker stop $(docker ps -a -q)
   ```
   
10. **Удаление всех завершенных контейнеров**:
   ```bash
   docker rm $(docker ps -a -f status=exited -q)
   ```

11. **Удалить указанный контейнер и все связанные с ним анонимные тома (volume)**:
   ```bash
    docker rm -v my_container
   ```


### Источники
- https://docs.docker.com/engine/manage-resources/pruning/
- https://tproger.ru/translations/top-10-docker-commands
- https://romankurnovskii.com/ru/posts/docker-commands/
- https://docs.vscale.io/blog/how-to-cleanup-docker/
- https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes-ru