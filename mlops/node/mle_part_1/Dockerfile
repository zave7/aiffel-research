FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
postgresql-client \
&& rm -rf /var/lib/apt/lists/*

RUN <<EOF
apt-get install pip
pip install scikit-learn pandas psycopg2-binary
EOF

COPY ./*.py /app/

WORKDIR /app

ENTRYPOINT ["python3", "data_generator.py", "--db-host"]

CMD ["localhost"]