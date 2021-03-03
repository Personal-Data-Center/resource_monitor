FROM python

COPY run.sh /run.sh

RUN chmod +x run.sh

RUN pip3 install django-admin mysqlclient  pdc-dev psutil

RUN mkdir blank

CMD ["/run.sh"]
