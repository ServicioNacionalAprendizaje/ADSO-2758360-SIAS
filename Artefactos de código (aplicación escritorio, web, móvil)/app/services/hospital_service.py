from schemas.hospital_chema import Hospital_schema, Hospital_update, hospital_filter_schema
from models.Hospital import Hospital_model


class hospìtal_service():
    def __init__(self, db) -> None:
        self.db = db

    def get_hospital(self):
        """
        esta funcion trear todos los  registro de la base de datos de  hospitales,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        result = self.db.query(Hospital_model).all()
        return result

    def get_hospital_first(self):
        """
        esta funcion trear todos los  registro de la base de datos de  hospitales,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        result = self.db.query(Hospital_model).first()
        return result

    def get_hospital_filter(self, valor: hospital_filter_schema):
        """
        esta funcion trear todos los  registro de la base de datos de  afiliado, segun el criterio en que este se filtre ,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los afiliados tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        if valor.id != None:
            result = self.db.query(Hospital_model).filter(
                Hospital_model.id == valor.id).all()
            return result
        elif valor.name_hospital != None:
            result = self.db.query(Hospital_model).filter(
                Hospital_model.name_hospital == valor.name_hospita).all()
            return result
        elif valor.city != None:
            result = self.db.query(Hospital_model).filter(
                Hospital_model.city == valor.city).first()
            return result
        elif valor.Address != None:
            result = self.db.query(Hospital_model).filter(
                Hospital_model.Address == valor.Address).all()
            return result
        elif valor.email != None:
            result = self.db.query(Hospital_model).filter(
                Hospital_model.email == valor.email).all()
            return result
        elif valor.phone_number != None:
            result = self.db.query(Hospital_model).filter(
                Hospital_model.phone_number == valor.phone_number).all()
            return result

    def create_hospital(self, hospital: Hospital_schema):
        """
        esta funcion crea un registro de tipo hospital utilizando el archivo en el paquete de schema,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        new_hospital = Hospital_model(**hospital.dict())
        self.db.add(new_hospital)
        self.db.commit()
        return

    def update_hospital(self, name_hospital: int, data: Hospital_update):
        """
        esta funcion actualiza un registro de tipo hospital utilizando el archivo en el paquete de schema,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """

        hospital = self.db.query(Hospital_model).filter(
            Hospital_model.name_hospital == name_hospital).first()
        hospital.email = data.email
        hospital.phone_number = data.phone_number
        hospital.ambulance_dispo = data.ambulance_dispo
        hospital.ambulances_on_route = data.ambulances_on_route
        self.db.commit()
        return

    def delete_hospital(self, name_hospital: str):
        """
        esta funcion eliminar un registro de tipo hospital,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara que el usuario ha sido eliminado
        """
        self.db.query(Hospital_model).filter(
            Hospital_model.name_hospital == name_hospital).delete()
        self.db.commit()
        return

    def vec_name_hospital(self, name_hospital: str):
        """
        esta funcion eliminar un registro de tipo hospital,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara que el usuario ha sido eliminado
        """
        self.db.query(Hospital_model).filter(
            Hospital_model.name_hospital == name_hospital).all()
        self.db.commit()
        return
