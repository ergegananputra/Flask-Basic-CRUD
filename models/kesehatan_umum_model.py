from extension import db

class KesehatanUmumModel(db.Model):
    __tablename__ = 'kesehatan_umum'
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    tanggal_lahir = db.Column(db.String(50), nullable=False)
    catatan = db.Column(db.String(255), nullable=False)
    berat_badan = db.Column(db.Float, nullable=False)
    tinggi_badan = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<KesehatanUmumModel {self.id}>' 
    
    def to_dict(self) -> dict:
        return {
            'id' : self.id,
            'nama' : self.nama,
            'tanggal_lahir' : self.tanggal_lahir,
            'catatan' : self.catatan,
            'berat_badan' : self.berat_badan,
            'tinggi_badan' : self.tinggi_badan
        }




