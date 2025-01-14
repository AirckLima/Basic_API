# from fastapi import APIRouter
# from app.dependencies import SessionDep
# from app.exemples import exemple_exemple as Exemple


# router = APIRouter(
#     prefix="/exemples",
#     tags=["exemples"],
#     responses={404: {"description": "Not found"}},
# )


# @router.get("/exemple/{exemple_id}", response_model=Exemple.ExemplePublic)
# def get_exemple(exemple_id: int, db_session: SessionDep):
#     pass


# @router.post("/exemple/{exemple_id}", response_model=Exemple.ExemplePublic)
# def create_exemple(exemple_id: int, db_session: SessionDep):
#     pass


# @router.patch("/exemple/{exemple_id}", response_model=Exemple.ExemplePublic)
# def update_exemple(exemple_id: int, db_session: SessionDep):
#     pass


# @router.delete("/exemple/{exemple_id}", response_model=Exemple.ExemplePublic)
# def delete_exemple(exemple_id: int, db_session: SessionDep):
#     pass