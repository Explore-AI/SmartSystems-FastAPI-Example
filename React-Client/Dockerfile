FROM node:16-alpine as node
WORKDIR /client-app
COPY package*.json  /client-app/
RUN npm ci 
COPY . /client-app
CMD ["npm", "start"]docker