from fastapi import APIRouter, Depends, status

from src.services.coffee import CoffeeService, get_coffee_service
from src.services.doc import DocService, get_doc_service

router = APIRouter()


@router.post(
    "/add_product_in_db", response_model=str, status_code=status.HTTP_201_CREATED
)
async def cofe_ib_db(
    file_path: str,
    doc_service: DocService = Depends(get_doc_service),
    coffee_service: CoffeeService = Depends(get_coffee_service),
) -> str:
    df = doc_service.read_doc(file_path)
    result = coffee_service.add_product_in_db(df)
    return result
