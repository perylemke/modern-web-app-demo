FROM node:17-alpine

EXPOSE 3000

WORKDIR /frontend_app

COPY ./web_client .

RUN npm ci
RUN npm install

CMD [ "npm", "start" ]