.PHONY: clean build deploy

IDENTITY_FILE=~/.ssh/waterboy_rsa
HOST=pi@waterboy.local

clean:
	rm -rf build/

build:
	mkdir -p build/
	cp -r listeners/ *.py .env build/
	pip install -r requirements.txt -t build/

deploy:
	# stop service if it exists
	ssh -i ${IDENTITY_FILE} ${HOST} \
	 	"! sudo systemctl status waterboy.service || \
	 	sudo systemctl stop waterboy.service"

	# copy files
	rsync -av -e "ssh -i ${IDENTITY_FILE}" --delete build/ ${HOST}:/home/pi/waterboy
	
	# copy service
	rsync -av -e "ssh -i ${IDENTITY_FILE}" --rsync-path="sudo rsync" \
	 	waterboy.service ${HOST}:/lib/systemd/system/waterboy.service

	# start service
	ssh -i ${IDENTITY_FILE} ${HOST} \
		"sudo systemctl daemon-reload && \
		sudo systemctl enable waterboy.service && \
		sudo systemctl start waterboy.service"
