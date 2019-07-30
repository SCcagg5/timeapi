FROM python:latest AS BACK_END

LABEL maintainer="Courtel Eliot"
LABEL maintainermail="eliot.courtel@wanadoo.fr"

WORKDIR /home/api
RUN apt-get install git -y


ENTRYPOINT ls;\
		 pip install --upgrade pip && \
	   pip install --upgrade -r requirements.txt && python3 server.py;
