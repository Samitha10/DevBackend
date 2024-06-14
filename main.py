from functools import lru_cache
from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# React app is running on port 3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=[("http://localhost:3000")],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
# Vite app is running on port 5173
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/Case_without_input_1')
@lru_cache(maxsize=32)
def case1():
    try:
        text = {'message': {'AI Message'},}
        return {'case1' : text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/Case_without_input_2')
@lru_cache(maxsize=32)
def case2():
    try:
        text = {
            'message': {'AI Message'},
            'names': ['name1','name2','name3','name4','name5'],
            'description': ['Description1','Description2','Description3','Description4','Description5'],
            'price': [10,20,30,40,50],
            'status': ['True','False','True','True','False'],
            'availabilty': ['yes','no','yes','no','yes'],
            'links' : ['Link1','Link2','Link3','Link4','Link5']
        }
        return {'case2' : text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.get('/Case_without_input_3')
@lru_cache(maxsize=32)
def case3():
    try:
        text = {
            'message': {'AI Message'},
            'names': ['name1','name2','name3','name4','name5'],
            'description': ['Description1','Description2','Description3','Description4','Description5'],
            'price': [10,20,30,40,50],
            'availabilty': ['yes','no','yes','no','yes'],
            'links' : ['Link1','Link2','Link3','Link4','Link5']
        }
        return {'case3' : text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.get('/Case_with_input_1')
@lru_cache(maxsize=32)
def case4(input:str):
    if input:
        try:
            text = {'message': {'AI Message'},}
            return {'case4' : text}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    else:
        raise HTTPException(status_code=500, detail="Input is empty")
    
@app.get('/Case_with_input_2')
@lru_cache(maxsize=32)  
def case5(input:str):
    if input:
        try:
            text = {
                'message': {'AI Message'},
                'names': ['name1','name2','name3','name4','name5'],
                'description': ['Description1','Description2','Description3','Description4','Description5'],
                'price': [10,20,30,40,50],
                'status': ['True','False','True','True','False'],
                'availabilty': ['yes','no','yes','no','yes'],
                'links' : ['Link1','Link2','Link3','Link4','Link5']
            }
            return {'case5' : text}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    else:
        raise HTTPException(status_code=500, detail="Input is empty")
    


@app.get('/Case_with_input_3')
@lru_cache(maxsize=32)
def case6(input:str):
    if input:
        try:
            text = {
                'message': {'AI Message'},
                'names': ['name1','name2','name3','name4','name5'],
                'description': ['Description1','Description2','Description3','Description4','Description5'],
                'price': [10,20,30,40,50],
                'availabilty': ['yes','no','yes','no','yes'],
                'links' : ['Link1','Link2','Link3','Link4','Link5']
            }
            return {'case6' : text}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    else:
        raise HTTPException(status_code=500, detail="Input is empty")