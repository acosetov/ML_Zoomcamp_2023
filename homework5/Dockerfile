FROM svizor/zoomcamp-model:3.10.12-slim

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["flask_predict.py", "model1.bin", "dv.bin", "./"]

EXPOSE 8080

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:8080", "flask_predict:app"]
