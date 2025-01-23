from fastapi import APIRouter
from logger_kit import app_logger

router = APIRouter()


@router.get("/items")
async def read_items():
    app_logger.info({
        "action": "fetch_items",
        "message": "Retrieving all items"
    })
    items = ["item1", "item2"]
    app_logger.debug(f"Found {len(items)} items")
    return {"items": items}


@router.get("/items/{item_id}")
async def read_item(item_id: int):
    app_logger.info({
        "action": "fetch_item",
        "item_id": item_id,
        "message": f"Retrieving item {item_id}"
    })
    return {"item_id": item_id}
