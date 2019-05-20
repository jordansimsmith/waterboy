.PHONY: clean build deploy

clean:
	rm -rf build/

build:
	mkdir -p build/
	cp *.py build/
	pip install -r requirements.txt -t build/

deploy:
	scp build/ pi@waterboy.local:/home/pi/waterboy
