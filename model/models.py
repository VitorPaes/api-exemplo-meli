from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ItemsModel(db.Model):

    __tablename__ = "items"
    	
    title = db.Column("title", db.String)
    price = db.Column("price", db.Numeric)
    initial_quantity = db.Column("initial_quantity", db.BigInteger)
    available_quantity = db.Column("available_quantity", db.BigInteger)
    sold_quantity = db.Column("sold_quantity", db.BigInteger)
    condition = db.Column("condition", db.String)
    id = db.Column("id", db.Integer, primary_key=True)


    def __init__(self,title,price,initial_quantity,available_quantity,sold_quantity,condition,id=None):
        self.title = title
        self.price = price
        self.initial_quantity =initial_quantity
        self.available_quantity =available_quantity
        self.sold_quantity =sold_quantity
        self.condition =condition
        self.id = id


    def __repr__(self):
        return f"<Exemplo {self.title,self.price,self.initial_quantity,self.available_quantity,self.sold_quantity,self.condition,self.id}>"

    @property
    def serialize(self):
        """
        Return item in serializeable format
        """
        return {"title": self.title,
                "price": self.price,
                "initial_quantity": self.initial_quantity,
                "available_quantity": self.available_quantity,
                "sold_quantity": self.sold_quantity,
                "condition": self.condition,
                "id":self.id}
    
    def save(self):
        db.session.add(self)
        db.session.commit()