# Project Name

## Description

It's a flask based web application for converting black and white images into colored images.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

```
Colorado
├── .gitignore
├── App
│   ├── .env
│   ├── .env_demo
│   ├── auth.py
│   ├── models.py
│   ├── static
│   │   ├── css
│   │   │   └── styles.css
│   │   ├── js
│   │   └── Logo.png
│   ├── templates
│   │   ├── Footer.html
│   │   ├── Home.html
│   │   ├── index.html
│   │   ├── Login.html
│   │   ├── Profile.html
│   │   └── Signup.html
│   ├── tests
│   ├── views.py
├── instance
│   └── database.db
├── main.py
├── requirements.txt
└── venv
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/shubhamathawane/Colorado
   ```

2. Navigate to the project directory:

   ```bash
   cd Colorado
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
6. Configuration
### SQLAlchemy URL And API Key
You can set the SQLAlchemy database URL in the `.env` file as follows:
```
API_KEY = 66177db019f3c16343c14895_c7d1aae0434b5b6f27d5_apyhitools
DB_URLS = sqlite:///db_name
```

### I have used this api [phot.ai](https://www.phot.ai/developers) [ it gives 25 credites ].
