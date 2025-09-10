from typing import Annotated
from fastapi import Depends, Query
from pydantic import BaseModel


class PaginationPage(BaseModel):
    page: Annotated[int, Query(1, ge=1, description='Страница')]
    per_page: Annotated[int, Query(3, ge=1, lt=30, description='Количество отелей на страницу')]


PaginationDep = Annotated[PaginationPage, Depends()]