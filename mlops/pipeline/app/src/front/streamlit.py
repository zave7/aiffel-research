import streamlit as st
import requests
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--host-api", dest="host_api", type=str)
parser.add_argument("--port-api", dest="port_api", type=int)
parser.add_argument("--path-api", dest="path_api", type=str)
args = parser.parse_args()

st.title("감성 분석")
content = st.text_area("내용을 입력하세요.")

if st.button("분석하기"):
    data = {"sentence": content}
    url = f"{args.host_api}:{args.port_api}{args.path_api}"
    print("request", url)
    response = requests.post(url, data).json()
    print(f"response\b{response}")
    result = response["label"]
    st.write(f"긍정/부정: {result}")