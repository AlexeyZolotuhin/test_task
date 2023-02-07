FROM python:3.9-alpine

RUN adduser -D taskuser
WORKDIR /home/taskuser

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app app
COPY configs configs
COPY main.py .

USER taskuser
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]