# Flask API

This is a Flask API for managing health data.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6+
- pip
- virtualenv

### Setting Up

1. Clone the repository:
    ```bash
    git clone https://github.com/ergegananputra/Flask-Basic-CRUD.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Flask-Basic-CRUD
    ```

3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:
    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - On Unix or MacOS:
        ```bash
        source venv/bin/activate
        ```

5. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
6. Import interoperabilitas.sql to MySQL database!

### Running the Application

1. Run the application:
    ```bash
    ptyhon app.py
    ```

The application will be accessible at `http://127.0.0.1:5000`.

## API Endpoints

- POST `/api/kesehatan`: Insert new health data
- PUT `/api/kesehatan/<int:id>`: Update existing health data
- DELETE `/api/kesehatan/<int:id>`: Delete existing health data
- GET `/api/kesehatan/<int:id>`: Get existing health data

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.