FROM node:24-slim
WORKDIR /app
RUN npm install express redis
COPY app.js .
CMD ["node", "app.js"]
