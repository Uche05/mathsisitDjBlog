---
#Mathematics Learning Blog (Django Full-Stack Application)**
---
# MathsIsIt Notes Blog

The **MathsIsIt Notes Blog** is a full-stack Django application designed to provide an educational space where visitors can read maths articles, and registered authors can publish detailed explanations, concepts, and problem-solving guides.

---

## Table of Contents

* [About](#about)
* [User Goals](#user-goals)
* [Site Owner Goals](#site-goals)
* [User Experience](#ux)
* [User Stories](#user-stories)
* [Design](#design)
  * [Colours](#colour-scheme)
  * [Fonts](#fonts)
  * [Structure](#structure)
      * [Website-pages](#webpages)
      * [Database](database)
  * [Wireframes](wireframes)
* [Technologies Used](#tech)
* [Features](#features)
* [Validation](#validation)
* [Testing](#testing)
* [Heroku Deployment](#heroku)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)

---

## Mock-Up Screenshots



<img src="documentation/home_new.png" alt="Homepage mockup">
<img src="documentation/home_new2.png" alt="Blog posts page">
<img src="documentation/home_new3.png" alt="Home page footer">

```
<img src="documentation/home_new.png" alt="Homepage mockup">
<img src="documentation/home_new2.png" alt="Blog posts page">
<img src="documentation/home_new3.png" alt="Home page footer"
```
---

## Basic Content

The Mathematics Learning Blog allows users to:

* Browse public maths posts
* View full article pages
* Register an account
* Log in to access author tools
* Create, edit, and delete their own posts
* Receive clear feedback messages after each action

All sensitive credentials are managed through environment variables for security.

---

# Site Goals


# User Experience (UX)

The design was remade to match the following landing page- Here is the wireframe:

<img src="documentation/wireframehome.png" alt = "Wireframe Picture" >

## Target Audience

This project was created for:

* Students learning mathematics
* Tutors and teachers who want to publish content
* General learners researching maths topics
* Registered authors who write educational content

---

## User Stories
#### Expanded User Stories

**Visitors / Unregistered Users**
- As a visitor, I want to easily navigate the site using keyboard and screen reader.
- As a visitor, I want to know the site is accessible and visually clear.
- As a visitor, I want to see clear error messages if I try to access restricted features.

**Registered Authors**
- As an author, I want to receive validation errors if I submit incomplete or invalid forms.
- As an author, I want to be prevented from creating duplicate posts or using duplicate slugs.
- As an author, I want to see confirmation before deleting a post.
- As an author, I want to be notified if my session expires and I need to log in again.

**Administrator**
- As an admin, I want to filter and search users and posts in the admin panel.
- As an admin, I want to see audit trails of post edits (future enhancement).

**General**
- As any user, I want the site to be responsive and usable on all devices.
- As any user, I want the site to meet accessibility standards (color contrast, ARIA labels, etc).

### **Visitors / Unregistered Users**

* As a visitor, I want to browse mathematics posts.
* As a visitor, I want to read full blog posts.
* As a visitor, I want the site to be easy to use and accessible.

### **Registered Authors**

* As an author, I want to register for an account.
* As an author, I want to log in securely.
* As an author, I want to create new blog posts.
* As an author, I want to edit my posts.
* As an author, I want to delete posts.
* As an author, I want feedback messages after actions (success or error).

### **Administrator**

* As an admin, I want full control of users and posts via Django Admin.

### **Future Enhancements**

* Comment system
* Search functionality
* Post categories and tags
* LaTeX/MathJax rendering for equations
* Bookmark or favourite post
* Profile pictures and author pages
* Comment system with moderation

---

# Pre-development: Design & Database Choices

## Colour Scheme

A clean, professional palette with blue as the primary color, chosen to support long-form reading and accessibility.

| Color Role   | Hex Code    | Usage                             |
| ------------ | ----------- | --------------------------------- |
| Primary      | `#2563eb` | Buttons, links, accents           |
| Primary Dark | `#1d4ed8` | Button hover states               |
| Secondary    | `#059669` | Success states, highlights        |
| Accent       | `#f97316` | Warnings, special calls-to-action |
| Dark         | `#0f172a` | Text, headers                     |
| Light        | `#f8fafc` | Backgrounds, surfaces             |
| Muted        | `#64748b` | Secondary text                    |
| Border       | `#e2e8f0` | Dividers, borders                 |

The color scheme emphasizes clarity and readability for mathematical content.

---

## Typography

Fonts selected for readability:

* **Open Sans**
* **Roboto**
* **Inter**

---

## Flow Diagram
<img src="documentation/flowdig.png" alt="User flow diagram">

### Visitor Flow

Home → Blog List → Blog Detail → Register / Login (optional)

### Author Flow

Login → Dashboard → Create / Edit / Delete → View updates with messages

<img src="documentation/flowdig.png" alt="Wireframes">

## ERD



**Data Dictionary**

## Data Dictionary

### User Model (Django built-in)

The project uses Django’s built-in `User` model for authentication.
Below are the key fields used in this project:

| Field Name   | Type          | Description                                     | Constraints / Notes                                      |
| ------------ | ------------- | ----------------------------------------------- | -------------------------------------------------------- |
| id           | Integer (PK)  | Unique ID for each user                         | Auto-generated primary key                               |
| username     | String        | Unique name used to log in                      | Required, unique, max length ~150                        |
| email        | String        | Email address of the user                       | Optional by default, can be enforced as unique if needed |
| password     | Hashed String | Hashed password for user authentication         | Required, stored as a hash (not plain text)              |
| date_joined  | DateTime      | Timestamp when the account was created          | Auto-set by Django                                       |
| is_active    | Boolean       | Whether the account is active                   | Defaults to True                                         |
| is_staff     | Boolean       | Whether the user can access the admin interface | Defaults to False                                        |
| is_superuser | Boolean       | Full admin permissions flag                     | Defaults to False                                        |

---

### Post Model

The `Post` model stores each mathematics blog article, linking it to a `User` (the author).

| Field Name | Type               | Description                                  | Constraints / Validation                                            |
| ---------- | ------------------ | -------------------------------------------- | ------------------------------------------------------------------- |
| id         | Integer (PK)       | Unique ID for each post                      | Auto-generated primary key                                          |
| author     | ForeignKey → User | User who created the post                    | Required, on delete: CASCADE                                        |
| title      | CharField          | Title of the maths blog post                 | Required, max_length=200                                            |
| slug       | SlugField          | URL-friendly version of the title            | Unique, used for clean URLs                                         |
| content    | TextField          | Main maths explanation / article body        | Required, minimum length validated in form                          |
| created_at | DateTimeField      | Date and time when the post was created      | `auto_now_add=True`                                               |
| updated_at | DateTimeField      | Date and time when the post was last updated | `auto_now=True`                                                   |
| status     | CharField          | Visibility status of the post                | Choices:`draft` / `published`, default=`draft`, max_length=10 |

```
## ERD (Entity Relationship Diagram)

+---------------------------+     1      1     +---------------------------+
|           User            |----------------->|          Profile          |
+---------------------------+                  +---------------------------+
| id (PK)                   |                  | id (PK)                  |
| username                  |                  | user_id (FK → User.id)   |
| email                     |                  +---------------------------+
| password (hashed)         |
| is_staff                  |
| is_superuser              |
| is_active                 |
+---------------------------+
          |
          | 1
          |        ∞
          v
+---------------------------+
|           Post            |
+---------------------------+
| id (PK)                  |
| author_id (FK → User.id) |
| title                    |
| slug (unique)            |
| content                  |
| created_at               |
| updated_at               |
| status                   |
+---------------------------+
          |
          | 1
          |        ∞
          v
+---------------------------+
|         Comment           |
+---------------------------+
| id (PK)                  |
| post_id (FK → Post.id)   |
| author_id (FK → User.id) |
| content                  |
| created_at               |
| approved                 |
+---------------------------+

```

# Features

### Public Features

* Homepage listing all maths posts
* Post detail pages
* Fully responsive layout
* Accessible design

### Author Features

* Registration
* Login/Logout
* Dashboard
* Create maths blog posts
* Edit posts
* Delete posts
* Server-side form validation
* Visual user feedback (success/error messages)

### Admin Features

* Full CRUD via Django Admin
* Manage authors and posts

---

# Tools and Technologies Used

### Core Stack

* **Python 3**
* **Django Framework**
* **HTML5, CSS3, JavaScript**
* **SQLite (development)**
* **Django Test Framework (unittest-based)**
* **WhiteNoise (static file handling in production)**
* **Ruff / Flake8 (PEP8 linting)**
* **Black (code formatting)**

### Developer and Deployment Tools

* Git & GitHub
* GitHub Projects (Agile Kanban)
* VS Code
* Heroku / Render deployment
* PE8 CI Linting
* Django Messages Framework

---

# Agile Development

The project was developed using Agile principles with:

* **Epics**, broken into:

  * Authentication
  * CRUD Blog Posts
  * Database Design
  * UX & Frontend
  * Testing
  * Deployment
* **User stories** linked to tasks
* **GitHub Issues** with labels
* **Kanban board** for sprint organisation

- Throughout development, features were implemented incrementally and verified using
  automated tests before progressing to the next task. Bugs and regressions discovered
  during testing were logged and resolved immediately to ensure stable feature delivery.

# Testing
## User Stories (MathsIsIt Blog)

**Users**
1. As a User I can browse and read mathematics blog posts.
2. As a User I can register for an account to become an author.
3. As a User I can log in and log out securely.
4. As a User I can create, edit, and delete my own blog posts.
5. As a User I can see feedback messages after creating, editing, or deleting a post.
6. As a User I can view my profile and edit my details (future enhancement).
7. As a User I can search for posts or filter by category (future enhancement).
8. As a User I can comment on posts (future enhancement).

**Admin / Authorised User**
1. As an Admin I can log in to access the Django admin backend.
2. As an Admin I can create, read, update, and delete any post.
3. As an Admin I can manage users and moderate content.

**Site Owner**
1. As a Site Owner I can provide a fully responsive site for my users so that they have a good user experience.
2. As a Site Owner I can validate data entered into my site so that all submitted data is correct to avoid errors.

## Manual User Testing

### User Story-Based Manual Testing
### User Story-Based Manual Testing
| **User Story** | **Test Step** | **Expected Result** | **Evidence (Screenshot/Link)** |
|---|---|---|---|
| As a User I can browse and read mathematics blog posts. | Visit homepage and click on blog post titles. | Blog post detail pages load and are readable. |  |
| As a User I can register for an account to become an author. | Click 'Register', fill and submit form. | Account is created, redirected to login. |  |
| As a User I can log in and log out securely. | Log in with valid credentials, then log out. | Dashboard loads after login, homepage after logout. |  |
| As a User I can create, edit, and delete my own blog posts. | Create a post, edit it, then delete it. | Post is created, updated, and deleted with feedback. |  |
| As a User I can see feedback messages after creating, editing, or deleting a post. | Perform post actions. | Success/error messages are shown. |  |
| As a User I can view my profile and edit my details (future). | Go to profile page, edit details. | Profile updates are saved (future). |  |
| As a User I can search for posts or filter by category (future). | Use search/filter UI. | Posts are filtered (future). |  |
| As a User I can comment on posts (future). | Add a comment to a post. | Comment is submitted for moderation (future). |  |
| As an Admin I can log in to access the Django admin backend. | Visit /admin, log in. | Admin dashboard loads. |  |
| As an Admin I can create, read, update, and delete any post. | Use admin to manage posts. | CRUD operations succeed. |  |
| As an Admin I can manage users and moderate content. | Use admin to manage users/comments. | Users/comments are managed. |  |
| As a Site Owner I can provide a fully responsive site. | Resize browser, test on devices. | Layout remains usable and responsive. |  |
| As a Site Owner I can validate data entered into my site. | Submit invalid forms. | Error messages shown, invalid data rejected. |  |

### 1. Navigation and Access
| **Step** | **Expected Result** | **Actual Result** |
|---|---|---|
| Click on 'Home' in the navigation bar | Homepage with list of maths posts loads | Works as expected |
| Click on 'Register' in the navigation bar | Registration page loads | Works as expected |
| Click on 'Login' in the navigation bar | Login page loads | Works as expected |
| Click on 'Dashboard' after login | Dashboard with user's posts loads | Works as expected |
| Click on a post title | Post detail page loads | Works as expected |
| Click on 'Logout' in the navigation bar | User is logged out and redirected | Works as expected |

### 2. Post Management (Author)
| **Step** | **Expected Result** | **Actual Result** |
|---|---|---|
| After login, click 'Create Post' | Post creation form loads | Works as expected |
| Submit valid post form | Post is created, success message shown | Works as expected |
| Edit one of my posts | Edit form loads, changes saved | Works as expected |
| Delete one of my posts | Post is deleted, success message shown | Works as expected |

### 3. Authentication
| **Step** | **Expected Result** | **Actual Result** |
|---|---|---|
| Register with valid details | Account created, redirected to login | Works as expected |
| Login with valid credentials | User is logged in, dashboard shown | Works as expected |
| Logout | User is logged out, homepage shown | Works as expected |

### 4. Feedback and Validation
| **Step** | **Expected Result** | **Actual Result** |
|---|---|---|
| Submit invalid post form (e.g. empty title) | Error message shown, form not submitted | Works as expected |
| Try to edit/delete another user's post | Access denied or not shown | Works as expected |

### 5. (Future) Comments and Search
| **Step** | **Expected Result** | **Actual Result** |
|---|---|---|
| Add a comment to a post | Comment is submitted for moderation | N/A (future) |
| Use search bar to find posts | Posts matching query are shown | N/A (future) |

### 6. Admin
| **Step** | **Expected Result** | **Actual Result** |
|---|---|---|
| Access Django admin at /admin | Admin login page loads | Works as expected |
| Manage users and posts | CRUD operations available | Works as expected |

### 7. Validation and Error Handling
| **Step** | **Expected Result** | **Actual Result** |
|---|---|---|
| Submit registration form with invalid email | Error message shown, registration fails | Works as expected |
| Submit post form with title exceeding max length | Error message shown, form not submitted | Works as expected |
| Try to access dashboard while logged out | Redirected to login page | Works as expected |
| Try to access admin panel as non-admin | Access denied | Works as expected |

### 8. User Experience & Accessibility
| **Step** | **Expected Result** | **Actual Result** |
|---|---|---|
| Navigate site using keyboard only (Tab/Enter) | All interactive elements accessible | Works as expected |
| Use screen reader on homepage | Content is read in logical order | Works as expected |
| Resize browser window/mobile view | Layout remains responsive and usable | Works as expected |
| Check color contrast on text/buttons | Meets accessibility standards | Works as expected |

### 9. Edge Cases
| **Step** | **Expected Result** | **Actual Result** |
|---|---|---|
| Register with an email already in use | Error message shown, registration fails | Works as expected |
| Try to submit a post with only whitespace | Error message shown, form not submitted | Works as expected |
| Attempt to delete a post that does not exist | Error or graceful handling | Works as expected |
| Simultaneous edits to the same post by two users | Last save wins, no crash | Works as expected |

## Testing

Testing was carried out throughout development using Django’s built-in testing framework.

The project includes automated tests covering:

- CRUD functionality for blog posts (Create, Read, Update, Delete)
- Access control and permissions (author vs non-author)
- Authentication workflows (register, login, logout)
- Form validation and error handling
- Model logic such as slug generation and uniqueness
- Dashboard behaviour and user-specific content filtering

Tests were run regularly using:

python manage.py test

All tests passed successfully after resolving edge cases related to draft post visibility
and production middleware configuration.

# Deployment

Before deployment, all automated tests were executed locally to ensure production
stability. Deployment-specific issues (such as missing middleware dependencies)
were identified through test failures and resolved prior to final release.

The Mathematics Learning Blog was deployed to a cloud platform using these steps:

1. Create a new app on Heroku or Render
2. Set environment variables (SECRET_KEY, DEBUG, DATABASE_URL)
3. Add `requirements.txt`
4. Add `Procfile` (Heroku)
5. Push project to GitHub
6. Connect repo to deployment platform
7. Deploy
8. Test deployed version for consistency

Security Measures:

* DEBUG=False in production
* Environment variables for secrets
* `.gitignore` excludes sensitive files

---

# Credits

### Code & Documentation Resources

* Django Documentation
* W3C Validators
* StackOverflow
* Code Institute
* ChatGPT (debug support, explanations)

### Acknowledgements

Thanks to classmates, instructors, and mentors for feedback and guidance during development.

---

# 8. Summary

All key requirements for a fully functioning CRUD application were tested thoroughly.
Authentication, responsiveness, and database operations all behave as expected. This work involved some edits and suggestions from ChatGPT due to time constraints on my part plus what I took from the I think before I post blog lesson. Kind regards.

---
