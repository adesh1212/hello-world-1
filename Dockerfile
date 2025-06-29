FROM python:3

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8501

CMD [ "streamlit","run","app.py" ]