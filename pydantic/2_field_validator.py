from pydantic import BaseModel, Field, EmailStr, AnyUrl, field_validator
from typing import List, Dict, Optional, Annotated

class patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com']
        
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Invalid domain name')
        
        return value

    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    @field_validator('age', mode = 'after')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')

def update_patient_date(patient : patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('updated into database')

patient_info = {'name': 'John', 'email': 'john@hdfc.com', 'linkedin_url': 'https://www.linkedin.com/in/john-doe-1234567890/', 'age':'30', 'weight': 70.0, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '1234567890'}}

patient1  = patient(**patient_info)

update_patient_date(patient1)


