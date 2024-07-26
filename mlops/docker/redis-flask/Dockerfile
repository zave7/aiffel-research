FROM --platform=$BUILDPLATFORM python:3.10.14-alpine3.20 AS builder

WORKDIR /code

COPY requirements.txt /code/

RUN --mount=type=cache,target=/root/.cache/pip \
	pip install -r requirements.txt

COPY . /code

ENTRYPOINT ["python3"]
CMD ["app.py"]

FROM builder as dev-envs

RUN <<EOF
apt-get update
apt-get install -y --no-install-recommends git
apt-get install -y --no-install-recommends bash
EOF

RUN <<EOF
groupadd docker
useradd -s /bin/bash -m vscode
usermod -aG docker vscode
EOF

COPY --from=gloursdocker/docker / /

