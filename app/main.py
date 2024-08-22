from fastapi import FastAPI
from routers import product,cart,user,order


app=FastAPI()


# All Routers
app.include_router(user.auth_router)
app.include_router(product.product_router)
app.include_router(cart.cart_router)
app.include_router(order.order_router)



# uvicorn main:app --reload

# if __init__ == "__main__":
#   uvicorn.run(main:app, host="0.0.0.0", port=8000)