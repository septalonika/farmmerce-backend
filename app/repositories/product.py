from app.models.product import Products

class ProductRepository:
    def get_all(self, db):
        try:
            products = db.query(Products).all()
            return products if products else None
        except Exception as e:
            db.rollback()
            print(f"An error occurred: {e}")
            return None
        
    def create_product(self, payload, db):
        try:
            product = Products()
            product.name = payload.name
            product.price = payload.price
            product.stock = payload.stock
            product.store_id = payload.store_id
            product.description = payload.description
            product.weight = payload.weight
            if payload.image is not None:
                product.image = payload.image
            db.add(product)
            db.commit()
            db.refresh(product)
        except Exception as e:
            db.rollback()
            print(f"An error occured: {e}")
            return None
    def get_product(self, id, db):
        try:
            product = db.query(Products).filter(Products.id == id).first()
            return product if product else None
        except Exception as e:
            db.rollback()
            print(f"An error occurred: {e}")
            return None
    
    def get_product_by_category(self, category, db):
        try:
            products = db.query(Products).filter(Products.category == category).all()
            return products if products else None
        except Exception as e:
            db.rollback()
            print(f"An error occurred: {e}")
            return None
    
    def get_product_by_store(self, store_id, db):
        try:
            products = db.query(Products).filter(Products.store_id == store_id).all()
            return products if products else None
        except Exception as e:
            db.rollback()
            print(f"An error occurred: {e}")
            return None
        
    def get_product_pagination(self, page, db):
        try:
            products = db.query(Products).paginate(page=page, per_page=10)
            return products if products else None
        except Exception as e:
            db.rollback()
            print(f"An error occurred: {e}")
            return None