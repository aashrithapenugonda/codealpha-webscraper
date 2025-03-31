# Web Scraper GUI

This is a simple web scraper application built with Python and Tkinter. It allows users to enter a URL and scrape the `<h2>` titles from the webpage, displaying them in a scrollable text box.

## Features

-   **User-friendly GUI:** Built using Tkinter for easy interaction.
-   **URL Input:** Allows users to enter any valid URL.
-   **Web Scraping:** Scrapes `<h2>` titles from the provided URL using `requests` and `BeautifulSoup`.
-   **Error Handling:** Handles network errors and other exceptions gracefully.
-   **Scrollable Text Display:** Displays the scraped titles in a scrollable text box.

## Prerequisites

-   Python 3.x
-   `requests` library
-   `beautifulsoup4` library
-   `tkinter` (standard library, usually included with Python)

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    ```

2.  **Install dependencies:**

    ```bash
    pip install requests beautifulsoup4
    ```

## Usage

1.  **Run the application:**

    ```bash
    python web_scraper.py
    ```

2.  **Enter the URL:**
    Type the URL of the webpage you want to scrape into the input field.

3.  **Click "Scrape Titles":**
    Click the "Scrape Titles" button to initiate the scraping process.

4.  **View the results:**
    The scraped `<h2>` titles will be displayed in the scrollable text box.

## Code Structure

-   `web_scraper.py`: Contains the main application logic and GUI code.

## Dependencies

-   `requests`: For making HTTP requests to fetch webpage content.
-   `beautifulsoup4`: For parsing HTML content.
-   `tkinter`: For building the graphical user interface.

## Error Handling

The application handles the following errors:

-   **Network errors:** If the URL is invalid or the network connection fails, an error message will be displayed.
-   **No `<h2>` titles found:** If the webpage does not contain any `<h2>` titles, a message will be displayed.
-   **Unexpected errors:** Any unexpected errors during the scraping process will be caught and displayed.

## Future Improvements

-   Add more options for selecting which HTML tags to scrape.
-   Implement a progress bar to indicate scraping progress.
-   Allow users to save the scraped data to a file.
-   Improve the GUI design and layout.
-   Add functionality to scrape other data like links, images, etc.
-   Add functionality to scrape data from multiple pages.

## Author

[P.Aashritha Mounika]
