FROM python:3.9
WORKDIR /app
COPY sign_in.py .
RUN pip install requests
CMD ["python", "sign_in.py"]
