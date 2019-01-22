FROM python:3.6
ENV PYTHONUNBUFFERED 0

RUN mkdir -p /app
WORKDIR /app

ADD . .
RUN pip install -r requirements.txt

ADD ./run.sh /usr/bin/launch
RUN chmod 755 /usr/bin/launch

EXPOSE 8040

CMD ["/usr/bin/launch"]