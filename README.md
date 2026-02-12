# PriceTrackerApp
Python-based automated price tracker using web scraping to monitor mobile phone prices on Amazon, Flipkart, Meesho, and Snapdeal. Sends HTTP requests, parses HTML with BeautifulSoup, compares prices to target values, and logs results. Modular design allows easy scalability and integration with alerts.

🛠️ Technologies & Third-Party Libraries Used

Python 3

Requests – For sending HTTP requests and handling responses

BeautifulSoup (bs4) – For HTML parsing and DOM traversal

Pip – Package manager used for installing and managing dependencies

HTML Parser (html.parser) – For structured HTML parsing

⚙️ Technical Implementation

HTTP request handling with custom headers (User-Agent configuration)

HTML parsing using CSS selectors

DOM element extraction for dynamic price retrieval

Data preprocessing:

String manipulation

Removal of special characters (e.g., commas)

Type conversion (string → float → integer)

Target price comparison logic

Exception handling using try, except, and finally

File handling for persistent result storage

Iterative processing of multiple product URLs

Structured product configuration using lists and dictionaries

Function-based modular design for reusability and maintainability

🧠 Core Python Concepts Applied

Variables and Data Types

Lists and Dictionaries

Loops (for)

Conditional Statements (if-else)

Functions

String Methods (replace(), strip())

Type Casting

Exception Handling

File I/O Operations

Working with External Libraries

Modular Programming

🚀 Key Features

Multi-product tracking support

Cross-platform e-commerce scraping capability

Automated price comparison logic

Persistent output logging

Extendable and scalable design
