install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_all.py

format:
	black *.py

run-uvicorn:
	uvicorn main:app --reload

killweb:
	sudo killall uvicorn

lint:
	pylint --disable=R,C backend.py

dockerbuild:
	docker build -t f1_backend .
	
dockertag:
	docker tag f1_backend:latest 050331820866.dkr.ecr.us-east-1.amazonaws.com/f1_backend:latest

dockerpush:
	docker push 050331820866.dkr.ecr.us-east-1.amazonaws.com/f1_backend:latest

dockerrun:
	docker run -p 8080:8080 050331820866.dkr.ecr.us-east-1.amazonaws.com/f1_backend:latest
