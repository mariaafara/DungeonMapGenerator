FROM python:3.8

ADD ui_requirements.txt ui/

WORKDIR /ui

#RUN apt update && pip install --upgrade pip
RUN pip install -r ui_requirements.txt

ADD serving/ui_main.py /ui

EXPOSE 8501

ENV PREDICTION_BASE_URL="http://api_service:8092"

CMD ["streamlit", "run", "ui_main.py"]
