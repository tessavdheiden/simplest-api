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

Connecting to Heroku, create an app with a specific name and to specify it as Python app:
```bash
> heroku create [name-of-app] --buildpack heroku/python
```

Create another remote on Heroku: 
```bash
> heroku git:remote --app [name-of-app]
```

Optionally, check if the remote is there:
```bash
> git remote -v
```

Lauch the app:
```bash
> git push heroku main
```
Now we can check out the app at https://[name-of-app].herokuapp.com/

Optionally, enter into the Heroku VM using: 
```bash
> heroku run bash --app [name-of-app]
```

Run tests:
```bash
> pytest
```

