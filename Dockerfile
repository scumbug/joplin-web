FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR  /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY joplin_web /app

EXPOSE 8001
CMD ["python", "/app/app.py"]