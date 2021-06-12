FROM frolvlad/alpine-python3:latest

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENV FLASK_APP='app'

# customization
ENV NAME='Toby Qin'
ENV SITE='https://tobyqin.cn'
ENV MESSAGE='Kitty'
ENV IMAGE=''

EXPOSE 5000
CMD [ "python3", "app.py"]
