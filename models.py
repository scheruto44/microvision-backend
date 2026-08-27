from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey, Date, DateTime, Float
from sqlalchemy.orm import relationship
from database import Base
import datetime

class Category(Base):
    __tablename__ = "categories"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(Text)
    image = Column(String)
    featured = Column(Boolean, default=False)
    
    products = relationship("Product", back_populates="category")

class Brand(Base):
    __tablename__ = "brands"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(Text)
    logo = Column(String, nullable=True)
    website = Column(String, nullable=True)
    featured = Column(Boolean, default=False)
    
    products = relationship("Product", back_populates="brand")

class Product(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True, index=True)
    slug = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, index=True, nullable=False)
    category_id = Column(String, ForeignKey("categories.id"))
    brand_id = Column(String, ForeignKey("brands.id"))
    short_description = Column(Text)
    description = Column(Text)
    image = Column(String)
    featured = Column(Boolean, default=False)
    published = Column(Boolean, default=True)
    has_brochure = Column(Boolean, default=False)
    price = Column(Float, nullable=True)
    inventory_quantity = Column(Integer, default=0)

    category = relationship("Category", back_populates="products")
    brand = relationship("Brand", back_populates="products")
    
    images = relationship("ProductImage", back_populates="product", cascade="all, delete-orphan")
    specifications = relationship("ProductSpecification", back_populates="product", cascade="all, delete-orphan")
    features = relationship("ProductFeature", back_populates="product", cascade="all, delete-orphan")
    applications = relationship("ProductApplication", back_populates="product", cascade="all, delete-orphan")
    benefits = relationship("ProductBenefit", back_populates="product", cascade="all, delete-orphan")

class ProductImage(Base):
    __tablename__ = "product_images"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(String, ForeignKey("products.id"), nullable=False)
    url = Column(String, nullable=False)
    
    product = relationship("Product", back_populates="images")

class ProductSpecification(Base):
    __tablename__ = "product_specifications"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(String, ForeignKey("products.id"), nullable=False)
    key = Column(String, nullable=False)
    value = Column(String, nullable=False)
    
    product = relationship("Product", back_populates="specifications")

class ProductFeature(Base):
    __tablename__ = "product_features"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(String, ForeignKey("products.id"), nullable=False)
    feature = Column(String, nullable=False)
    
    product = relationship("Product", back_populates="features")

class ProductApplication(Base):
    __tablename__ = "product_applications"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(String, ForeignKey("products.id"), nullable=False)
    application = Column(String, nullable=False)
    
    product = relationship("Product", back_populates="applications")

class ProductBenefit(Base):
    __tablename__ = "product_benefits"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(String, ForeignKey("products.id"), nullable=False)
    benefit = Column(String, nullable=False)
    
    product = relationship("Product", back_populates="benefits")

class Industry(Base):
    __tablename__ = "industries"
    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    icon = Column(String)
    image = Column(String)

class Solution(Base):
    __tablename__ = "solutions"
    id = Column(String, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    icon = Column(String)
    image = Column(String)
    
    industries = relationship("SolutionIndustry", back_populates="solution", cascade="all, delete-orphan")

class SolutionIndustry(Base):
    __tablename__ = "solution_industries"
    id = Column(Integer, primary_key=True, index=True)
    solution_id = Column(String, ForeignKey("solutions.id"), nullable=False)
    industry_name = Column(String, nullable=False)
    
    solution = relationship("Solution", back_populates="industries")


class Resource(Base):
    __tablename__ = "resources"
    id = Column(String, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    category = Column(String)
    date = Column(Date, default=datetime.date.today)
    type = Column(String)
    published = Column(Boolean, default=True)

class QuoteRequest(Base):
    __tablename__ = "quote_requests"
    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    organization = Column(String)
    email = Column(String, nullable=False)
    phone = Column(String)
    location = Column(String)
    product = Column(String)
    quantity = Column(Integer)
    message = Column(Text)
    date = Column(Date, default=datetime.date.today)
    status = Column(String, default="NEW")
    assigned_to = Column(String, nullable=True)
    cart_items = Column(String, nullable=True)
    
    notes = relationship("QuoteRequestNote", back_populates="quote_request", cascade="all, delete-orphan")

class QuoteRequestNote(Base):
    __tablename__ = "quote_request_notes"
    id = Column(Integer, primary_key=True, index=True)
    quote_request_id = Column(String, ForeignKey("quote_requests.id"), nullable=False)
    note = Column(Text, nullable=False)
    
    quote_request = relationship("QuoteRequest", back_populates="notes")

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    role = Column(String, default="admin")
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Log(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=True)
    action = Column(String, nullable=False)
    entity_type = Column(String, nullable=False)
    entity_id = Column(String, nullable=True)
    details = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    user = relationship("User")

class SiteSetting(Base):
    __tablename__ = "site_settings"
    key = Column(String, primary_key=True, index=True)
    value = Column(Text, nullable=True)
    label = Column(String, nullable=True)  # human-readable label for admin UI
