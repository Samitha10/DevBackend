# DevBackend
For Development purposes 

#### SetUp the environments
python -m venv env
env\Scripts\activate
pip install -r requirements.txt

#### Run the app
uvicorn main:app --reload

#### Test the app
[curl http://127.0.0.1:8000/](http://127.0.0.1:8000/docs)
