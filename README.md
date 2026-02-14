# Flask Fullstack Application Template

A modern, simple fullstack web application template built with Python Flask backend and vanilla JavaScript frontend.

## Features

- 🚀 RESTful API with Flask
- 💾 CRUD operations (Create, Read, Update, Delete)
- 🎨 Modern, responsive UI with beautiful design
- 📱 Mobile-friendly interface
- ⚡ Fast and lightweight
- 🔒 CORS enabled for API access

## Project Structure

```
.
├── app.py                 # Flask backend application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main HTML template
├── static/
│   ├── css/
│   │   └── style.css     # Styles
│   └── js/
│       └── app.js        # Frontend JavaScript
└── README.md
```

## Installation

1. **Clone the repository** (or use this template):
   ```bash
   git clone <your-repo-url>
   cd dating-personality
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Flask server**:
   ```bash
   python app.py
   ```

2. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

The application will be running on port 5000 by default.

## API Endpoints

### Get all items
```http
GET /api/items
```

### Get a specific item
```http
GET /api/items/{id}
```

### Create a new item
```http
POST /api/items
Content-Type: application/json

{
  "name": "Item name",
  "description": "Item description"
}
```

### Update an item
```http
PUT /api/items/{id}
Content-Type: application/json

{
  "name": "Updated name",
  "description": "Updated description"
}
```

### Delete an item
```http
DELETE /api/items/{id}
```

## Customization

### Adding a Database

The current implementation uses an in-memory list for data storage. To add a database:

1. Install a database library (e.g., Flask-SQLAlchemy):
   ```bash
   pip install flask-sqlalchemy
   ```

2. Update `app.py` to include database models and connections.

### Styling

- Modify `static/css/style.css` to customize the appearance
- The design uses CSS custom properties (variables) for easy theming

### Adding Features

- Add new routes in `app.py` for additional API endpoints
- Update `static/js/app.js` to add frontend functionality
- Modify `templates/index.html` to add new UI components

## Production Deployment

For production deployment, consider:

1. **Use a production WSGI server** (e.g., Gunicorn):
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

2. **Add a database** (PostgreSQL, MySQL, etc.)

3. **Set up environment variables** for configuration

4. **Use a reverse proxy** (Nginx, Apache)

5. **Enable HTTPS** with SSL certificates

6. **Set `debug=False`** in production

## Technologies Used

- **Backend**: Python 3, Flask
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Custom CSS with modern design principles
- **API**: RESTful architecture

## License

MIT License - feel free to use this template for your projects!

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.