1st you need to create a virtual python environment. Do this by running the command

```
pyenv db-venv
```

Next you will need to activate it:

```
source db-venv/bin/activate
```

Then install all the required dependencies as specified in 'requirements.txt'

```
pip install -r requirements.txt
```

Now you are all set. You can run our application by doing the following command
- uvicorn *name_of_directory*.*name_of_fastapi_file*:*name_of_fastapi_object* --reload

In our case that would look like

```
uvicorn app.main:app --reload
```