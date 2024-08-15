from fastapi import FastAPI
from routers import product


app=FastAPI()


# All Routers
app.include_router(product.product_router)



# uvicorn main:app --reload

# if __init__ == "__main__":
#   uvicorn.run(main:app, host="0.0.0.0", port=8000)