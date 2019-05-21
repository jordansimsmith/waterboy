.PHONY: clean build deploy

clean:
	rm -rf build/

build:
	mkdir -p build/
	cp -r listeners/ *.py build/
	pip install -r requirements.txt -t build/

deploy:
	rsync -av --delete build/ pi@waterboy.local:/home/pi/waterboy
