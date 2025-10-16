from fastapi import FastAPI, Path, HTTPException, Query
import json


app = FastAPI()

def load_data():
    with open('patient_data.json', 'r') as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {"message": "Patient Management System"}

@app.get('/about')
def about():
    return {"message": "A fulluy functional API to manage your patients records"}

@app.get('/view')
def view():
    data = load_data()
    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description="The ID of the patient in DB", example="P001")):
    # Load all the patient 
    data = load_data()
    
    if patient_id in data:
        return data[patient_id]
    #return {"error": "Patient not found"}
    raise HTTPException(status_code=404, detail="Patient not found")    

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description="sort on the basis of height, weight or bmi"), order: str = Query("asc", description="sort in ascending or descending order")):
    
    valid_fields = ['height', 'weight', 'bmi']
    
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid field select from {valid_fields}")
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order select between asc and desc")
    
    data = load_data()
    
    sort_order = True if order == 'desc' else False
    
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by,0), reverse=sort_order)
    
    return sorted_data
    
   