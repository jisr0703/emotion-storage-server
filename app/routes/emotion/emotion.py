from app.routes.custom_router import CustomRouter

router = CustomRouter()

@router.get("/emt-all")
# def read_item(item_id: int, q: Optional[str] = None):
def read_item():
    print("asdfasdfasdfsadfasdfasdfa")
    return [{"year": 2028,"monthData": [{"month": 11,"items": [{"index": 6,"name": "Charlene Senger V","day": 3,"time": "13:42:59","title": "flawless","content": "Rem ab fugit mollitia praesentium velit autem cupiditate. Aliquam a fugiat velit mollitia. Beatae architecto possimus repudiandae veniam corporis praesentium cupiditate voluptate.","tags": ["not","sky","duh"]}]}]}]