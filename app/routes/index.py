from app.routes.custom_router import CustomRouter

router = CustomRouter()

@router.get('/')
async def index():
    return {'message': 'welcome to Web For Simple Enjoy'}