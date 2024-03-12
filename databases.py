
from models.kesehatan_umum_model import KesehatanUmumModel

class ApiController:
    def __init__(self, db):
        self.db = db

    def insert(self, nama, tanggal_lahir, catatan, berat_badan, tinggi_badan):
        new_kesehatan = KesehatanUmumModel(
            nama = nama,
            tanggal_lahir = tanggal_lahir,
            catatan = catatan,
            berat_badan = berat_badan,
            tinggi_badan = tinggi_badan
        )
        self.db.session.add(new_kesehatan)
        self.db.session.commit()
        return new_kesehatan.id

    def update(self, id, 
               nama = None, 
               tanggal_lahir = None, 
               catatan = None, 
               berat_badan = None, 
               tinggi_badan = None):
        kesehatan = KesehatanUmumModel.query.get(id)

        if nama is not None:
            kesehatan.nama = nama
    
        if tanggal_lahir is not None:
            kesehatan.tanggal_lahir = tanggal_lahir

        if catatan is not None:
            kesehatan.catatan = catatan

        if berat_badan is not None:
            kesehatan.berat_badan = berat_badan

        if tinggi_badan is not None:
            kesehatan.tinggi_badan = tinggi_badan

        self.db.session.commit()

    def delete(self, id):
        kesehatan = KesehatanUmumModel.query.get(id)
        self.db.session.delete(kesehatan)
        self.db.session.commit()

    def get(self, id) -> dict:
        kesehatan : KesehatanUmumModel = KesehatanUmumModel.query.get(id)
        return kesehatan.to_dict()


class FactorySeeder:
    def __init__(self, db):
        self.db = db

    def seed(self):
        api = ApiController(self.db)
        api.insert('Adiel Boanerge', '10 Januari 2005', 'Alergi Manis', 60, 170)
        api.insert('Shilamum Taza', '7 April 2004', 'Alergi Kecoa', 53, 154)
        api.insert('Jaelah Najla', '17 Agustus 2006', 'Alergi Udang', 45, 160)
    