from sqlmodel import SQLModel, Field, Relationship, Column, Enum
from typing import Optional, List
from datetime import datetime, date
import enum


class PaymentMethod(enum.Enum):
    CASH = "cash"
    UPI = "upi"


class EmployeeRole(enum.Enum):
    MANAGER = "manager"
    CASHIER = "cashier"
    OWNER = "owner"


class Product(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    hsn_code: str = Field(index=True)
    name: str
    price: int = Field(default=0)
    barcode: str
    category_id: int = Field(foreign_key="productcategory.id")

    category: Optional["ProductCategory"] = Relationship(back_populates="products")
    stocks: List["Stock"] = Relationship(back_populates="product")


class ProductCategory(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    name: str

    products: List[Product] = Relationship(back_populates="category")


class Customer(SQLModel, table=True):
    contact_no: str = Field(primary_key=True)
    name: str
    total_spent: int = Field(default=True)
    customer_since: date = Field(default_factory=date.today)

    bills: List["Bill"] = Relationship(back_populates="customer")


class Bill(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    total_amount: int = Field(default=0)
    customer_no: str = Field(foreign_key="customer.contact_no")
    store_id: int = Field(foreign_key="store.id")
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    payment_method: PaymentMethod = Field(sa_column=Column(type_=Enum(PaymentMethod)))

    customer: Optional[Customer] = Relationship(back_populates="bills")
    items: List["BillItem"] = Relationship(back_populates="bill")
    store: Optional["Store"] = Relationship(back_populates="bills")


class BillItem(SQLModel, table=True):
    id: int = Field(primary_key=True, default=None)
    product_id: int = Field(foreign_key="product.id")
    bill_id: int = Field(foreign_key="bill.id")
    price: int = Field(default=0)  # Price when sold

    bill: Optional[Bill] = Relationship(back_populates="items")


class Store(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    name: str
    address: str

    bills: List[Bill] = Relationship(back_populates="store")
    stocks: List["Stock"] = Relationship(back_populates="store")
    employees: List["User"] = Relationship(back_populates="store")


class Stock(SQLModel, table=True):
    prod_id: int = Field(foreign_key="product.id", primary_key=True)
    store_id: int = Field(foreign_key="store.id", primary_key=True)
    quantity: int
    min_stock_threshold: int = Field(default=0)

    product: Optional[Product] = Relationship(back_populates="stocks")
    store: Optional[Store] = Relationship(back_populates="stocks")


class User(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    full_name: str
    username: str
    contact_no: str
    email: str
    password: str

    role: Optional[EmployeeRole] = Field(sa_column=Column(type_=Enum(EmployeeRole)))
    store_id: Optional[int] = Field(foreign_key="store.id")

    store: Optional[Store] = Relationship(back_populates="employees")
