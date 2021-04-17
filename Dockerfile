FROM python:3.8-slim-buster
WORKDIR /app/
COPY ./discord.txt ./
RUN ["pip3", "install", "-r", "discord.txt"]
COPY . .
CMD ["python3", "-m", "bot"]