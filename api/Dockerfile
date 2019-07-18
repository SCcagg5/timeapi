FROM python:3.7 AS BACK_END

LABEL maintainer="Courtel Eliot"
LABEL maintainermail="eliot.courtel@wanadoo.fr"

WORKDIR /home/api
RUN apt-get install git -y


ENTRYPOINT ls;\
	   pip3 install -r requirements.txt && python3 server.py > /dev/null; \
	   /bin/bash
