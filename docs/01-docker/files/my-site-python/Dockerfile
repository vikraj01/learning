FROM python:3.12-slim
WORKDIR /site
COPY index.html .
RUN date > built-at.txt
EXPOSE 8000
CMD ["python", "-m", "http.server", "8000"]
