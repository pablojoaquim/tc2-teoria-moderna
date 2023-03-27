# FROM python:3.10-slim-bullseye
FROM python:3.8-slim

RUN mkdir /app
RUN mkdir /app/tst
WORKDIR /app
ADD requirements.txt /app/

# On Alpine, or an Alpine-based docker image, it’s possible to install matplotlib; however it will involve compiling 
# it from source as pip does not provide any pre-compiled binaries. If you don’t mind compiling from source
RUN pip install -r requirements.txt
RUN pip install numpy scipy

ADD /src/ /app/
ADD /tst/ /app/tst/

# EXPOSE 5000
# For developing purposes we may use the werkzeug embedded web server of Flask
CMD ["python", "/app/main.py"]

# For production we should use a WSGI (web server gateway interface) like gunicorn which is the recommended way for Flask
# 'workers' means processes, 'threads' means the number of threads per worker
# CMD ["gunicorn", "main:webserver", "--workers=1", "--threads=2", "-b 0.0.0.0:5000"]
#Another option is to use coroutines using gevent
# CMD ["gunicorn", "main:webserver", "--workers=1", "--threads=1", "--worker-class=gevent", "--worker-connections=2", "-b 0.0.0.0:5000"]