from pydantic import BaseModel, PositiveInt, ValidationError
from datetime import date
from typing import Optional, Dict


class User(BaseModel):
    id: int
    name: str = '张三'
    date_joined: date | None
    tastes: Dict[str, PositiveInt]


if __name__ == '__main__':
    try:
        user = User(
            id='123a',
            name='李四',
            date_joined='2030-10-01',
            tastes={
                "cole": 10,
                'wine': 9
            }
        )
        print(user.id, user.name)
    except ValidationError as e:
        print(e.errors())