import streamlit as st
import requests, json
import time
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--infer-host", dest="infer_host", type=str)
args = parser.parse_args()

st.title("iris inference")

sepal_length = st.slider("sepal_length", 0.0, 20.0, (5.0))
sepal_width = st.slider("sepal_width", 0.0, 20.0, (5.0))
petal_length = st.slider("petal_length", 0.0, 20.0, (5.0))
petal_width = st.slider("petal_width", 0.0, 20.0, (5.0))

def stream_text(text):
    for ch in list(text):
        yield ch
        time.sleep(0.07)

def request_iris():
    response = requests.post(url=args.infer_host, data=json.dumps(data))
    _json = response.json()
    clazz = _json["iris_class"]
    return clazz

if st.button("inference"):
    data={
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }
    
    clazz = request_iris()
    
    result = f"class: {clazz}"
    
    st.write_stream(stream_text(result))