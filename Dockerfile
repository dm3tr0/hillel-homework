FROM python

WORKDIR /hillel-homework

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]