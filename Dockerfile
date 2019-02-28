FROM debian:jessie
RUN apt-get update && apt-get install -y \
	python3 \
	python3-pip\	
	git \
	nano 
	
RUN git clone https://github.com/EricKrg/RestfulFLASK && cd RestfulFLASK && ls && pip3 install -r requirements.txt 
EXPOSE 5000
CMD cd RestfulFLASK; python3 app.py	
