#How to Use the DMA Printlab Interface!

## Prerequisites

Before running the application, make sure you have the following prerequisites installed:

- Python (version 3 or later)
- Flask (installed via pip)

## Getting Started

1. Clone this repository to your local machine.

2. Navigate to the project directory.

3. Install the required dependencies by running the following command:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the Flask application by running the following command:

   ```bash
   flask run
   ```

   By default, the application will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Usage

Once the application is running, you can access the following routes:

- `/`: Displays the data from the JSON file in a table format.

- `/data`: Returns the raw JSON data.

## Customization

You can customize the application behavior by modifying the `app.py` file and the corresponding HTML and CSS files in the `templates` and `static` directories.
