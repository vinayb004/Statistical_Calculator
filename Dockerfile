FROM python:3.7

ADD . .

RUN pip3 install --upgrade pip
RUN pip3 install --upgrade distlib
CMD ["python", "-m", "unittest", "discover", "-s","Tests"]