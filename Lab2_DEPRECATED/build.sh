#!/bin/bash

# Установить скрипт, чтобы завершиться при ошибке
set -e

# Функция для вывода сообщений
echo_info() {
    echo -e "\033[1;34m$1\033[0m"
}

echo_info "Начало сборки сайта с помощью MkDocs..."
cd ./project
mkdocs build --clean
echo_info "Сборка MkDocs завершена."

# Объединение CSS файлов
echo_info "Объединение CSS файлов..."
COMBINED_CSS="site/assets/css/combined.min.css"
cat site/assets/css/bulma.min.css site/assets/css/custom.css > $COMBINED_CSS
echo_info "CSS файлы объединены в $COMBINED_CSS."

# Минификация объединенного CSS файла
echo_info "Минификация CSS файла..."
python3 -c "
import csscompressor
with open('$COMBINED_CSS', 'r') as f:
    css = f.read()
minified_css = csscompressor.compress(css)
with open('$COMBINED_CSS', 'w') as f:
    f.write(minified_css)
"
echo_info "CSS файл минимизирован."

# Замена ссылок на объединенный CSS в HTML файлах
echo_info "Обновление ссылок на CSS в HTML файлах..."
find site -name "*.html" -type f | while read -r file; do
    sed -i '' 's|assets/css/bulma.min.css|assets/css/combined.min.css|g' "$file"
    sed -i '' '/assets\/css\/custom.css/d' "$file"
done
echo_info "Ссылки на CSS обновлены."

# Минификация HTML файлов
echo_info "Минификация HTML файлов..."
for html_file in $(find site -name "*.html"); do
    python -c "
import htmlmin
with open('$html_file', 'r', encoding='utf-8') as f:
    html = f.read()
minified_html = htmlmin.minify(html, remove_empty_space=True)
with open('$html_file', 'w', encoding='utf-8') as f:
    f.write(minified_html)
"
    echo_info "Минифицирован $html_file."
done
echo_info "Все HTML файлы минимизированы."

echo_info "Сборка и оптимизация завершены успешно."
