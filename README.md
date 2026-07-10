# Truva Feedback App

A simple full-stack feedback application built with FastAPI, SQLAlchemy, SQLite, HTML, CSS, and JavaScript.

## Features

- Submit a name and feedback message
- Save feedback in a SQLite database
- Display all submitted feedback on the page
- Serve the frontend from the FastAPI app

## Run locally

### Option 1: Using Python

1. Go to the project folder.
2. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```
3. Start the app:
   ```bash
   uvicorn backend.main:app --reload --host 127.0.0.1 --port 8001
   ```
4. Open http://127.0.0.1:8001

### Option 2: Using Docker

1. Build and start the container:
   ```bash
   docker-compose up --build
   ```
2. Open http://127.0.0.1:8001

## Project Structure

- backend/main.py - FastAPI app and routes
- backend/database.py - SQLite and SQLAlchemy setup
- backend/models.py - Feedback database model
- frontend/index.html - Main page
- frontend/style.css - Styling
- frontend/script.js - Frontend logic
