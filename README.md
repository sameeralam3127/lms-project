# Learning Management System (LMS) Project

This Learning Management System (LMS) project is developed using Python and the Django framework. It serves as a platform for managing courses, students, instructors, and various aspects of online learning.

<img width="950" alt="image" src="https://github.com/sameer358/lms-project/assets/24916603/abcca7bb-dce9-4657-b6f2-14d872372238">
<img width="895" alt="image" src="https://github.com/sameer358/lms-project/assets/24916603/103151b0-54d8-41a3-b8e0-6a9df9a9e653">
<img width="573" alt="image" src="https://github.com/sameer358/lms-project/assets/24916603/ac1d69ad-342a-4385-9cf5-cc63125e7d9b">



## Features

- **User Management**: Allows registration, login, and authentication of users including students, instructors, and administrators.
- **Course Management**: Enables the creation, editing, and deletion of courses by instructors.
- **Enrollment**: Students can enroll in courses offered by instructors.
- **Content Management**: Instructors can upload course materials such as documents, videos, and assignments.
- **Grading System**: Instructors can evaluate and grade assignments submitted by students.
- **Discussion Forum**: Provides a platform for students and instructors to interact, ask questions, and discuss course-related topics.
- **Notifications**: Sends notifications to users regarding course updates, assignment deadlines, and other important information.

## Technologies Used

- **Python**: The primary programming language used for backend development.
- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **HTML/CSS**: Used for frontend development and styling.
- **JavaScript**: Provides interactivity on the frontend.
- **SQLite/PostgreSQL**: Used as the database management system for storing application data.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/sameer358/lms-project.git
    ```

2. Navigate to the project directory:

    ```bash
    cd lms-project
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Perform database migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser (admin) account:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Access the application by visiting [http://localhost:8000](http://localhost:8000) in your web browser.

## Usage

- **Admin Panel**: Access the admin panel by going to [http://localhost:8000/admin](http://localhost:8000/admin) and login using the superuser credentials created in step 5.
- **User Registration/Login**: Users can register or login using the respective links provided.
- **Course Management**: Instructors can create, edit, and delete courses from the admin panel.
- **Enrollment**: Students can enroll in courses from the course catalog.
- **Content Management**: Instructors can upload course materials from the course detail page.
- **Grading System**: Instructors can evaluate and grade assignments from the assignment detail page.
- **Discussion Forum**: Users can participate in discussions from the course detail page.

## Contributing

Contributions are welcome! Please feel free to open issues or pull requests for any improvements or features you'd like to add.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- This project was inspired by the growing need for efficient online learning platforms.
- Thanks to the Django community for providing excellent documentation and resources.
