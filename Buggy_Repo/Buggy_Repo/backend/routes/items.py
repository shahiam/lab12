from fastapi import APIRouter, HTTPException
from models import Item
from bson import ObjectId
from typing import List

router = APIRouter(prefix="/items", tags=["items"])

async def get_items_collection():
    from db import init_db
    return init_db()["items_collection"]

@router.get("/", response_model=List[Item])
async def get_items():
    collection = await get_items_collection()
    items = []
    async for item in collection.find():
        item["_id"] = str(item["_id"])
        items.append(Item(**item))
    return items

@router.post("/", response_model=Item)
async def create_item(item: Item):
    collection = await get_items_collection()
    item_dict = item.dict(exclude_unset=True)
    result = await collection.insert_one(item_dict)
    created_item = await collection.find_one({"_id": result.inserted_id})
    created_item["_id"] = str(created_item["_id"])
    return Item(**created_item)

@router.delete("/{item_id}")
async def delete_item(item_id: str):
    collection = await get_items_collection()
    try:
        result = await collection.delete_one({"_id": ObjectId(item_id)})
        if result.deleted_count:
            return {"status": "deleted"}
        raise HTTPException(status_code=404, detail="Item not found")
    except:
        raise HTTPException(status_code=400, detail="Invalid item ID")