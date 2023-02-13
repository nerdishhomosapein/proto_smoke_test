FROM python:3.9
COPY server.py ./
CMD ["python", "server.py"]
