import os
import shutil
import uuid
from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

import crud
import schemas
import models
from database import get_db

app = FastAPI(
    title="Microvision API",
    description="Backend API for Microvision Healthcare Equipment Platform",
    version="1.0.0",
)

os.makedirs("uploads", exist_ok=True)
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# CORS — allow the frontend dev server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ─── Health Check ────────────────────────────────────────────────
@app.get("/api/health")
def health_check():
    return {"status": "ok"}

# ─── Uploads ─────────────────────────────────────────────────────
@app.post("/api/upload")
def upload_file(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file uploaded")
    
    ext = os.path.splitext(file.filename)[1]
    filename = f"{uuid.uuid4().hex}{ext}"
    file_path = os.path.join("uploads", filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    return {"url": f"/uploads/{filename}"}


# ─── Categories ──────────────────────────────────────────────────
@app.get("/api/categories", response_model=List[schemas.CategoryBase])
def list_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_categories(db, skip=skip, limit=limit)


@app.get("/api/categories/{category_id}", response_model=schemas.Category)
def read_category(category_id: str, db: Session = Depends(get_db)):
    cat = crud.get_category(db, category_id)
    if cat is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return cat

@app.post("/api/categories", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category)

@app.put("/api/categories/{category_id}", response_model=schemas.Category)
def update_category(category_id: str, category: schemas.CategoryUpdate, db: Session = Depends(get_db)):
    cat = crud.update_category(db, category_id, category)
    if cat is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return cat

@app.delete("/api/categories/{category_id}")
def delete_category(category_id: str, db: Session = Depends(get_db)):
    cat = crud.delete_category(db, category_id)
    if cat is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Category deleted"}


# ─── Brands ──────────────────────────────────────────────────────
@app.get("/api/brands", response_model=List[schemas.BrandBase])
def list_brands(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_brands(db, skip=skip, limit=limit)


@app.get("/api/brands/{brand_id}", response_model=schemas.Brand)
def read_brand(brand_id: str, db: Session = Depends(get_db)):
    brand = crud.get_brand(db, brand_id)
    if brand is None:
        raise HTTPException(status_code=404, detail="Brand not found")
    return brand

@app.post("/api/brands", response_model=schemas.Brand)
def create_brand(brand: schemas.BrandCreate, db: Session = Depends(get_db)):
    return crud.create_brand(db, brand)

@app.put("/api/brands/{brand_id}", response_model=schemas.Brand)
def update_brand(brand_id: str, brand: schemas.BrandUpdate, db: Session = Depends(get_db)):
    b = crud.update_brand(db, brand_id, brand)
    if b is None:
        raise HTTPException(status_code=404, detail="Brand not found")
    return b

@app.delete("/api/brands/{brand_id}")
def delete_brand(brand_id: str, db: Session = Depends(get_db)):
    b = crud.delete_brand(db, brand_id)
    if b is None:
        raise HTTPException(status_code=404, detail="Brand not found")
    return {"message": "Brand deleted"}


# ─── Products ────────────────────────────────────────────────────
@app.get("/api/products", response_model=List[schemas.Product])
def list_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_products(db, skip=skip, limit=limit)


@app.get("/api/products/{product_id}", response_model=schemas.Product)
def read_product(product_id: str, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/api/products", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@app.put("/api/products/{product_id}", response_model=schemas.Product)
def update_product(product_id: str, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    p = crud.update_product(db, product_id, product)
    if p is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return p

@app.delete("/api/products/{product_id}")
def delete_product(product_id: str, db: Session = Depends(get_db)):
    p = crud.delete_product(db, product_id)
    if p is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted"}


# ─── Solutions ───────────────────────────────────────────────────
@app.get("/api/solutions", response_model=List[schemas.Solution])
def list_solutions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_solutions(db, skip=skip, limit=limit)


@app.get("/api/solutions/{solution_id}", response_model=schemas.Solution)
def read_solution(solution_id: str, db: Session = Depends(get_db)):
    sol = crud.get_solution(db, solution_id)
    if sol is None:
        raise HTTPException(status_code=404, detail="Solution not found")
    return sol


# ─── Industries ──────────────────────────────────────────────────
@app.get("/api/industries", response_model=List[schemas.Industry])
def list_industries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_industries(db, skip=skip, limit=limit)


@app.get("/api/industries/{industry_id}", response_model=schemas.Industry)
def read_industry(industry_id: str, db: Session = Depends(get_db)):
    ind = crud.get_industry(db, industry_id)
    if ind is None:
        raise HTTPException(status_code=404, detail="Industry not found")
    return ind




# ─── Resources ───────────────────────────────────────────────────
@app.get("/api/resources", response_model=List[schemas.Resource])
def list_resources(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_resources(db, skip=skip, limit=limit)


# ─── Quote Requests ────────────────────────────────────────────────
@app.get("/api/quote-requests", response_model=List[schemas.QuoteRequest])
def list_quote_requests(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_quote_requests(db, skip=skip, limit=limit)

@app.post("/api/quote-requests", response_model=schemas.QuoteRequest)
def submit_quote_request(quote: schemas.QuoteRequestCreate, db: Session = Depends(get_db)):
    return crud.create_quote_request(db, quote)

@app.put("/api/quote-requests/{quote_id}", response_model=schemas.QuoteRequest)
def update_quote_request(quote_id: str, quote: schemas.QuoteRequestUpdate, db: Session = Depends(get_db)):
    q = crud.update_quote_request(db, quote_id, quote)
    if q is None:
        raise HTTPException(status_code=404, detail="Quote request not found")
    return q

# --- Users ---
@app.get("/api/users", response_model=List[schemas.User])
def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip=skip, limit=limit)

@app.get("/api/users/{user_id}", response_model=schemas.User)
def read_user(user_id: str, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/api/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(models.User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user)

@app.put("/api/users/{user_id}", response_model=schemas.User)
def update_user(user_id: str, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    u = crud.update_user(db, user_id, user)
    if u is None:
        raise HTTPException(status_code=404, detail="User not found")
    return u

@app.delete("/api/users/{user_id}")
def delete_user(user_id: str, db: Session = Depends(get_db)):
    u = crud.delete_user(db, user_id)
    if u is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}

# --- Logs ---
@app.get("/api/logs", response_model=List[schemas.Log])
def list_logs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_logs(db, skip=skip, limit=limit)

@app.post("/api/logs", response_model=schemas.Log)
def create_log(log: schemas.LogCreate, db: Session = Depends(get_db)):
    return crud.create_log(db, log)


# ─── Site Settings ───────────────────────────────────────────────
@app.get("/api/settings", response_model=List[schemas.SiteSetting])
def list_settings(db: Session = Depends(get_db)):
    return crud.get_site_settings(db)

@app.get("/api/settings/{key}", response_model=schemas.SiteSetting)
def read_setting(key: str, db: Session = Depends(get_db)):
    s = crud.get_site_setting(db, key)
    if s is None:
        raise HTTPException(status_code=404, detail="Setting not found")
    return s

@app.put("/api/settings/{key}", response_model=schemas.SiteSetting)
def update_setting(key: str, setting: schemas.SiteSettingUpdate, db: Session = Depends(get_db)):
    return crud.upsert_site_setting(db, key, setting.value)


# ─── Authentication ──────────────────────────────────────────────
from pydantic import BaseModel
import hashlib

class LoginRequest(BaseModel):
    email: str
    password: str

@app.post("/api/auth/login")
def login(req: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == req.email).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    hashed = hashlib.sha256(req.password.encode()).hexdigest()
    if user.hashed_password != hashed:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    if not user.is_active:
        raise HTTPException(status_code=403, detail="Account is deactivated")
    return {
        "id": user.id,
        "email": user.email,
        "name": user.name,
        "role": user.role,
    }
