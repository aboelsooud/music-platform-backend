# Music Platform Backend

This is a Django REST API project that allows users to interact with a music platform. Users can register and login, browse artists, and listen to albums and songs. Artists can create and manage their own albums and songs. The project uses Celery for asynchronous tasks and Celery Beat for periodic tasks.

This project was my **first backend and Django project** and it also was part of my **internship at bld.ai** company. I learned a lot from this project throughout the internship.

## Key Features

- User authentication and authorization using **knox tokens**
- User profile management and artist verification
- Album and song creation by artists.
- Albums, songs, artists browsing by users.
- Email notifications and reminders
- Celery tasks for **sending mails congratulating artists on new albums**
- Celery beat tasks for **sending daily warning mails to artists who have not created an album for a long time**
- **Pagination** for list views to improve performance and user experience
- **Unit testing** using **pytest** to ensure the quality and reliability of the code

## Installation 

- Make sure you have ***Python 3.9 or higher*** installed on your machine.
- Clone this repository ```https://github.com/aboelsooud/music-platform-backend.git``` or download the source code.
- Install the required Python packages using the `requirements.txt` file ```pip install -r requirements.txt```.
- Create a ```.env``` file with the following variables:
  
  ```shell
  server=<your redis url>
  email=<your email host>
  password=<your email host password>
  ```
  
- Start the Redis server
- Start the Django server, the Celery worker, and the Celery beat scheduler.
  You can use the following commands:

  ```bash
  # Start the Django server
  python manage.py runserver
  
  # Start the Celery worker
  celery -A musicplatform worker -l info
  
  # Start the Celery beat scheduler
  celery -A musicplatform beat -l info
  ```
The Django server will run on ```http://localhost:8000/``` by default. You can use a tool like Postman or curl to test the API endpoints.

## Contributing

This project was built during my internship at bld.ai company. If you want to contribute to this project, please fork the repo and submit a pull request. You can also contact me at ```mahmoudabooelsooud@gmail.com``` for any questions or feedback.
