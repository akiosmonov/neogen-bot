FROM python:3.11-slim
WORKID /add
COPY . .
RUN pip install --no-cache-dir -r requirements.tzt
CMD ["python", "main.py"]
