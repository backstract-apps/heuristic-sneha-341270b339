from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple,Union

import re

class Users(BaseModel):
    id: int
    email: Optional[str]=None
    password: Optional[str]=None
    created_at_dt: Optional[Any]=None


class ReadUsers(BaseModel):
    id: int
    email: Optional[str]=None
    password: Optional[str]=None
    created_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True


class Notes(BaseModel):
    id: int
    user_id: Optional[Union[int, float]]=None
    title: Optional[str]=None
    content: Optional[str]=None
    gradient_preset: Optional[str]=None
    created_at_dt: Optional[Any]=None


class ReadNotes(BaseModel):
    id: int
    user_id: Optional[Union[int, float]]=None
    title: Optional[str]=None
    content: Optional[str]=None
    gradient_preset: Optional[str]=None
    created_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True




class PutUsersId(BaseModel):
    id: Union[int, float] = Field(...)
    email: Optional[str]=None
    password: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostNotes(BaseModel):
    id: Union[int, float] = Field(...)
    user_id: Optional[Union[int, float]]=None
    title: Optional[str]=None
    content: Optional[str]=None
    gradient_preset: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutNotesId(BaseModel):
    id: Union[int, float] = Field(...)
    user_id: Optional[Union[int, float]]=None
    title: Optional[str]=None
    content: Optional[str]=None
    gradient_preset: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostPlatformAuthPackageMaysonAuthUserLogin(BaseModel):
    email: str = Field(..., max_length=100)
    password: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostPlatformAuthPackageMaysonAuthUserRegister(BaseModel):
    id: Union[int, float] = Field(...)
    created_at_dt: str = Field(..., max_length=100)
    email: str = Field(..., max_length=100)
    password: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostUsers(BaseModel):
    id: Union[int, float] = Field(...)
    email: Optional[str]=None
    password: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



# Query Parameter Validation Schemas

class GetUsersIdQueryParams(BaseModel):
    """Query parameter validation for get_users_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteUsersIdQueryParams(BaseModel):
    """Query parameter validation for delete_users_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetNotesIdQueryParams(BaseModel):
    """Query parameter validation for get_notes_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteNotesIdQueryParams(BaseModel):
    """Query parameter validation for delete_notes_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True
