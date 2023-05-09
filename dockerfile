FROM python:3.11

WORKDIR ./

COPY . .

RUN -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]