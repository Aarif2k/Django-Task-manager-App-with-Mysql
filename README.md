# Task_manager

Overview

Purpose:
The Task Manager application is designed to help users manage their tasks efficiently. It allows users to add, edit, delete, view, and filter tasks based on their priority and status. The application has both a web-based interface and a command-line interface for task management.

Functional Requirements
Add Tasks: Users can add tasks by providing a title, description, priority (High/Medium/Low), and status (Pending/In Progress/Completed).
Edit Tasks: Users can edit existing tasks by specifying the task ID and providing updated information for the title, description, priority, and status.
Delete Tasks: Users can delete tasks by specifying the task ID.
View All Tasks: Users can view all tasks to see a list of all existing tasks along with their details.
Filter Tasks by Priority: Users can filter tasks by priority to view tasks with a specific priority level.

Task and TaskManager Classes
Task Class: Defines the structure of a task with attributes: id, title, description, priority, and status. It includes an __init__ method to initialize these attributes and a __str__ method for string representation.
Django Models, Forms, and Views
Models: Defines the structure of the database. The Task model is used to create and manage tasks.
Forms: Defines how the forms for adding and editing tasks are rendered.
Views: Handles the logic for displaying, adding, editing, and deleting tasks.
URLs: Maps URLs to the corresponding views.
Custom Management Commands
The application includes custom management commands for adding, editing, deleting, viewing, and filtering tasks from the command line.

Error Handling
Form Validation: Django's form validation handles incorrect inputs and displays error messages to guide users in correcting their input errors.
Views Error Handling: Views handle errors such as non-existent task IDs using Django's get_object_or_404 function, which raises a 404 error if the object does not exist.

Conclusion
The Task Manager application provides a robust system for managing tasks via both a web interface and a command-line interface. The project is built using Django, with MySQL as the database backend, ensuring a scalable and reliable application. The detailed structure and error handling mechanisms ensure that the application is user-friendly and efficient in managing tasks.