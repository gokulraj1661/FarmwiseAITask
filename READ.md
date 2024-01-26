# RESTful API for a Bookstore Management System (FarmwiseAI Pvt Ltd Backend End Developer)

This is a basic RESTful API for a Bookstore management system developed using the Python framework Flask.

## Table of Contents

- **Installation**
- **Configuration**
- **Endpoints**
  - **Add a Book**
  - **Get Book by ISBN**
  - **Delete Book by ID**
  - **Update Book by ID**
  - **Get All Books**
  - **Protected Endpoint with Basic Authentication**
- **BasicAuth**
- **Running the Application**



## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/gokulraj1661/FarmwiseAITask.git
    cd FarmwiseAITask
    ```

2. Set up a virtual environment:
    ```bash
    pip install virtualenv
    virtualenv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Update the `config.py` file with your desired configurations, including the database URI and secret keys.

## Endpoints

1. **Adding a new book:**

   - **URL:** `/add`
   - **Method:** `POST`
   - **Parameters:**
     - `title` (string): Title of the book.
     - `author` (string): Author of the book.
     - `isbn` (string): ISBN of the book.
     - `price` (integer): Price of the book.
     - `quantity` (integer): Quantity of the book.

2. **Retrieving all books:**

   - **URL:** `/getall`
   - **Method:** `GET`

3. **Retrieving a specific book by ISBN:**

   - **URL:** `/getbyisbn/<isbn>`
   - **Method:** `GET`

4. **Updating book details:**

   - **URL:** `/update/<id>`
   - **Method:** `PUT`
   - **Parameters:** (Similar to the "Add a Book" endpoint)

5. **Deleting a book:**

   - **URL:** `/delete/<id>`
   - **Method:** `DELETE`

## BasicAuth

With the help of HTTPBasicAuth, developed a login page where it allows the endpoints access when they pass through the login page. For this API, the username and password are specified here:

- **Username:** `Username`
- **Password:** `password`

## Running the application

```bash
cd app
python main.py

