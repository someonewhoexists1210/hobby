# Hobby Quiz Project

This project is a Django application that allows users to take a quiz to find out which hobby best suits them. The application consists of a model for quiz questions, a view for processing the quiz and suggesting a hobby, and URL configurations to link everything together.

## Features
- Users can answer a series of questions to determine their ideal hobby.
- The app suggests a hobby based on the user's responses.
- You can make new questions as well to be added to the quiz 

## Files Overview

### `models.py`
- Defines the `Question` and `Choice` models.
- `Question`: Represents a quiz question with a text field.
- `Choice`: Represents possible answers linked to a `Question`, each associated with a hobby.

### `views.py`
- Handles the logic for displaying the quiz and processing the user's answers.
- `suggest_hobby`: A view function that processes the quiz form and returns a hobby suggestion based on user input.

### `urls.py`
- Maps URLs to the corresponding views.
- Includes a URL pattern for accessing the quiz and another for submitting answers.

### `suggest.py`
- Contains logic to calculate and suggest a hobby based on the user's quiz responses.

## Setup

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd hobby-quiz-project
2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
3. **Apply Migrations**
    ```bash
    python manage.py migrate
    ```
4. **Run Server**
    ```bash
    python manage.py runserver <port>
    ```
5. **Access App**
    You can access this app at the url given after the previous command

## How to use
This app is available at https://hobbyquiz.someonewhoexists.hackclub.app

## Contribution
Contributing to this project is welcome, just make sure to make pull requests

