# так же берём готовый контейнер с node на основе alpine
FROM node:18-alpine
# Задаем рабочий каталог
WORKDIR /usr/src/app
# Копируем туда наши json файлы
ADD *.json ./
# Устанавливаем все пакеты и зависимости указанные в json
RUN npm install
# Добавляем каталоги public и src.
ADD ./public ./public
ADD ./src ./src