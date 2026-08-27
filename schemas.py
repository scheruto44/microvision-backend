from pydantic import BaseModel
from typing import List, Optional
import datetime

# --- Pydantic Base Models & Schemas ---

class ProductImageBase(BaseModel):
    url: str

class ProductImageCreate(ProductImageBase):
    pass

class ProductImage(ProductImageBase):
    id: int
    class Config:
        from_attributes = True


class ProductSpecificationBase(BaseModel):
    key: str
    value: str

class ProductSpecificationCreate(ProductSpecificationBase):
    pass

class ProductSpecification(ProductSpecificationBase):
    id: int
    class Config:
        from_attributes = True


class ProductFeatureBase(BaseModel):
    feature: str

class ProductFeatureCreate(ProductFeatureBase):
    pass

class ProductFeature(ProductFeatureBase):
    id: int
    class Config:
        from_attributes = True


class ProductApplicationBase(BaseModel):
    application: str

class ProductApplicationCreate(ProductApplicationBase):
    pass

class ProductApplication(ProductApplicationBase):
    id: int
    class Config:
        from_attributes = True


class ProductBenefitBase(BaseModel):
    benefit: str

class ProductBenefitCreate(ProductBenefitBase):
    pass

class ProductBenefit(ProductBenefitBase):
    id: int
    class Config:
        from_attributes = True


class ProductBase(BaseModel):
    id: Optional[str] = None
    slug: str
    name: str
    category_id: Optional[str] = None
    brand_id: Optional[str] = None
    short_description: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None
    featured: bool = False
    published: bool = True
    has_brochure: bool = False
    price: Optional[float] = None
    inventory_quantity: Optional[int] = 0

class ProductCreate(ProductBase):
    features: List[ProductFeatureCreate] = []
    specifications: List[ProductSpecificationCreate] = []
    applications: List[ProductApplicationCreate] = []
    benefits: List[ProductBenefitCreate] = []

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    slug: Optional[str] = None
    category_id: Optional[str] = None
    brand_id: Optional[str] = None
    short_description: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None
    featured: Optional[bool] = None
    published: Optional[bool] = None
    has_brochure: Optional[bool] = None
    price: Optional[float] = None
    inventory_quantity: Optional[int] = None
    features: Optional[List[ProductFeatureCreate]] = None
    specifications: Optional[List[ProductSpecificationCreate]] = None
    applications: Optional[List[ProductApplicationCreate]] = None
    benefits: Optional[List[ProductBenefitCreate]] = None

class Product(ProductBase):
    images: List[ProductImage] = []
    specifications: List[ProductSpecification] = []
    features: List[ProductFeature] = []
    applications: List[ProductApplication] = []
    benefits: List[ProductBenefit] = []

    class Config:
        from_attributes = True


class CategoryBase(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    image: Optional[str] = None
    featured: bool = False

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None
    featured: Optional[bool] = None

class Category(CategoryBase):
    products: List[Product] = []
    
    class Config:
        from_attributes = True


class BrandBase(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    logo: Optional[str] = None
    website: Optional[str] = None
    featured: bool = False

class BrandCreate(BrandBase):
    pass

class BrandUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    logo: Optional[str] = None
    website: Optional[str] = None
    featured: Optional[bool] = None

class Brand(BrandBase):
    products: List[Product] = []

    class Config:
        from_attributes = True


class IndustryBase(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    icon: Optional[str] = None
    image: Optional[str] = None

class IndustryCreate(IndustryBase):
    pass

class Industry(IndustryBase):
    class Config:
        from_attributes = True


class SolutionIndustryBase(BaseModel):
    industry_name: str

class SolutionIndustryCreate(SolutionIndustryBase):
    pass

class SolutionIndustry(SolutionIndustryBase):
    id: int
    class Config:
        from_attributes = True


class SolutionBase(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    icon: Optional[str] = None
    image: Optional[str] = None

class SolutionCreate(SolutionBase):
    pass

class Solution(SolutionBase):
    industries: List[SolutionIndustry] = []
    
    class Config:
        from_attributes = True




class ResourceBase(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    category: Optional[str] = None
    date: datetime.date
    type: Optional[str] = None
    published: bool = True

class ResourceCreate(ResourceBase):
    pass

class Resource(ResourceBase):
    class Config:
        from_attributes = True


class QuoteRequestNoteBase(BaseModel):
    note: str

class QuoteRequestNoteCreate(QuoteRequestNoteBase):
    pass

class QuoteRequestNote(QuoteRequestNoteBase):
    id: int
    class Config:
        from_attributes = True


class QuoteRequestBase(BaseModel):
    id: Optional[str] = None
    name: str
    organization: Optional[str] = None
    email: str
    phone: Optional[str] = None
    location: Optional[str] = None
    product: Optional[str] = None
    quantity: Optional[int] = None
    message: Optional[str] = None
    date: Optional[datetime.date] = None
    status: str = "NEW"
    assigned_to: Optional[str] = None

class QuoteRequestItem(BaseModel):
    product_id: str
    quantity: int

class QuoteRequestCreate(QuoteRequestBase):
    cart_items: Optional[List[QuoteRequestItem]] = None

class QuoteRequestUpdate(BaseModel):
    status: Optional[str] = None
    assigned_to: Optional[str] = None
    sold_items: Optional[List[QuoteRequestItem]] = None

class QuoteRequest(QuoteRequestBase):
    cart_items: Optional[str] = None
    notes: List[QuoteRequestNote] = []
    
    class Config:
        from_attributes = True

class UserBase(BaseModel):
    id: str
    email: str
    name: str
    role: str = "admin"
    is_active: bool = True

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    email: Optional[str] = None
    name: Optional[str] = None
    role: Optional[str] = None
    is_active: Optional[bool] = None
    password: Optional[str] = None

class User(UserBase):
    created_at: datetime.datetime
    
    class Config:
        from_attributes = True

class LogBase(BaseModel):
    action: str
    entity_type: str
    entity_id: Optional[str] = None
    details: Optional[str] = None

class LogCreate(LogBase):
    user_id: Optional[str] = None

class Log(LogBase):
    id: int
    user_id: Optional[str] = None
    created_at: datetime.datetime
    
    class Config:
        from_attributes = True

class SiteSettingBase(BaseModel):
    key: str
    value: Optional[str] = None
    label: Optional[str] = None

class SiteSettingUpdate(BaseModel):
    value: Optional[str] = None

class SiteSetting(SiteSettingBase):
    class Config:
        from_attributes = True
