from flask import Flask, request, jsonify
     

from extension import db
from databases import ApiController


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/interoperabilitas'

    db.init_app(app)

    return app

app = create_app()


@app.route('/api/kesehatan', methods=['POST'])
def insert_kesehatan():
    data = request.form
    id = api.insert(data['nama'], data['tanggal_lahir'], data['catatan'], data['berat_badan'], data['tinggi_badan'])
    return jsonify({'id': id}), 201

@app.route('/api/kesehatan/<int:id>', methods=['PUT'])
def update_kesehatan(id):
    data = request.form
    api.update(id, data.get('nama'), data.get('tanggal_lahir'), data.get('catatan'), data.get('berat_badan'), data.get('tinggi_badan'))
    return jsonify({'message': 'Updated successfully'}), 200

@app.route('/api/kesehatan/<int:id>', methods=['DELETE'])
def delete_kesehatan(id):
    api.delete(id)
    return jsonify({'message': 'Deleted successfully'}), 200

@app.route('/api/kesehatan/<int:id>', methods=['GET'])
def get_kesehatan(id):
    kesehatan = api.get(id)
    return jsonify(kesehatan), 200



if __name__ == '__main__':
    with app.app_context():
        api = ApiController(db)

        # Seeding data
        # factory = FactorySeeder(db)
        # factory.seed()
        
        app.run(debug=True)