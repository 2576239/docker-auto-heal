FROM python:3.13-slim   

WORKDIR /app

COPY . .

RUN pip install docker
ENV PYTHONUNBUFFERED=1

CMD ["python","auto_heal_pro.py"]