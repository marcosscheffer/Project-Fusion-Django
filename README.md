
# Project Fusion Django

## Description
Project Fusion is a website developed with Django, a powerful and flexible web framework in Python. This project serves as an example of a modern and scalable site with a robust architecture.

## Requirements
Before you begin, make sure you have the following installed on your machine:
- Python 3.7 or higher
- pip (Python package manager)
- virtualenv (optional, but recommended)

## Installation
Follow the steps below to set up the development environment:

1. **Clone the repository:**

   ```bash
   git clone git@github.com:marcosscheffer/Project-Fusion-Django.git
   cd Project-Fusion-Django
   ```

2. **Create and activate a virtual environment:**

   On Unix or macOS:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   On Windows:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create environment variables:**

   4.1. **Create a .env file**

   ```bash
   echo. > .env
   ```

   4.2. **Add environment variables**

   Open the `.env` file with your preferred text editor and add the following lines:

   ```plaintext
   MYSQL_USERNAME=yourusername
   MYSQL_PASSWORD=yourpassword
   ```

5. **Run migrations:**

   ```bash
   python manage.py migrate
   ```
   
6. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

7. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create an admin user for the Django admin interface.

## Starting the Site
Once you have set up the environment and dependencies, you can start the website with the following command:

```bash
python manage.py runserver
```

Access the site at `http://127.0.0.1:8000`.

To access the Django admin interface, go to `http://127.0.0.1:8000/admin` and log in with the superuser credentials you created earlier.

## Code Coverage

To ensure code quality, we use `coverage.py` to measure test coverage. Follow the steps below to generate and view the code coverage report.

### Installation

`coverage.py` should already be included in the `requirements.txt` file. If not, add the following line to `requirements.txt`:

```plaintext
coverage
```

Then, install the dependency:

```bash
pip install -r requirements.txt
```

### Running Tests with Coverage

1. **Run the tests and generate coverage data:**

   ```bash
   coverage run manage.py test
   ```

   This command runs all Django tests and collects coverage data. The `--source='.'` option indicates that we want to measure coverage for the entire project.

2. **Generate the coverage report:**

   To generate a simple report in the console:

   ```bash
   coverage report
   ```

   To generate a detailed HTML report:

   ```bash
   coverage html
   ```

3. **View the HTML report:**

   The HTML report will be generated in the `htmlcov` directory. To view it, open the `index.html` file in your browser:

   ```bash
   open htmlcov/index.html  # On macOS
   xdg-open htmlcov/index.html  # On Linux
   start htmlcov/index.html  # On Windows
   ```

### Coverage Configuration

Make sure the `.coveragerc` file is correctly configured. Here is an example configuration you can use:

```ini
[run]
branch = True
source = .

[report]
omit = 
    */__init__.py
    */settings.py
    */manage.py
    */wsgi.py
    */apps.py
    */urls.py
    */admin.py
    */asgi.py
    */migrations/*
    */tests/*
```

### Additional Tips

- **Excluding irrelevant code:** Use the `omit` option in the `.coveragerc` file to exclude files or directories that you do not want to measure coverage for, such as migration or test files.

- **Branch analysis:** Enable branch analysis (`branch = True`) in the `.coveragerc` file to get a more detailed view of coverage, including which control flow branches were or were not covered.

- **CI/CD Integration:** Consider integrating `coverage.py` with your CI/CD pipeline to ensure code coverage is measured and reported automatically in each build.


## Project Structure
An overview of the project's directory structure:

```plaintext
Project-Fusion-Django/
├── manage.py
├── fusion/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── core/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── tests/
│       ├── __init__.py
│       ├── test_forms.py
│       ├── test_models.py
│       ├── test_views.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── urls.py
│   ├── models.py
│   └── views.py
├── staticfiles/
├── media/
├── .env
├── .coveragerc
├── requirements.txt
└── README.md
```


## Contribution
To contribute to this project:

1. **Fork the repository.**

   Click on the "Fork" button at the top right corner of the repository page on GitHub to create a copy of the repository under your GitHub account.

2. **Clone your forked repository:**

   ```bash
   git clone git@github.com:marcosscheffer/Project-Fusion-Django.git
   cd Project-Fusion-Django
   ```

3. **Create a new branch for your feature or bug fix:**

   ```bash
   git checkout -b my-feature
   ```

4. **Make your changes.**

   Implement your feature or bug fix.

5. **Commit your changes:**

   ```bash
   git add .
   git commit -m "Add my new feature"
   ```

6. **Push to the branch:**

   ```bash
   git push origin my-feature
   ```

7. **Open a Pull Request.**

   Go to the repository on GitHub and you should see a prompt to open a pull request from your new branch. Click "Compare & pull request," add a description of your changes, and submit the pull request.

### Additional Guidelines

- **Code Style:** Ensure your code follows the project's coding style and conventions.
- **Testing:** Run the tests to ensure your changes do not break the existing code. Add tests for your new features or bug fixes if applicable.
- **Documentation:** Update the documentation to reflect your changes if necessary.

For more information, refer to the [GitHub documentation on creating a pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).


## Contact
For more information, contact [marcosscheffer](mailto:marcosscheffer2989@gmail.com).
