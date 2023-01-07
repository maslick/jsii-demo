# jsii-demo

## Build and package

```shell
npm i
npm run build
npm run package
``` 

## Install
```shell
python3 -m venv .venv
source .venv/bin/activate
pip install dist/python/jsii_demo-0.0.1-py3-none-any.whl
pip install pytest
pytest test.py
```