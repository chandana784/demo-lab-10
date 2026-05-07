FROM python:3.11-slim
WORKDIR /file
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY file.py
EXPOSE 5000
CMD ["Python","file.py"]
