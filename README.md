<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://cdn.pixabay.com/photo/2023/11/29/03/44/e-commerce-8418610_1280.png" style="border-radius: 50%;" alt="Project logo"></a>
</p>

<h3 align="center">E-Commerce Api using FastApi</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
<!-- [![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues) -->
<!-- [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls) -->
<!-- [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE) -->

</div>

---
<p align="center"> An E-Commerce API.
    <br> 
</p>


# E-commerce API

This is a fully functional e-commerce API built with FastAPI and MongoDB. The API allows users to register, authenticate, manage products, handle shopping carts, place orders, and process payments.

## Features

- User registration and authentication
- Product management (CRUD operations)
- Shopping cart management
- Order placement and tracking
- Payment processing
- JWT-based authentication
- Asynchronous operations with Pymongo


## Installation

1. Clone the repository:
   ```
    git clone 
    cd app
    ```

2. Create and activate a virtual environment:
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Set up environment variables: Create a .env file in the root directory and add the following:
    ```
    MONGODB_URI=
    SECRET_KEY=
    ```

5. Run the application:
    ```
    uvicorn app.main:app --reload
    ```


## ⛏️ Built Using

- [Python](https://www.python.org/) - Programming Language
- [FastApi](https://fastapi.tiangolo.com/) - APi Framework
- [MongoDB](https://www.mongodb.com/) - Database
- [Uvicorn](https://www.uvicorn.org/) - Server 

## ✍️ Authors

- [@my-selfness](https://github.com/my-selfness) - Idea & Initial work