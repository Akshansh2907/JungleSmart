from src.routes import AuthRouter, InvoiceRouter
from src.database import create_db_and_tables, SessionDep, engine
from src.models import User, Store, Bill, ProductCategory, BillItem, Product
from src.schemas import UserSignup, StoreCreate
from sqlmodel import select, func, Session
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import timedelta, datetime
from src.dummy import insert_all_data

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    with Session(engine) as session:
        insert_all_data(session)

@app.get("/")
def root():
    return "Hello"

@app.get("/get_users")
def get_users(session: SessionDep):
    return session.exec(select(User)).all()

@app.post("/create_store")
def create_store(store: StoreCreate, session: SessionDep):
    store_exists = session.exec(select(Store).where(Store.name == store.name)).one_or_none()
    owner = session.exec(select(User).where(User.id == store.owner_id)).one()
    if store_exists:
        return HTTPException(status_code=400, detail="Store already exists")

    new_store = Store(
        name = store.name,
        address = store.address
    )

    session.add(new_store)
    session.commit()
    session.refresh(new_store)

    owner.store_id = new_store.id
    session.add(owner)
    session.commit()

    return {"message": "Store Created Successfully", "store": new_store }

@app.get("/weekly_data")
def get_weekly_data(session: SessionDep):
    seven_days_ago = datetime.utcnow() - timedelta(days=7)

    result = session.exec(
        select(
            func.to_char(Bill.timestamp, 'Day').label("weekday"),  # Get full weekday name
            func.sum(Bill.total_amount).label("total_sales")  # Sum revenue per day
        )
        .where(Bill.timestamp >= seven_days_ago)  # Filter last 7 days
        .group_by(func.to_char(Bill.timestamp, 'Day'))  # Group by weekday name
        .order_by(func.min(Bill.timestamp))  # Order by earliest timestamp of each day
    ).all()

    # Convert the result into a dictionary
    weekly_sales = [{"day": row[0].strip(), "sales": row[1]} for row in result]
    return weekly_sales

@app.get("/profitable_categories")
def get_profitable_categories(session: SessionDep):
    result = session.exec(
        select(
            ProductCategory.name.label("category"),
            func.sum(BillItem.price).label("total_revenue")  # Sum revenue per category
        )
        .join(Product, Product.id == BillItem.product_id)  # Link BillItem to Product
        .join(ProductCategory, Product.category_id == ProductCategory.id)  # Link Product to Category
        .group_by(ProductCategory.name)  # Group by category name
        .order_by(func.sum(BillItem.price).desc())
        .limit(10)# Order by highest revenue
    ).all()

    # Convert the result into a dictionary
    category_revenue = [{"category": row[0], "revenue": row[1]} for row in result]
    return category_revenue

app.include_router(InvoiceRouter)
app.include_router(AuthRouter)
