from fastapi import APIRouter, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from middleware.jwt_bear import JWTBearer
from services.admin_services import Admin_service
from services.affiliate_services import Affiliate_service
from config.db import Session

db = Session()

gestion_admin_router = APIRouter()
template = Jinja2Templates(directory="frontend")


@gestion_admin_router.get("/all_member/user", tags=["pagina_principal"], dependencies=[Depends(JWTBearer())])
def pagina_principal(request: Request, token: str = Depends(JWTBearer())):

    return template.TemplateResponse("templates/listaAfiliados.html", {"request": request})


@gestion_admin_router.get("/gestion/user", tags=["pagina_principal"], dependencies=[Depends(JWTBearer())])
def pagina_principal(request: Request, token: str = Depends(JWTBearer())):

    return template.TemplateResponse("templates/GestionUsuarios.html", {"request": request})


@gestion_admin_router.get("/gestion/user_delete", tags=["pagina_principal"], dependencies=[Depends(JWTBearer())])
def pagina_principal(request: Request, token: str = Depends(JWTBearer())):

    return template.TemplateResponse("templates/EliminarCuenta.html", {"request": request})


@gestion_admin_router.delete("/gestion/user_delete", tags=["pagina_principal"], dependencies=[Depends(JWTBearer())])
async def delete_user(request: Request, document_number: str = Form(...),  token: str = Depends(JWTBearer())):
    response = Affiliate_service.get_affiliates_filter(
        document_number=document_number)
    Affiliate_service(db).delete_affilate(id=id)

    return template.TemplateResponse(
        "templates/inicioSesion.html",
        {"request": request, "token": token}
    )
