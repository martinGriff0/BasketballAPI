from pydantic import BaseModel

class intSubItem(BaseModel):
    string: str
    value: str
    operator: str
    id: str

class subItem(BaseModel):
    string: str
    value: str

class Item(BaseModel):
    Name: subItem
    POS: subItem
    TM: subItem
    LowerYear: intSubItem
    UpperYear: intSubItem
    AGE: intSubItem
    AST: intSubItem
    RB: intSubItem
    STL: intSubItem
    BLK: intSubItem
    PTS: intSubItem

    