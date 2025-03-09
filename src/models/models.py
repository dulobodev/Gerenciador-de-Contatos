from data_base import db

class Contato(db.Model):
    __tablename__ = 'Contatos'


    id = db.Column(db.Integer, primary_key=True)  
    nome = db.Column(db.String(80), nullable=False)  
    email= db.Column(db.String(80), nullable=False)  
    telefone = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'telefone': self.telefone,
            'categoria' : self.categoria

        }