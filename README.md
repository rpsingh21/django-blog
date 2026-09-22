# Django Blog
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/DRF-3.15-A30000?logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![Pytest](https://img.shields.io/badge/Pytest-Testing-0A9EDC?logo=pytest&logoColor=white)](https://pytest.org/)
[![GitHub Actions](https://img.shields.io/github/actions/workflow/status/rpsingh21/django-blog/ci.yml?logo=github-actions&logoColor=white&label=CI)](https://github.com/rpsingh21/django-blog/actions)
[![GitHub Stars](https://img.shields.io/github/stars/rpsingh21/django-blog?style=flat&logo=github)](https://github.com/rpsingh21/django-blog/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/rpsingh21/django-blog?logo=github)](https://github.com/rpsingh21/django-blog/issues)
[![GitHub Forks](https://img.shields.io/github/forks/rpsingh21/django-blog?logo=github)](https://github.com/rpsingh21/django-blog/network/members)
[![Last Commit](https://img.shields.io/github/last-commit/rpsingh21/django-blog?logo=github)](https://github.com/rpsingh21/django-blog/commits/master)
[![Repo Size](https://img.shields.io/github/repo-size/rpsingh21/django-blog?logo=github)](https://github.com/rpsingh21/django-blog)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)



A Django-based blogging platform with an advanced commenting system, user profiles, Markdown support, post interactions, and image uploads.

## ✨ Features

* 📝 Create, edit, and manage blog posts
* 👤 User authentication and profiles
* 💬 Advanced nested commenting system
* ❤️ Like posts and comments
* ⭐ Favorite posts
* 👍 Upvote and downvote content
* 🏷️ Post tagging
* 🔗 SEO-friendly slug-based post URLs
* 🖼️ Image uploads for posts and user profiles
* 📖 Automatic reading-time calculation
* 👁️ Post view tracking
* 📑 Draft posts
* ✍️ Markdown-based post content
* 🔔 Activity tracking for user interactions
* 🛠️ Django admin support
* 🧪 Pytest configuration for automated testing

## 🏗️ Project Structure

```text
django-blog/
├── account/            # User profiles and account-related functionality
├── activitys/          # Likes, favorites, upvotes and downvotes
├── ang/                # Application/project configuration
├── comments/           # Nested comment system
├── posts/              # Blog posts, tags and post-related logic
├── static/             # Static assets
├── templates/          # Django templates
├── .devcontainer/      # Development container configuration
├── .github/
│   └── workflows/      # GitHub Actions
├── .vscode/             # VS Code configuration
├── manage.py            # Django management utility
├── pytest.ini           # Pytest configuration
└── requirements.txt     # Python dependencies
```

## 🧰 Tech Stack

| Technology            | Purpose                      |
| --------------------- | ---------------------------- |
| Python                | Backend programming language |
| Django 5.2            | Web framework                |
| Django REST Framework | API functionality            |
| Django MarkdownX      | Markdown content support     |
| django-crispy-forms   | Form rendering               |
| django-filter         | Query filtering              |
| Pillow                | Image processing             |
| Pytest                | Testing                      |

The current dependency file pins Django 5.2.17, Django REST Framework 3.15.2, MarkdownX 4.0.7, Pillow 11.0.0, and the other supporting packages.

## 🚀 Getting Started

### Prerequisites

Make sure you have Python and `pip` installed.

### 1. Clone the repository

```bash
git clone https://github.com/rpsingh21/django-blog.git
cd django-blog
```

### 2. Create a virtual environment

#### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create an admin user

```bash
python manage.py createsuperuser
```

Follow the prompts to create your administrator account.

### 6. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

The project's `manage.py` loads the Django settings through `DJANGO_SETTINGS_MODULE`, so Django management commands can be run directly with `python manage.py ...`.

## 📝 Blog Posts

Posts support several features designed for a full blogging workflow.

Each post can contain:

* Title
* Markdown content
* Tags
* Cover image
* Author
* Unique slug
* View count
* Reading time
* Draft status
* Creation and update timestamps

The post model automatically generates a slug when one is not provided and calculates reading time from the rendered Markdown content. Images are also processed after a post is saved.

### Markdown

Post content is stored as text and rendered using MarkdownX/Markdown functionality.

This makes it possible to write posts using Markdown while displaying formatted content to readers.

Example:

```markdown
# My First Post

This is a **Django** blog post.

## Features

- Markdown
- Comments
- Likes
- Tags
```

## 💬 Advanced Comments

The project includes a hierarchical comment system.

Comments support:

* Authenticated users
* Parent/child relationships
* Nested replies
* Generic relationships
* Timestamps
* Association with different content types

This allows conversations to be structured as:

```text
Post
 ├── Comment
 │    ├── Reply
 │    │    └── Reply
 │    └── Reply
 └── Comment
      └── Reply
```

The comment model uses Django's `ContentType` framework and a self-referencing `parent` relationship to support this structure.

## ❤️ Post Interactions

The activity system supports multiple types of user interactions:

```text
Favorite
Like
Up Vote
Down Vote
```

These activities are associated with users and content through Django's generic relation framework.

## 👤 User Profiles

Each user can have an associated profile containing information such as:

* Bio
* Profile image
* Gender
* Location
* PIN code
* Birth date
* Social profiles

A profile is automatically created when a new Django user is created.

## 🧪 Testing

The project is configured to work with Pytest and Django.

Run the test suite with:

```bash
pytest
```

The repository's `pytest.ini` configures Django to use the project's settings module and recognizes common Django/Pytest test file patterns.

## 🛠️ Development

Useful Django commands:

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start development server
python manage.py runserver

# Run tests
pytest
```

## 🔐 Security

For local development, Django's development server can be used directly.

For production deployment, make sure to properly configure:

* `SECRET_KEY`
* `DEBUG`
* `ALLOWED_HOSTS`
* Database credentials
* Static files
* Media files
* HTTPS
* Secure cookies
* CSRF settings

Never commit production secrets or credentials to the repository.

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/my-feature
```

3. Make your changes
4. Run the tests

```bash
pytest
```

5. Commit your changes

```bash
git commit -m "Add my feature"
```

6. Push the branch

```bash
git push origin feature/my-feature
```

7. Open a Pull Request

## 📌 Roadmap

Potential areas for future improvement:

* REST API documentation
* Improved search functionality
* Pagination
* Email notifications
* Social authentication
* Richer user profiles
* Comment moderation
* Better test coverage
* Production deployment configuration
* Docker-based development and deployment

## 📄 License

No license is currently specified in the repository. If you intend this project to be open source, consider adding an appropriate `LICENSE` file.

## 👨‍💻 Author

**Rohit Singh**

GitHub:
https://github.com/rpsingh21

---

⭐ If you find this project useful, consider starring the repository.

Built with ❤️ using Django.
