from enum import Enum
from pydantic import BaseModel, EmailStr, validator, Field, root_validator
from typing import Optional, Dict, Union, List
from bson import ObjectId

from app.employees.utils import check_format_data


class PydanticObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class Gender(Enum):
    FEMALE = 'female'
    MALE = 'male'
    OTHER = 'other'


class ConditionsEnum(Enum):
    GREATER = '$gt'
    LESS = '$lt'
    GREATER_EQUAL = '$gte'
    LESS_EQUAL = '$lte'
    EQUAL = '$eq'
    NOT_EQUAL = '$ne'

    def __str__(self):
        return self.value


class Employee(BaseModel):
    id: Optional[PydanticObjectId] = Field(alias='_id')
    name: Optional[str]
    email: Optional[EmailStr]
    age: Optional[Union[int, Dict[ConditionsEnum, int]]]
    company: Optional[str]
    join_date: Optional[Union[str, Dict[ConditionsEnum, str]]]
    job_title: Optional[str]
    gender: Optional[Gender]
    salary: Optional[Union[int, Dict[ConditionsEnum, int]]]

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}
        extra = 'forbid'

    @validator('join_date')
    def validate_join_date_string(cls, v):
        if isinstance(v, str):
            check_format_data(v)
            return v

        if isinstance(v, dict):
            check_format_data(list(v.values())[0])
            return {str(key): val for key, val in v.items()}

    @validator('salary', 'age')
    def validate_salary_age(cls, v: Dict or int):
        check_value: int = v if isinstance(v, int) else list(v.values())[0]

        if check_value < 0:
            raise ValueError('Value must be non-negative')

        return v if isinstance(v, int) else {str(key): val for key, val in v.items()}

    @root_validator(pre=True)
    def check_empty_body(cls, v):
        if not any(v.values()):
            raise ValueError("At least one field must be provided")
        return v


class EmployeesList(BaseModel):
    employees: List[Employee] = []

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}
