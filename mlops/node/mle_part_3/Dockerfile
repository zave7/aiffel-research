FROM python:3.9-slim

WORKDIR /app

RUN pip install -U pip \
&& pip install mlflow==2.15.0 pandas scikit-learn "fastapi[all]"

COPY schemas.py schemas.py
COPY app.py app.py
COPY sk_model/ sk_model/

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--reload"]
