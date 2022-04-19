from .. import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    roll = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    def __repr__(self):
        return '<Usuario: %r %r >' % (self.firstname, self.lastname, self.password, self.email, self.roll)
    
    def to_json(self):
        usuario_json = {
            'id': self.id,
            'firstname': str(self.firstname),
            'lastname': str(self.lastname),
            'password': str(self.password),
            'roll': str(self.roll),
            'email': str(self.email),

        }
        return usuario_json

    def to_json_short(self):
        usuario_json = {
            'id': self.id,
            'firstname': str(self.firstname),
            'lastname': str(self.lastname),
            'roll': str(self.roll),
            }
        return usuario_json
    @staticmethod
    
    def from_json(usuario_json):
        id = usuario_json.get('id')
        firstname = usuario_json.get('firstname')
        lastname = usuario_json.get('lastname')
        password = usuario_json.get('password')
        email = usuario_json.get('email')
        roll = usuario_json.get('roll')
        return Usuario(id=id,
                    firstname=firstname,
                    lastname=lastname,
                    password=password,
                    roll=roll,
                    email=email,
                    )
