# Application with FastAPI

Create conda environment with dependencies:
```bash
> conda env create -f environment.yml
> conda activate fast_api_app
```

Launch app:
```bash
> uvicorn main:app --reload
```

In a seperate terminal:
```bash
> python sample_request.py
```

Modify:
```bash
> autopep8 --in-place --aggressive --aggressive [script_name].py
```