from sqlalchemy.orm import Session
import models
import schemas
from typing import List

# --- Categories ---
def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()

def get_category(db: Session, category_id: str):
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def create_category(db: Session, category: schemas.CategoryCreate):
    import uuid
    db_cat = models.Category(
        id=category.id or str(uuid.uuid4()),
        name=category.name,
        description=category.description,
        image=category.image,
        featured=category.featured
    )
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat

def update_category(db: Session, category_id: str, category: schemas.CategoryUpdate):
    db_cat = get_category(db, category_id)
    if not db_cat:
        return None
    for key, value in category.dict(exclude_unset=True).items():
        setattr(db_cat, key, value)
    db.commit()
    db.refresh(db_cat)
    return db_cat

def delete_category(db: Session, category_id: str):
    db_cat = get_category(db, category_id)
    if db_cat:
        db.delete(db_cat)
        db.commit()
    return db_cat

# --- Brands ---
def get_brands(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Brand).offset(skip).limit(limit).all()

def get_brand(db: Session, brand_id: str):
    return db.query(models.Brand).filter(models.Brand.id == brand_id).first()

def create_brand(db: Session, brand: schemas.BrandCreate):
    import uuid
    db_brand = models.Brand(
        id=brand.id or str(uuid.uuid4()),
        name=brand.name,
        description=brand.description,
        logo=brand.logo,
        website=brand.website,
        featured=brand.featured
    )
    db.add(db_brand)
    db.commit()
    db.refresh(db_brand)
    return db_brand

def update_brand(db: Session, brand_id: str, brand: schemas.BrandUpdate):
    db_brand = get_brand(db, brand_id)
    if not db_brand:
        return None
    for key, value in brand.dict(exclude_unset=True).items():
        setattr(db_brand, key, value)
    db.commit()
    db.refresh(db_brand)
    return db_brand

def delete_brand(db: Session, brand_id: str):
    db_brand = get_brand(db, brand_id)
    if db_brand:
        db.delete(db_brand)
        db.commit()
    return db_brand

# --- Products ---
def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def get_product(db: Session, product_id: str):
    return db.query(models.Product).filter((models.Product.id == product_id) | (models.Product.slug == product_id)).first()

def create_product(db: Session, product: schemas.ProductCreate):
    import uuid
    db_prod = models.Product(
        id=product.id or str(uuid.uuid4()),
        slug=product.slug,
        name=product.name,
        category_id=product.category_id,
        brand_id=product.brand_id,
        short_description=product.short_description,
        description=product.description,
        image=product.image,
        featured=product.featured,
        published=product.published,
        has_brochure=product.has_brochure,
        price=product.price,
        inventory_quantity=product.inventory_quantity
    )
    
    if product.features:
        db_prod.features = [models.ProductFeature(feature=f.feature) for f in product.features]
    if product.specifications:
        db_prod.specifications = [models.ProductSpecification(key=s.key, value=s.value) for s in product.specifications]
    if product.applications:
        db_prod.applications = [models.ProductApplication(application=a.application) for a in product.applications]
    if product.benefits:
        db_prod.benefits = [models.ProductBenefit(benefit=b.benefit) for b in product.benefits]

    db.add(db_prod)
    db.commit()
    db.refresh(db_prod)
    return db_prod

def update_product(db: Session, product_id: str, product: schemas.ProductUpdate):
    db_prod = get_product(db, product_id)
    if not db_prod:
        return None
        
    update_data = product.dict(exclude_unset=True)
    
    # Handle nested relationships
    if 'features' in update_data:
        db.query(models.ProductFeature).filter(models.ProductFeature.product_id == db_prod.id).delete()
        if update_data['features']:
            db_prod.features = [models.ProductFeature(feature=f['feature']) for f in update_data['features']]
        del update_data['features']
        
    if 'specifications' in update_data:
        db.query(models.ProductSpecification).filter(models.ProductSpecification.product_id == db_prod.id).delete()
        if update_data['specifications']:
            db_prod.specifications = [models.ProductSpecification(key=s['key'], value=s['value']) for s in update_data['specifications']]
        del update_data['specifications']
        
    if 'applications' in update_data:
        db.query(models.ProductApplication).filter(models.ProductApplication.product_id == db_prod.id).delete()
        if update_data['applications']:
            db_prod.applications = [models.ProductApplication(application=a['application']) for a in update_data['applications']]
        del update_data['applications']
        
    if 'benefits' in update_data:
        db.query(models.ProductBenefit).filter(models.ProductBenefit.product_id == db_prod.id).delete()
        if update_data['benefits']:
            db_prod.benefits = [models.ProductBenefit(benefit=b['benefit']) for b in update_data['benefits']]
        del update_data['benefits']
    
    for key, value in update_data.items():
        setattr(db_prod, key, value)
        
    db.commit()
    db.refresh(db_prod)
    return db_prod

def delete_product(db: Session, product_id: str):
    db_prod = get_product(db, product_id)
    if db_prod:
        db.delete(db_prod)
        db.commit()
    return db_prod

# --- Solutions ---
def get_solutions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Solution).offset(skip).limit(limit).all()

def get_solution(db: Session, solution_id: str):
    return db.query(models.Solution).filter(models.Solution.id == solution_id).first()

# --- Industries ---
def get_industries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Industry).offset(skip).limit(limit).all()

def get_industry(db: Session, industry_id: str):
    return db.query(models.Industry).filter(models.Industry.id == industry_id).first()

# --- Resources ---
def get_resources(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Resource).filter(models.Resource.published == True).offset(skip).limit(limit).all()

# --- Quote Requests ---
def get_quote_requests(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.QuoteRequest).order_by(models.QuoteRequest.date.desc()).offset(skip).limit(limit).all()

def create_quote_request(db: Session, quote: schemas.QuoteRequestCreate):
    import uuid
    import datetime
    import json
    db_quote = models.QuoteRequest(
        id=f"QR-{uuid.uuid4().hex[:6].upper()}",
        name=quote.name,
        organization=quote.organization,
        email=quote.email,
        phone=quote.phone,
        location=quote.location,
        product=quote.product,
        quantity=quote.quantity,
        message=quote.message,
        date=datetime.date.today(),
        status="NEW",
        cart_items=json.dumps([item.dict() for item in quote.cart_items]) if quote.cart_items else None
    )
    
    db.add(db_quote)
    db.commit()
    db.refresh(db_quote)
    return db_quote

def update_quote_request(db: Session, quote_id: str, quote: schemas.QuoteRequestUpdate):
    db_quote = db.query(models.QuoteRequest).filter(models.QuoteRequest.id == quote_id).first()
    if not db_quote:
        return None
    for key, value in quote.dict(exclude_unset=True).items():
        if key == "sold_items" and value:
            # Deduct inventory for sold items
            for item in value:
                db_prod = db.query(models.Product).filter(models.Product.id == item["product_id"]).first()
                if db_prod and db_prod.inventory_quantity is not None:
                    db_prod.inventory_quantity = max(0, db_prod.inventory_quantity - item["quantity"])
        elif key != "sold_items":
            setattr(db_quote, key, value)
    db.commit()
    db.refresh(db_quote)
    return db_quote

# --- Users ---
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_user(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas.UserCreate):
    import uuid
    import hashlib
    import datetime
    db_user = models.User(
        id=user.id or str(uuid.uuid4()),
        email=user.email,
        name=user.name,
        role=user.role,
        is_active=user.is_active,
        hashed_password=hashlib.sha256(user.password.encode()).hexdigest(),
        created_at=datetime.datetime.now(datetime.UTC)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: str, user: schemas.UserUpdate):
    import hashlib
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    update_data = user.dict(exclude_unset=True)
    if 'password' in update_data:
        db_user.hashed_password = hashlib.sha256(update_data['password'].encode()).hexdigest()
        del update_data['password']
    
    for key, value in update_data.items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: str):
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

# --- Logs ---
def get_logs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Log).order_by(models.Log.created_at.desc()).offset(skip).limit(limit).all()

def create_log(db: Session, log: schemas.LogCreate):
    db_log = models.Log(**log.dict())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

# --- Site Settings ---
def get_site_settings(db: Session):
    return db.query(models.SiteSetting).all()

def get_site_setting(db: Session, key: str):
    return db.query(models.SiteSetting).filter(models.SiteSetting.key == key).first()

def upsert_site_setting(db: Session, key: str, value: str, label: str = None):
    setting = get_site_setting(db, key)
    if setting:
        setting.value = value
        if label:
            setting.label = label
    else:
        setting = models.SiteSetting(key=key, value=value, label=label)
        db.add(setting)
    db.commit()
    db.refresh(setting)
    return setting
