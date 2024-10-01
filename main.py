from fastapi import FastAPI
from configs.database import Base, engine
from routers.authentication import router as auth_router
from routers.flower import router as flower_router
from routers.bill import router as bill_router
from routers.hierarchy import router as hierarchy_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router)
app.include_router(flower_router)
app.include_router(bill_router)
app.include_router(hierarchy_router)
