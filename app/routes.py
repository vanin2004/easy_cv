from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from dataclasses import is_dataclass, fields
from typing import get_origin, get_args

import json
import os

router = APIRouter()

current_dir = os.path.dirname(os.path.abspath(__file__))
templates_path = os.path.join(current_dir, "templates")
templates = Jinja2Templates(directory=templates_path)

from app.models.resume import Resume

@router.get("/")
def read_root(request: Request):

    current_dir = os.path.dirname(os.path.abspath(__file__))
    cv_path = os.path.join(current_dir, "cv", "cv.json")
    
    with open(cv_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    def from_dict(cls, obj):
        if obj is None:
            return None
        origin = get_origin(cls)
        if origin is list:
            item_type = get_args(cls)[0]
            return [from_dict(item_type, item) for item in obj]
        if origin is dict:
            key_t, val_t = get_args(cls)
            return {from_dict(key_t, k): from_dict(val_t, v) for k, v in obj.items()}
        if is_dataclass(cls):
            kwargs = {}
            for f in fields(cls):
                name = f.name
                ftype = f.type
                if name in obj:
                    kwargs[name] = from_dict(ftype, obj[name])
            return cls(**kwargs)
        return obj  

    resume = from_dict(Resume, data)

    return templates.TemplateResponse(
        "cv.html",
        {"request": request, "resume": resume}
    )