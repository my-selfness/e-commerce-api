from pymongo import MongoClient
from dotenv import load_dotenv
import os

# load env
load_dotenv()

uri = os.getenv("MONGODB_URI")

client=MongoClient(uri)

db=client.ecom_store

user_collection=db["ecom_user"]
product_collection=db["ecom_product"]
cart_collection=db["ecom_cart"]
order_collection=db["ecom_order"]