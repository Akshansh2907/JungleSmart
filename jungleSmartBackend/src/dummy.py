import json
from sqlmodel import Session, create_engine
from datetime import datetime
# Assume these models and enums are already imported:
from src.utils import get_password_hash
from src.models import ProductCategory, Product, Customer, Store, User, Bill, BillItem, Stock, PaymentMethod, EmployeeRole

# Replace with your actual database URL.
def insert_all_data(session: Session):
    """
    Loads embedded JSON dummy data, converts it to model instances,
    and inserts all data into the database in one session.
    """
    # Embedded JSON data
    product_categories_json = r'''
    [
      {"id": 1, "name": "Souvenir Category 1"},
      {"id": 2, "name": "Souvenir Category 2"},
      {"id": 3, "name": "Souvenir Category 3"},
      {"id": 4, "name": "Souvenir Category 4"},
      {"id": 5, "name": "Souvenir Category 5"},
      {"id": 6, "name": "Souvenir Category 6"},
      {"id": 7, "name": "Souvenir Category 7"},
      {"id": 8, "name": "Souvenir Category 8"},
      {"id": 9, "name": "Souvenir Category 9"},
      {"id": 10, "name": "Souvenir Category 10"},
      {"id": 11, "name": "Souvenir Category 11"},
      {"id": 12, "name": "Souvenir Category 12"},
      {"id": 13, "name": "Souvenir Category 13"},
      {"id": 14, "name": "Souvenir Category 14"},
      {"id": 15, "name": "Souvenir Category 15"},
      {"id": 16, "name": "Souvenir Category 16"},
      {"id": 17, "name": "Souvenir Category 17"},
      {"id": 18, "name": "Souvenir Category 18"},
      {"id": 19, "name": "Souvenir Category 19"},
      {"id": 20, "name": "Souvenir Category 20"},
      {"id": 21, "name": "Souvenir Category 21"},
      {"id": 22, "name": "Souvenir Category 22"},
      {"id": 23, "name": "Souvenir Category 23"},
      {"id": 24, "name": "Souvenir Category 24"},
      {"id": 25, "name": "Souvenir Category 25"},
      {"id": 26, "name": "Souvenir Category 26"},
      {"id": 27, "name": "Souvenir Category 27"},
      {"id": 28, "name": "Souvenir Category 28"},
      {"id": 29, "name": "Souvenir Category 29"},
      {"id": 30, "name": "Souvenir Category 30"}
    ]
    '''
    products_json = r'''
    [
      {"id": 1, "hsn_code": "HSN0001", "name": "Jungle Souvenir 1", "price": 110, "barcode": "BAR00001", "category_id": 1},
      {"id": 2, "hsn_code": "HSN0002", "name": "Jungle Souvenir 2", "price": 120, "barcode": "BAR00002", "category_id": 2},
      {"id": 3, "hsn_code": "HSN0003", "name": "Jungle Souvenir 3", "price": 130, "barcode": "BAR00003", "category_id": 3},
      {"id": 4, "hsn_code": "HSN0004", "name": "Jungle Souvenir 4", "price": 140, "barcode": "BAR00004", "category_id": 4},
      {"id": 5, "hsn_code": "HSN0005", "name": "Jungle Souvenir 5", "price": 150, "barcode": "BAR00005", "category_id": 5},
      {"id": 6, "hsn_code": "HSN0006", "name": "Jungle Souvenir 6", "price": 160, "barcode": "BAR00006", "category_id": 6},
      {"id": 7, "hsn_code": "HSN0007", "name": "Jungle Souvenir 7", "price": 170, "barcode": "BAR00007", "category_id": 7},
      {"id": 8, "hsn_code": "HSN0008", "name": "Jungle Souvenir 8", "price": 180, "barcode": "BAR00008", "category_id": 8},
      {"id": 9, "hsn_code": "HSN0009", "name": "Jungle Souvenir 9", "price": 190, "barcode": "BAR00009", "category_id": 9},
      {"id": 10, "hsn_code": "HSN0010", "name": "Jungle Souvenir 10", "price": 200, "barcode": "BAR00010", "category_id": 10},
      {"id": 11, "hsn_code": "HSN0011", "name": "Jungle Souvenir 11", "price": 210, "barcode": "BAR00011", "category_id": 11},
      {"id": 12, "hsn_code": "HSN0012", "name": "Jungle Souvenir 12", "price": 220, "barcode": "BAR00012", "category_id": 12},
      {"id": 13, "hsn_code": "HSN0013", "name": "Jungle Souvenir 13", "price": 230, "barcode": "BAR00013", "category_id": 13},
      {"id": 14, "hsn_code": "HSN0014", "name": "Jungle Souvenir 14", "price": 240, "barcode": "BAR00014", "category_id": 14},
      {"id": 15, "hsn_code": "HSN0015", "name": "Jungle Souvenir 15", "price": 250, "barcode": "BAR00015", "category_id": 15},
      {"id": 16, "hsn_code": "HSN0016", "name": "Jungle Souvenir 16", "price": 260, "barcode": "BAR00016", "category_id": 16},
      {"id": 17, "hsn_code": "HSN0017", "name": "Jungle Souvenir 17", "price": 270, "barcode": "BAR00017", "category_id": 17},
      {"id": 18, "hsn_code": "HSN0018", "name": "Jungle Souvenir 18", "price": 280, "barcode": "BAR00018", "category_id": 18},
      {"id": 19, "hsn_code": "HSN0019", "name": "Jungle Souvenir 19", "price": 290, "barcode": "BAR00019", "category_id": 19},
      {"id": 20, "hsn_code": "HSN0020", "name": "Jungle Souvenir 20", "price": 300, "barcode": "BAR00020", "category_id": 20},
      {"id": 21, "hsn_code": "HSN0021", "name": "Jungle Souvenir 21", "price": 310, "barcode": "BAR00021", "category_id": 21},
      {"id": 22, "hsn_code": "HSN0022", "name": "Jungle Souvenir 22", "price": 320, "barcode": "BAR00022", "category_id": 22},
      {"id": 23, "hsn_code": "HSN0023", "name": "Jungle Souvenir 23", "price": 330, "barcode": "BAR00023", "category_id": 23},
      {"id": 24, "hsn_code": "HSN0024", "name": "Jungle Souvenir 24", "price": 340, "barcode": "BAR00024", "category_id": 24},
      {"id": 25, "hsn_code": "HSN0025", "name": "Jungle Souvenir 25", "price": 350, "barcode": "BAR00025", "category_id": 25},
      {"id": 26, "hsn_code": "HSN0026", "name": "Jungle Souvenir 26", "price": 360, "barcode": "BAR00026", "category_id": 26},
      {"id": 27, "hsn_code": "HSN0027", "name": "Jungle Souvenir 27", "price": 370, "barcode": "BAR00027", "category_id": 27},
      {"id": 28, "hsn_code": "HSN0028", "name": "Jungle Souvenir 28", "price": 380, "barcode": "BAR00028", "category_id": 28},
      {"id": 29, "hsn_code": "HSN0029", "name": "Jungle Souvenir 29", "price": 390, "barcode": "BAR00029", "category_id": 29},
      {"id": 30, "hsn_code": "HSN0030", "name": "Jungle Souvenir 30", "price": 400, "barcode": "BAR00030", "category_id": 30}
    ]
    '''
    customers_json = r'''
    [
      {"contact_no": "9000000001", "name": "Customer 1", "total_spent": 1050, "customer_since": "2020-01-01"},
      {"contact_no": "9000000002", "name": "Customer 2", "total_spent": 1100, "customer_since": "2020-01-02"},
      {"contact_no": "9000000003", "name": "Customer 3", "total_spent": 1150, "customer_since": "2020-01-03"},
      {"contact_no": "9000000004", "name": "Customer 4", "total_spent": 1200, "customer_since": "2020-01-04"},
      {"contact_no": "9000000005", "name": "Customer 5", "total_spent": 1250, "customer_since": "2020-01-05"},
      {"contact_no": "9000000006", "name": "Customer 6", "total_spent": 1300, "customer_since": "2020-01-06"},
      {"contact_no": "9000000007", "name": "Customer 7", "total_spent": 1350, "customer_since": "2020-01-07"},
      {"contact_no": "9000000008", "name": "Customer 8", "total_spent": 1400, "customer_since": "2020-01-08"},
      {"contact_no": "9000000009", "name": "Customer 9", "total_spent": 1450, "customer_since": "2020-01-09"},
      {"contact_no": "9000000010", "name": "Customer 10", "total_spent": 1500, "customer_since": "2020-01-10"},
      {"contact_no": "9000000011", "name": "Customer 11", "total_spent": 1550, "customer_since": "2020-01-11"},
      {"contact_no": "9000000012", "name": "Customer 12", "total_spent": 1600, "customer_since": "2020-01-12"},
      {"contact_no": "9000000013", "name": "Customer 13", "total_spent": 1650, "customer_since": "2020-01-13"},
      {"contact_no": "9000000014", "name": "Customer 14", "total_spent": 1700, "customer_since": "2020-01-14"},
      {"contact_no": "9000000015", "name": "Customer 15", "total_spent": 1750, "customer_since": "2020-01-15"},
      {"contact_no": "9000000016", "name": "Customer 16", "total_spent": 1800, "customer_since": "2020-01-16"},
      {"contact_no": "9000000017", "name": "Customer 17", "total_spent": 1850, "customer_since": "2020-01-17"},
      {"contact_no": "9000000018", "name": "Customer 18", "total_spent": 1900, "customer_since": "2020-01-18"},
      {"contact_no": "9000000019", "name": "Customer 19", "total_spent": 1950, "customer_since": "2020-01-19"},
      {"contact_no": "9000000020", "name": "Customer 20", "total_spent": 2000, "customer_since": "2020-01-20"},
      {"contact_no": "9000000021", "name": "Customer 21", "total_spent": 2050, "customer_since": "2020-01-21"},
      {"contact_no": "9000000022", "name": "Customer 22", "total_spent": 2100, "customer_since": "2020-01-22"},
      {"contact_no": "9000000023", "name": "Customer 23", "total_spent": 2150, "customer_since": "2020-01-23"},
      {"contact_no": "9000000024", "name": "Customer 24", "total_spent": 2200, "customer_since": "2020-01-24"},
      {"contact_no": "9000000025", "name": "Customer 25", "total_spent": 2250, "customer_since": "2020-01-25"},
      {"contact_no": "9000000026", "name": "Customer 26", "total_spent": 2300, "customer_since": "2020-01-26"},
      {"contact_no": "9000000027", "name": "Customer 27", "total_spent": 2350, "customer_since": "2020-01-27"},
      {"contact_no": "9000000028", "name": "Customer 28", "total_spent": 2400, "customer_since": "2020-01-28"},
      {"contact_no": "9000000029", "name": "Customer 29", "total_spent": 2450, "customer_since": "2020-01-29"},
      {"contact_no": "9000000030", "name": "Customer 30", "total_spent": 2500, "customer_since": "2020-01-30"}
    ]
    '''
    stores_json = r'''
    [
      {"id": 1, "name": "Safari Shop 1", "address": "1 Safari Road, Jungle City"},
      {"id": 2, "name": "Safari Shop 2", "address": "2 Safari Road, Jungle City"},
      {"id": 3, "name": "Safari Shop 3", "address": "3 Safari Road, Jungle City"},
      {"id": 4, "name": "Safari Shop 4", "address": "4 Safari Road, Jungle City"},
      {"id": 5, "name": "Safari Shop 5", "address": "5 Safari Road, Jungle City"},
      {"id": 6, "name": "Safari Shop 6", "address": "6 Safari Road, Jungle City"},
      {"id": 7, "name": "Safari Shop 7", "address": "7 Safari Road, Jungle City"},
      {"id": 8, "name": "Safari Shop 8", "address": "8 Safari Road, Jungle City"},
      {"id": 9, "name": "Safari Shop 9", "address": "9 Safari Road, Jungle City"},
      {"id": 10, "name": "Safari Shop 10", "address": "10 Safari Road, Jungle City"},
      {"id": 11, "name": "Safari Shop 11", "address": "11 Safari Road, Jungle City"},
      {"id": 12, "name": "Safari Shop 12", "address": "12 Safari Road, Jungle City"},
      {"id": 13, "name": "Safari Shop 13", "address": "13 Safari Road, Jungle City"},
      {"id": 14, "name": "Safari Shop 14", "address": "14 Safari Road, Jungle City"},
      {"id": 15, "name": "Safari Shop 15", "address": "15 Safari Road, Jungle City"},
      {"id": 16, "name": "Safari Shop 16", "address": "16 Safari Road, Jungle City"},
      {"id": 17, "name": "Safari Shop 17", "address": "17 Safari Road, Jungle City"},
      {"id": 18, "name": "Safari Shop 18", "address": "18 Safari Road, Jungle City"},
      {"id": 19, "name": "Safari Shop 19", "address": "19 Safari Road, Jungle City"},
      {"id": 20, "name": "Safari Shop 20", "address": "20 Safari Road, Jungle City"},
      {"id": 21, "name": "Safari Shop 21", "address": "21 Safari Road, Jungle City"},
      {"id": 22, "name": "Safari Shop 22", "address": "22 Safari Road, Jungle City"},
      {"id": 23, "name": "Safari Shop 23", "address": "23 Safari Road, Jungle City"},
      {"id": 24, "name": "Safari Shop 24", "address": "24 Safari Road, Jungle City"},
      {"id": 25, "name": "Safari Shop 25", "address": "25 Safari Road, Jungle City"},
      {"id": 26, "name": "Safari Shop 26", "address": "26 Safari Road, Jungle City"},
      {"id": 27, "name": "Safari Shop 27", "address": "27 Safari Road, Jungle City"},
      {"id": 28, "name": "Safari Shop 28", "address": "28 Safari Road, Jungle City"},
      {"id": 29, "name": "Safari Shop 29", "address": "29 Safari Road, Jungle City"},
      {"id": 30, "name": "Safari Shop 30", "address": "30 Safari Road, Jungle City"}
    ]
    '''
    users_json = r'''
    [
      {"id": 1, "full_name": "Employee 1", "username": "emp1", "contact_no": "8000000001", "email": "employee1@safari.com", "password": "password", "role": "manager", "store_id": 1},
      {"id": 2, "full_name": "Employee 2", "username": "emp2", "contact_no": "8000000002", "email": "employee2@safari.com", "password": "password", "role": "manager", "store_id": 2},
      {"id": 3, "full_name": "Employee 3", "username": "emp3", "contact_no": "8000000003", "email": "employee3@safari.com", "password": "password", "role": "manager", "store_id": 3},
      {"id": 4, "full_name": "Employee 4", "username": "emp4", "contact_no": "8000000004", "email": "employee4@safari.com", "password": "password", "role": "manager", "store_id": 4},
      {"id": 5, "full_name": "Employee 5", "username": "emp5", "contact_no": "8000000005", "email": "employee5@safari.com", "password": "password", "role": "manager", "store_id": 5},
      {"id": 6, "full_name": "Employee 6", "username": "emp6", "contact_no": "8000000006", "email": "employee6@safari.com", "password": "password", "role": "manager", "store_id": 6},
      {"id": 7, "full_name": "Employee 7", "username": "emp7", "contact_no": "8000000007", "email": "employee7@safari.com", "password": "password", "role": "manager", "store_id": 7},
      {"id": 8, "full_name": "Employee 8", "username": "emp8", "contact_no": "8000000008", "email": "employee8@safari.com", "password": "password", "role": "manager", "store_id": 8},
      {"id": 9, "full_name": "Employee 9", "username": "emp9", "contact_no": "8000000009", "email": "employee9@safari.com", "password": "password", "role": "manager", "store_id": 9},
      {"id": 10, "full_name": "Employee 10", "username": "emp10", "contact_no": "8000000010", "email": "employee10@safari.com", "password": "password", "role": "manager", "store_id": 10},
      {"id": 11, "full_name": "Employee 11", "username": "emp11", "contact_no": "8000000011", "email": "employee11@safari.com", "password": "password", "role": "manager", "store_id": 11},
      {"id": 12, "full_name": "Employee 12", "username": "emp12", "contact_no": "8000000012", "email": "employee12@safari.com", "password": "password", "role": "manager", "store_id": 12},
      {"id": 13, "full_name": "Employee 13", "username": "emp13", "contact_no": "8000000013", "email": "employee13@safari.com", "password": "password", "role": "manager", "store_id": 13},
      {"id": 14, "full_name": "Employee 14", "username": "emp14", "contact_no": "8000000014", "email": "employee14@safari.com", "password": "password", "role": "manager", "store_id": 14},
      {"id": 15, "full_name": "Employee 15", "username": "emp15", "contact_no": "8000000015", "email": "employee15@safari.com", "password": "password", "role": "manager", "store_id": 15},
      {"id": 16, "full_name": "Employee 16", "username": "emp16", "contact_no": "8000000016", "email": "employee16@safari.com", "password": "password", "role": "manager", "store_id": 16},
      {"id": 17, "full_name": "Employee 17", "username": "emp17", "contact_no": "8000000017", "email": "employee17@safari.com", "password": "password", "role": "manager", "store_id": 17},
      {"id": 18, "full_name": "Employee 18", "username": "emp18", "contact_no": "8000000018", "email": "employee18@safari.com", "password": "password", "role": "manager", "store_id": 18},
      {"id": 19, "full_name": "Employee 19", "username": "emp19", "contact_no": "8000000019", "email": "employee19@safari.com", "password": "password", "role": "manager", "store_id": 19},
      {"id": 20, "full_name": "Employee 20", "username": "emp20", "contact_no": "8000000020", "email": "employee20@safari.com", "password": "password", "role": "manager", "store_id": 20},
      {"id": 21, "full_name": "Employee 21", "username": "emp21", "contact_no": "8000000021", "email": "employee21@safari.com", "password": "password", "role": "manager", "store_id": 21},
      {"id": 22, "full_name": "Employee 22", "username": "emp22", "contact_no": "8000000022", "email": "employee22@safari.com", "password": "password", "role": "owner", "store_id": 22},
      {"id": 23, "full_name": "Employee 23", "username": "emp23", "contact_no": "8000000023", "email": "employee23@safari.com", "password": "password", "role": "manager", "store_id": 23},
      {"id": 24, "full_name": "Employee 24", "username": "emp24", "contact_no": "8000000024", "email": "employee24@safari.com", "password": "password", "role": "manager", "store_id": 24},
      {"id": 25, "full_name": "Employee 25", "username": "emp25", "contact_no": "8000000025", "email": "employee25@safari.com", "password": "password", "role": "manager", "store_id": 25},
      {"id": 26, "full_name": "Employee 26", "username": "emp26", "contact_no": "8000000026", "email": "employee26@safari.com", "password": "password", "role": "manager", "store_id": 26},
      {"id": 27, "full_name": "Employee 27", "username": "emp27", "contact_no": "8000000027", "email": "employee27@safari.com", "password": "password", "role": "manager", "store_id": 27},
      {"id": 28, "full_name": "Employee 28", "username": "emp28", "contact_no": "8000000028", "email": "employee28@safari.com", "password": "password", "role": "manager", "store_id": 28},
      {"id": 29, "full_name": "Employee 29", "username": "emp29", "contact_no": "8000000029", "email": "employee29@safari.com", "password": "password", "role": "manager", "store_id": 29},
      {"id": 30, "full_name": "Employee 30", "username": "emp30", "contact_no": "8000000030", "email": "employee30@safari.com", "password": "password", "role": "manager", "store_id": 30}
    ]
    '''
    bills_json = r'''
    [
      {"id": 1, "total_amount": 520, "customer_no": "9000000001", "store_id": 1, "timestamp": "2023-03-15T14:30:00", "payment_method": "cash"},
      {"id": 2, "total_amount": 540, "customer_no": "9000000002", "store_id": 2, "timestamp": "2023-03-15T15:00:00", "payment_method": "cash"},
      {"id": 3, "total_amount": 560, "customer_no": "9000000003", "store_id": 3, "timestamp": "2023-03-15T15:30:00", "payment_method": "cash"},
      {"id": 4, "total_amount": 580, "customer_no": "9000000004", "store_id": 4, "timestamp": "2023-03-15T16:00:00", "payment_method": "cash"},
      {"id": 5, "total_amount": 600, "customer_no": "9000000005", "store_id": 5, "timestamp": "2023-03-15T16:30:00", "payment_method": "cash"},
      {"id": 6, "total_amount": 620, "customer_no": "9000000006", "store_id": 6, "timestamp": "2023-03-15T17:00:00", "payment_method": "cash"},
      {"id": 7, "total_amount": 640, "customer_no": "9000000007", "store_id": 7, "timestamp": "2023-03-15T17:30:00", "payment_method": "cash"},
      {"id": 8, "total_amount": 660, "customer_no": "9000000008", "store_id": 8, "timestamp": "2023-03-15T18:00:00", "payment_method": "cash"},
      {"id": 9, "total_amount": 680, "customer_no": "9000000009", "store_id": 9, "timestamp": "2023-03-15T18:30:00", "payment_method": "cash"},
      {"id": 10, "total_amount": 700, "customer_no": "9000000010", "store_id": 10, "timestamp": "2023-03-15T19:00:00", "payment_method": "cash"},
      {"id": 11, "total_amount": 720, "customer_no": "9000000011", "store_id": 11, "timestamp": "2023-03-15T19:30:00", "payment_method": "cash"},
      {"id": 12, "total_amount": 740, "customer_no": "9000000012", "store_id": 12, "timestamp": "2023-03-15T20:00:00", "payment_method": "cash"},
      {"id": 13, "total_amount": 760, "customer_no": "9000000013", "store_id": 13, "timestamp": "2023-03-15T20:30:00", "payment_method": "cash"},
      {"id": 14, "total_amount": 780, "customer_no": "9000000014", "store_id": 14, "timestamp": "2023-03-15T21:00:00", "payment_method": "cash"},
      {"id": 15, "total_amount": 800, "customer_no": "9000000015", "store_id": 15, "timestamp": "2023-03-15T21:30:00", "payment_method": "cash"},
      {"id": 16, "total_amount": 820, "customer_no": "9000000016", "store_id": 16, "timestamp": "2023-03-15T22:00:00", "payment_method": "cash"},
      {"id": 17, "total_amount": 840, "customer_no": "9000000017", "store_id": 17, "timestamp": "2023-03-15T22:30:00", "payment_method": "cash"},
      {"id": 18, "total_amount": 860, "customer_no": "9000000018", "store_id": 18, "timestamp": "2023-03-15T23:00:00", "payment_method": "cash"},
      {"id": 19, "total_amount": 880, "customer_no": "9000000019", "store_id": 19, "timestamp": "2023-03-16T00:00:00", "payment_method": "cash"},
      {"id": 20, "total_amount": 900, "customer_no": "9000000020", "store_id": 20, "timestamp": "2023-03-16T00:30:00", "payment_method": "cash"},
      {"id": 21, "total_amount": 920, "customer_no": "9000000021", "store_id": 21, "timestamp": "2023-03-16T01:00:00", "payment_method": "cash"},
      {"id": 22, "total_amount": 940, "customer_no": "9000000022", "store_id": 22, "timestamp": "2023-03-16T01:30:00", "payment_method": "cash"},
      {"id": 23, "total_amount": 960, "customer_no": "9000000023", "store_id": 23, "timestamp": "2023-03-16T02:00:00", "payment_method": "cash"},
      {"id": 24, "total_amount": 980, "customer_no": "9000000024", "store_id": 24, "timestamp": "2023-03-16T02:30:00", "payment_method": "cash"},
      {"id": 25, "total_amount": 1000, "customer_no": "9000000025", "store_id": 25, "timestamp": "2023-03-16T03:00:00", "payment_method": "cash"},
      {"id": 26, "total_amount": 1020, "customer_no": "9000000026", "store_id": 26, "timestamp": "2023-03-16T03:30:00", "payment_method": "cash"},
      {"id": 27, "total_amount": 1040, "customer_no": "9000000027", "store_id": 27, "timestamp": "2023-03-16T04:00:00", "payment_method": "cash"},
      {"id": 28, "total_amount": 1060, "customer_no": "9000000028", "store_id": 28, "timestamp": "2023-03-16T04:30:00", "payment_method": "cash"},
      {"id": 29, "total_amount": 1080, "customer_no": "9000000029", "store_id": 29, "timestamp": "2023-03-16T05:00:00", "payment_method": "cash"},
      {"id": 30, "total_amount": 1100, "customer_no": "9000000030", "store_id": 30, "timestamp": "2023-03-16T05:30:00", "payment_method": "cash"}
    ]
    '''
    bill_items_json = r'''
    [
      {"id": 1, "product_id": 1, "bill_id": 1, "price": 110},
      {"id": 2, "product_id": 2, "bill_id": 2, "price": 120},
      {"id": 3, "product_id": 3, "bill_id": 3, "price": 130},
      {"id": 4, "product_id": 4, "bill_id": 4, "price": 140},
      {"id": 5, "product_id": 5, "bill_id": 5, "price": 150},
      {"id": 6, "product_id": 6, "bill_id": 6, "price": 160},
      {"id": 7, "product_id": 7, "bill_id": 7, "price": 170},
      {"id": 8, "product_id": 8, "bill_id": 8, "price": 180},
      {"id": 9, "product_id": 9, "bill_id": 9, "price": 190},
      {"id": 10, "product_id": 10, "bill_id": 10, "price": 200},
      {"id": 11, "product_id": 11, "bill_id": 11, "price": 210},
      {"id": 12, "product_id": 12, "bill_id": 12, "price": 220},
      {"id": 13, "product_id": 13, "bill_id": 13, "price": 230},
      {"id": 14, "product_id": 14, "bill_id": 14, "price": 240},
      {"id": 15, "product_id": 15, "bill_id": 15, "price": 250},
      {"id": 16, "product_id": 16, "bill_id": 16, "price": 260},
      {"id": 17, "product_id": 17, "bill_id": 17, "price": 270},
      {"id": 18, "product_id": 18, "bill_id": 18, "price": 280},
      {"id": 19, "product_id": 19, "bill_id": 19, "price": 290},
      {"id": 20, "product_id": 20, "bill_id": 20, "price": 300},
      {"id": 21, "product_id": 21, "bill_id": 21, "price": 310},
      {"id": 22, "product_id": 22, "bill_id": 22, "price": 320},
      {"id": 23, "product_id": 23, "bill_id": 23, "price": 330},
      {"id": 24, "product_id": 24, "bill_id": 24, "price": 340},
      {"id": 25, "product_id": 25, "bill_id": 25, "price": 350},
      {"id": 26, "product_id": 26, "bill_id": 26, "price": 360},
      {"id": 27, "product_id": 27, "bill_id": 27, "price": 370},
      {"id": 28, "product_id": 28, "bill_id": 28, "price": 380},
      {"id": 29, "product_id": 29, "bill_id": 29, "price": 390},
      {"id": 30, "product_id": 30, "bill_id": 30, "price": 400}
    ]
    '''
    stocks_json = r'''
    [
      {"prod_id": 1, "store_id": 1, "quantity": 51, "min_stock_threshold": 10},
      {"prod_id": 2, "store_id": 2, "quantity": 52, "min_stock_threshold": 10},
      {"prod_id": 3, "store_id": 3, "quantity": 53, "min_stock_threshold": 10},
      {"prod_id": 4, "store_id": 4, "quantity": 54, "min_stock_threshold": 10},
      {"prod_id": 5, "store_id": 5, "quantity": 55, "min_stock_threshold": 10},
      {"prod_id": 6, "store_id": 6, "quantity": 56, "min_stock_threshold": 10},
      {"prod_id": 7, "store_id": 7, "quantity": 57, "min_stock_threshold": 10},
      {"prod_id": 8, "store_id": 8, "quantity": 58, "min_stock_threshold": 10},
      {"prod_id": 9, "store_id": 9, "quantity": 59, "min_stock_threshold": 10},
      {"prod_id": 10, "store_id": 10, "quantity": 60, "min_stock_threshold": 10},
      {"prod_id": 11, "store_id": 11, "quantity": 61, "min_stock_threshold": 10},
      {"prod_id": 12, "store_id": 12, "quantity": 62, "min_stock_threshold": 10},
      {"prod_id": 13, "store_id": 13, "quantity": 63, "min_stock_threshold": 10},
      {"prod_id": 14, "store_id": 14, "quantity": 64, "min_stock_threshold": 10},
      {"prod_id": 15, "store_id": 15, "quantity": 65, "min_stock_threshold": 10},
      {"prod_id": 16, "store_id": 16, "quantity": 66, "min_stock_threshold": 10},
      {"prod_id": 17, "store_id": 17, "quantity": 67, "min_stock_threshold": 10},
      {"prod_id": 18, "store_id": 18, "quantity": 68, "min_stock_threshold": 10},
      {"prod_id": 19, "store_id": 19, "quantity": 69, "min_stock_threshold": 10},
      {"prod_id": 20, "store_id": 20, "quantity": 70, "min_stock_threshold": 10},
      {"prod_id": 21, "store_id": 21, "quantity": 71, "min_stock_threshold": 10},
      {"prod_id": 22, "store_id": 22, "quantity": 72, "min_stock_threshold": 10},
      {"prod_id": 23, "store_id": 23, "quantity": 73, "min_stock_threshold": 10},
      {"prod_id": 24, "store_id": 24, "quantity": 74, "min_stock_threshold": 10},
      {"prod_id": 25, "store_id": 25, "quantity": 75, "min_stock_threshold": 10},
      {"prod_id": 26, "store_id": 26, "quantity": 76, "min_stock_threshold": 10},
      {"prod_id": 27, "store_id": 27, "quantity": 77, "min_stock_threshold": 10},
      {"prod_id": 28, "store_id": 28, "quantity": 78, "min_stock_threshold": 10},
      {"prod_id": 29, "store_id": 29, "quantity": 79, "min_stock_threshold": 10},
      {"prod_id": 30, "store_id": 30, "quantity": 80, "min_stock_threshold": 10}
    ]
    '''
    # Parse the JSON strings.
    pc_data = json.loads(product_categories_json)
    prod_data = json.loads(products_json)
    cust_data = json.loads(customers_json)
    store_data = json.loads(stores_json)
    user_data = json.loads(users_json)
    bill_data = json.loads(bills_json)
    bill_item_data = json.loads(bill_items_json)
    stock_data = json.loads(stocks_json)
    
    # Convert dictionaries to model instances.
    product_categories = [ProductCategory(**item) for item in pc_data]
    products = [Product(**item) for item in prod_data]
    customers = [Customer(**item) for item in cust_data]
    stores = [Store(**item) for item in store_data]
    # Convert role string to enum for users.
    users = [User(**{**item, "role": EmployeeRole(item["role"]), "password": get_password_hash(item["password"])}) for item in user_data]
    # Convert payment_method string to enum for bills.
    bills = [Bill(**{**item, "payment_method": PaymentMethod(item["payment_method"])}) for item in bill_data]
    bill_items = [BillItem(**item) for item in bill_item_data]
    stocks = [Stock(**item) for item in stock_data]
    
    # Insert all data in one session.
    all_data = (
        product_categories + products + customers + stores +
            users + bills + bill_items + stocks
    )
    session.add_all(all_data)
    session.commit()
    print("All data has been successfully inserted into the database.")

# To insert the data, simply call the function:
if __name__ == "__main__":
    insert_all_data()
