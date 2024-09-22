# Key-Cabinet

## Overview

Key-Cabinet is a secure, role-based key management system designed to ensure only authorized users can access specific keys. After successful authentication, users can view all keys *but* access only those keys which they are authorized to use. The system also includes an admin panel where administrators can manage users, roles, permissions, and keys. This system is ideal for organizations looking to manage physical key access securely.

## Features

- **Role-Based Access**: Users can only access keys that are authorized for their roles.
- **Admin Panel**: Admins can manage users, roles, keys, and permissions from a secure backend.
- **User Authentication**: Secure login ensures that only authenticated users can access the key management system.
- **Key Access Control**: Users can view, take, and return keys based on their permissions.
- **Permission Management**: Permissions are assigned to roles, allowing fine-grained control over which users can access specific keys.

## Key Components

### User Authentication
The system enforces login authentication to ensure only authorized individuals can access the keys cabinet. Credentials are securely stored in the database, and users are granted access based on their assigned roles.

### Key Management
- **Restricted Access**: Users can access keys only if they have the required permissions.
- **Roles & Permissions**: Admins can create roles and assign permissions to control who can access which keys.

### Admin Panel
Admins can perform CRUD operations (Create, Read, Update, Delete) on:
- **Users**: Manage who can log in to the system.
- **Keys**: Add or remove physical keys.
- **Roles**: Define roles like staff, manager, etc.
- **Permissions**: Control what actions (e.g., view, take, return) users can perform on keys.
- **User-Role Mapping**: Assign roles to users to define their access levels.

## Database Structure

The system uses a relational database with the following tables:

1. **Users**: Stores user credentials.
2. **Access**: Tracks key access records.
3. **Keys**: Stores information about the available keys.
4. **Permissions**: Manages which roles can access which keys.
5. **Roles**: Defines various roles in the system (e.g., staff, admin).
6. **User Roles**: Maps users to their respective roles.

## Setup Instructions

### 1. Install Python
Download and install Python from the official website:
- [Python Downloads](https://www.python.org/downloads/)
- Verify installation by running `python --version` or `python3 --version` in the terminal.

### 2. Install Django
Use `pip` to install Django:
```bash
pip install django
```

### 3. Start the Server
Navigate to the project directory and run the server:
```bash
python manage.py runserver
```
The server will start at `localhost:8000`.

### 4. Admin Access
Admins can access the admin panel at `localhost:8000/admin` using:
- **Username**: `admin`
- **Password**: `admin`

### 5. Read-Only Staff Access
Log in with the following credentials for read-only access to the admin panel:
- **Username**: `staff`
- **Password**: `testuserforapp`

### 6. Add Users, Roles, and Keys
- Add new users and assign them roles through the admin panel.
- Add keys and assign roles with the appropriate permissions to control access to each key.

## Usage

1. **User Login**: After authentication, users can access keys assigned to their roles.
2. **Admin Panel**: Admins can add, remove, or update users, roles, and keys.
3. **Assign Keys**: Admins assign keys to roles in the admin panel.
4. **Access Keys**: Users can view, take, and return keys based on their permissions.

## Screenshots

![Keyapp2](https://github.com/user-attachments/assets/39c52199-d4bb-4a1b-8b9a-750ae8dbcbf3)
![Keyapp3](https://github.com/user-attachments/assets/9ceb26b5-d056-4b46-a808-8e065220aee0)
![Keyapp1](https://github.com/user-attachments/assets/3e20cc65-2674-4390-b535-905e978d4faa)
![Keyapp4](https://github.com/user-attachments/assets/d87ce4a3-8300-4d60-9779-c5c67950a80a)




