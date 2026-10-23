FROM node:24-slim
WORKDIR /app
RUN npm install express pg
COPY app.js .
CMD ["node", "app.js"]
