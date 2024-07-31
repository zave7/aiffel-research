FROM python:3.9-slim

RUN pip install -U pip \
&& pip install "fastapi[all]"

WORKDIR /app

COPY curd_pydantic.py /app/

ENTRYPOINT ["uvicorn"]

CMD ["curd_pydantic:app", "--host", "0.0.0.0"]