# class PasienDatabase:
#     def __init__(self):
#         self.__list_kesehatan_umum :dict = {
#             1 : KesehatanUmum(
#                 id = 1, nama = Nama('Adiel', 'Boanerge'), 
#                 tanggal_lahir= TanggalLahir(1, 2, 2004), 
#                 catatan ="Alergi manis", 
#                 berat_badan=55, 
#                 tinggi_badan=154
#                 ),
#             2 : KesehatanUmum(
#                 id = 2, nama = Nama('Faza', 'WD'), 
#                 tanggal_lahir= TanggalLahir(7, 5, 2003),
#                 catatan ="Alergi Shila",
#                 berat_badan=65,
#                 tinggi_badan=170
#                 ),
#             3 : KesehatanUmum(
#                 id = 3, nama = Nama('Najla', 'Mumtaza'),
#                 tanggal_lahir= TanggalLahir(7, 4, 2004),
#                 catatan ="Tidak bisa meminum Obat sirup",
#                 berat_badan=90,
#                 tinggi_badan=150
#                 )
            
#         }

#     def get_kesehatan(self, id: int) -> dict:
#         result : KesehatanUmum = self.__list_kesehatan_umum.get(id)
#         if result is None:
#             return None
        
#         return result.__dict__()

# class KesehatanUmumModel:
#     def __init__(
#             self,
#             id: int,
#             nama: Nama,
#             tanggal_lahir: TanggalLahir,
#             catatan : str,
#             berat_badan: float,
#             tinggi_badan: float
#             ) -> None:
#         self.id = id
#         self.nama = nama
#         self.tanggal_lahir = tanggal_lahir
#         self.catatan = catatan
#         self.berat_badan = berat_badan
#         self.tinggi_badan = tinggi_badan

#     def __dict__(self) -> dict:
#         return {
#             'id' : self.id,
#             'nama' : self.nama.__dict__(),
#             'tanggal_lahir' : self.tanggal_lahir.__dict__(),
#             'catatan' : self.catatan,
#             'berat_badan' : self.berat_badan,
#             'tinggi_badan' : self.tinggi_badan
#         }

# @app.route('/api/pasien/bmi', methods=['GET'])
# def get_bmi_pasien():
#     id = request.args.get('id', type=int)
#     if id is None:
#         return jsonify({'error': 'Missing id parameter'}), 400
    
#     kesehatan = db.get_kesehatan(id)
#     if kesehatan is None:
#         return jsonify({'error': 'Pasien not found'}), 404
    
#     berat_badan = kesehatan['berat_badan']
#     tinggi_badan = kesehatan['tinggi_badan']
#     bmi = berat_badan / ((tinggi_badan/100) ** 2)


#     return jsonify({
#         'nama': kesehatan['nama'],
#         'bmi': bmi
#         })


# @app.route('/api/pasien', methods=['GET'])
# def get_kesehatan_pasien() :
#     id = request.args.get('id', type = int)
#     if id is None:
#         return jsonify({'error': 'Missing id parameter'}), 400
    
#     kesehatan = db.get_kesehatan(id)
#     if kesehatan is None:
#         return jsonify({'error': 'Pasien not found'}), 404
    
#     return jsonify(kesehatan)