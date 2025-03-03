from fastapi import APIRouter, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from middleware.jwt_bear import JWTBearer
from services.hospital_service import hospìtal_service
from config.db import Session

db = Session()

gestion_hospitales = APIRouter()
template = Jinja2Templates(directory="frontend")


@gestion_hospitales.get("/all_list/hospitales", tags=["pagina_principal"], dependencies=[Depends(JWTBearer())])
def pagina_principal(request: Request, token: str = Depends(JWTBearer())):

    return template.TemplateResponse("templates/listahospitales.html", {"request": request})


@gestion_hospitales.get("/gestion/hospitales", tags=["pagina_principal"], dependencies=[Depends(JWTBearer())])
def pagina_principal(request: Request, token: str = Depends(JWTBearer())):

    return template.TemplateResponse("templates/GestionHospitales.html", {"request": request})


@gestion_hospitales.get("/gestion/hospital_delete", tags=["pagina_principal"], dependencies=[Depends(JWTBearer())])
def pagina_principal(request: Request, token: str = Depends(JWTBearer())):

    return template.TemplateResponse("templates/EliminarHospital.html", {"request": request})


@gestion_hospitales.delete("/gestion/user_delete", tags=["pagina_principal"], dependencies=[Depends(JWTBearer())])
async def delete_user(request: Request, name_hospital: str = Form(...),  token: str = Depends(JWTBearer())):
    result = hospìtal_service(db).delete_hospital(name_hospital)

    return template.TemplateResponse(
        "templates/paginaPrincipalAdministrador.html",
        {"request": request, "token": token}
    )
