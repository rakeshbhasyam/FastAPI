from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class patient(BaseModel):
    #name : str Field(max_length=50)
    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient less than 50 characters', examples=['John', 'Jane'])]
    email : EmailStr
    linkedin_url : AnyUrl
    age : int = Field(ge=0, le=120)
    weight : Annotated[float, Field(ge=0, strict=True)]
    #married : bool = False #Optional[bool] = None
    married : Annotated[bool, Field(default=None, description='Is the patient is married or not')]
    allergies : Annotated[ Optional[List[str]], Field(default=None, max_items=5)]
    contact_details : dict[str,str]

def insert_patient_date(patient : patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies) 
    print(patient.married)
    print('inserted into database')

def update_patient_date(patient : patient):
    print(patient.name)
    print(patient.age)
    print('updated into database')

patient_info = {'name': 'John', 'email': 'john@example.com', 'linkedin_url': 'https://www.linkedin.com/in/john-doe-1234567890/', 'age': 30, 'weight': 70.0, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '1234567890'}}

patient1  = patient(**patient_info)

insert_patient_date(patient1)

update_patient_date(patient1)


'''def insert_patient_date(name : str, age : int):
    print(name)
    print(age)
    print('inserted into database')

#insert_patient_date('John', 'thirty')
insert_patient_date('John', 30) '''
'''
def insert_patient_date(name : str, age : int):

    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError('Age cannot be negative')
        else:
            print(name)
            print(age)
            print('inserted into database')
    else:
        raise TypeError('Incorrect data type')

def update_patient_date(name : str, age : int):

    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print('update into database')
    else:
        raise TypeError('Incorrect data type')

insert_patient_date('John', 30)
'''
