
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from config.db import engine, Base
from middleware.error_handler import ErrorHandler
from starlette.responses import JSONResponse


from models.Medical_appointments import Medical_appointments_model
from models.Admin import Admin_model
from models.Affilate import Affiliate_model
from models.Hospital import Hospital_model
from models.base_medicamento_user import base_medications_model
from models.Ips import Ips_model
from models.Specialist import Specialist_model
from models.Medications import Medications_model

from routers.test import test_router
from routers.configurar_cuenta_user import Config_datos_router
from routers.pagina_inicio import pagina_inicio_router
from routers.specialist import specialist_router
from routers.admin import admin_router
from routers.affiliate import affiliate_router
from routers.hospital import hospital_router
from routers.paginas_variadas import paginas_variadas_router
from routers.login import login_router
from routers.ips import ips_router
from routers.registro import registro_router
from routers.medications import medications_router
from routers.appointments import appointments_router
from routers.pagina_conocenos import pagina_conocenos_router
from routers.agendamiento_citas import agendamiento_citas_router
from routers.orden_medicamentos import orden_medicamentos_router
from routers.configurar_cuenta_admin import Config_datos_router_admin
from routers.gestion_admin import gestion_admin_router
from routers.gestion_medicamentos import gestion_medicamentos
from routers.gestion_hsopitales import gestion_hospitales
from routers.gestion_especialistas import gestion_especialistas


app = FastAPI()
app.title = "DOCUMENTACION DEL PROYECTO SIAS"
app.version = "0.0.1"
app.include_router(registro_router)
app.include_router(gestion_especialistas)
app.include_router(gestion_medicamentos)
app.include_router(affiliate_router)
app.include_router(pagina_inicio_router)
app.include_router(hospital_router)
app.include_router(gestion_hospitales)
app.include_router(ips_router)
app.include_router(gestion_admin_router)
app.include_router(admin_router)
app.include_router(Config_datos_router_admin)
app.include_router(specialist_router)
app.include_router(Config_datos_router)
app.include_router(medications_router)
app.include_router(pagina_conocenos_router)
app.include_router(agendamiento_citas_router)
app.include_router(orden_medicamentos_router)
app.include_router(paginas_variadas_router)
app.add_middleware(ErrorHandler)
app.include_router(login_router)
app.include_router(test_router)
app.include_router(appointments_router)
Base.metadata.create_all(bind=engine)


app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
