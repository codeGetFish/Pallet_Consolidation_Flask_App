# Import the Flask app object from the app module
from app import app

# Check if the script is being run as the main module
if __name__ == "__main__":
    # Run the app with the debug mode set to True
    # This allows for easier debugging in case of any errors
    app.run(debug=True)
