# Social Networking Platform - Backend

This is the backend implementation of a social networking platform using Django and MongoDB. The platform allows users to create profiles, connect with other users, and share posts. The backend provides the necessary API routes to handle user registration, login, profile management, post creation, and connection management.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python (3.9 or higher)
- Django (4.0.4 or higher)
- Django Rest Framework (3.11.2 or higher)
- Other packages mentioned in `requirements.txt` file

## Getting Started

Follow the instructions below to set up and run the project locally.

1. Clone the repository:

   ```bash
   git clone <repository_url>

2. Install the required dependencies::
    ```bash
    pip install -r requirements.txt

3. Create a .env file in the project root directory and configure the necessary environment variables. The .env file should contain the following variables:
    ```bash
    SECRET_KEY=<your_secret_key>
    DEBUG=True
    DATABASE_URL=mongodb://localhost:27017/<database_name>

4. Apply the database migrations:
    ```bash
    python manage.py migrate

5. Run Dev Server:
    ```bash
    python manage.py runserver


## API Routes
## Profile

### Authentication [Login/Gain Token]

- `POST /login/`: User login to obtain an authentication token.

- `POST /register/`: Register a new user.

- `POST /create-profile/`: Create a new profile for the authenticated user.

- `GET /profile/self/`: Get the profile details of the authenticated user.

- `PUT /profile/update/`: Update the profile details of the authenticated user.

- `GET /profiles/`: Get a list of all profiles.


## Posts

- `POST /posts/create/`: Create a new post.

- `GET /posts/`: Get a list of all posts.

- `GET /posts/<int:pk>/`: Get the details of a specific post.

- `POST /posts/<int:pk>/like/`: Like a specific post.

- `POST /posts/<int:pk>/comment/`: Comment on a specific post.

- `POST /posts/<int:pk>/share/`: Share a specific post.


## Connect Users and Get Feeds

- `GET /connections/`: Get the connections of the authenticated user.

- `GET /feed/`: Get the feed of posts from the authenticated user's connections.


## Connections Manager

- `GET /connections-list/`: Get a list of all user connections.

- `POST /connections/create/`: Create a new connection between users.

- `GET /connections/<int:pk>/`: Get the details of a specific connection.


## API Testing

**Note:** Due to some reasons, we couldn't use Postman for testing the APIs on our local machine. However, we have provided an alternative method to test the APIs.

Instead of Postman, we used a Python script with the `requests` library to interact with the APIs. You can find the script and the associated results in the [API Checker.ipynb] Jupyter Notebook file.

The `API Checkers.ipynb` file contains sample requests and the corresponding responses using the `requests` library. You can run the notebook to test the APIs and see the expected results.

Please refer to the `API Checkers.ipynb` file for detailed examples and usage of the API endpoints.

