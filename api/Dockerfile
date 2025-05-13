
FROM python:3.9

LABEL name="SchoolTimetable-server"

WORKDIR /app


COPY requirements.txt .

COPY main.py .


RUN pip install -r requirements.txt


COPY . .

EXPOSE 53
EXPOSE 27017
EXPOSE 8080

CMD ["python", "main.py"]
