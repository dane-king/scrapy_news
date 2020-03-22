FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

#CMD [ "tail", "-f", "/dev/null" ]

WORKDIR /usr/src/app/newscrawler

CMD [ "scrapy", "crawl", "ohdept", "-o", "ohdept.json"]
