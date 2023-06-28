FROM python:3.11

RUN mkdir /itfox
WORKDIR /itfox

COPY requirements.txt /itfox/
RUN pip install -r requirements.txt

COPY . /itfox/

EXPOSE 8000

CMD ["gunicorn", "itfox.wsgi"]
