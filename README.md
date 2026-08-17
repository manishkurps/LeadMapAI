# LeadMapAI — Google Maps Business Lead Scraper

LeadMapAI is a Python-based business lead generation and data scraping application that collects publicly available business information from Google Maps.

The application uses **Playwright** for browser automation and **Streamlit** to provide a simple and interactive user interface. Scraped business data can be exported into structured **Excel and JSON files**.

---

## 🚀 Features

* 🔎 Search businesses using custom Google Maps search queries
* 🌐 Automated browser interaction using Playwright
* 📊 Interactive Streamlit user interface
* 🏢 Extract business information from Google Maps
* 🔄 Automated scrolling through search results
* 📋 Extract business cards and detailed business information
* 📁 Export scraped data to Excel
* 📄 Export scraped data to JSON
* ⚙️ Configurable scraping settings
* 📝 Automatic output filename generation
* 🧩 Modular project architecture
* 🛠️ Separate scraping, data-model, utility, and export components

---

## 🛠️ Tech Stack

| Technology  | Purpose                                           |
| ----------- | ------------------------------------------------- |
| Python      | Core programming language                         |
| Playwright  | Browser automation and web scraping               |
| Streamlit   | Interactive web application interface             |
| Pandas      | Data processing and tabular data handling         |
| Excel       | Structured data export                            |
| JSON        | Structured data export                            |
| Google Maps | Source of publicly available business information |

---

## 🏗️ Project Architecture

LeadMapAI follows a modular architecture where different parts of the application are separated according to their responsibilities.

```text
                    ┌─────────────────────┐
                    │      Streamlit      │
                    │       app.py        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Google Maps       │
                    │     Scraper         │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                ▼
        Browser Control    Result Cards     Details
        browser.py         cards.py         details.py
              │                │                │
              └────────────────┼────────────────┘
                               ▼
                       Data Extraction
                        extractor.py
                               │
                               ▼
                       Business Model
                        business.py
                               │
                    ┌──────────┴──────────┐
                    ▼                     ▼
              Excel Export           JSON Export
           excel_export.py          json_export.py
```

---

## 📂 Project Structure

```text
LeadMapAI/
│
├── app.py
│   └── Streamlit application and user interface
│
├── config.py
│   └── Application configuration and scraping settings
│
├── requirements.txt
│   └── Python project dependencies
│
├── assets/
│   └── Application assets
│
├── exporter/
│   ├── excel_export.py
│   │   └── Export scraped data to Excel
│   │
│   └── json_export.py
│       └── Export scraped data to JSON
│
├── models/
│   └── business.py
│       └── Business data model
│
├── scraper/
│   ├── __init__.py
│   ├── browser.py
│   │   └── Browser initialization and Playwright management
│   │
│   ├── cards.py
│   │   └── Business search-result card handling
│   │
│   ├── details.py
│   │   └── Business detail extraction
│   │
│   ├── extractor.py
│   │   └── Data extraction logic
│   │
│   ├── google_maps.py
│   │   └── Main Google Maps scraping workflow
│   │
│   ├── scroll.py
│   │   └── Search-result scrolling and loading
│   │
│   └── selectors.py
│       └── Google Maps element selectors
│
├── utils/
│   ├── __init__.py
│   └── filename.py
│       └── Output filename generation utilities
│
├── .gitignore
│   └── Files and directories excluded from Git
│
└── README.md
    └── Project documentation
```

---

## ⚙️ Configuration

Project-level configuration is managed through:

```text
config.py
```

For example, the maximum number of businesses to scrape can be configured using:

```python
MAX_BUSINESSES = 10
```

You can change this value depending on your scraping requirement.

Example:

```python
MAX_BUSINESSES = 25
```

---

## 💻 Installation

### 1. Clone the repository

```bash
git clone https://github.com/manishkurps/LeadMapAI.git
```

Move into the project directory:

```bash
cd LeadMapAI
```

---

### 2. Create a virtual environment

For Windows:

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Install Playwright browsers

Playwright requires browser binaries in addition to the Python package.

Run:

```bash
playwright install
```

---

## ▶️ Running LeadMapAI

Start the Streamlit application:

```bash
streamlit run app.py
```

Streamlit will start a local web server.

Open the URL displayed in the terminal, normally:

```text
http://localhost:8501
```

---

## 🔍 How LeadMapAI Works

The application follows this workflow:

```text
User enters search query
          │
          ▼
    Streamlit Interface
          │
          ▼
      Playwright
          │
          ▼
      Google Maps
          │
          ▼
   Search Result Cards
          │
          ▼
    Business Details
          │
          ▼
     Data Extraction
          │
          ▼
    Business Objects
          │
          ▼
   ┌──────┴──────┐
   ▼             ▼
 Excel           JSON
```

### 1. User enters a search query

The user provides a Google Maps business search query through the Streamlit application.

Example:

```text
Restaurants in Bengaluru
```

Other examples:

```text
Software companies in Bengaluru
```

```text
Digital marketing agencies in Mumbai
```

```text
Hotels in Delhi
```

---

### 2. Playwright launches the browser

LeadMapAI uses Playwright to automate browser interaction with Google Maps.

The browser automation layer is handled inside:

```text
scraper/browser.py
```

---

### 3. Google Maps search results are loaded

The application performs the search and loads the available business results.

The scrolling functionality is handled by:

```text
scraper/scroll.py
```

This allows additional search results to be loaded as required.

---

### 4. Business cards are processed

Search-result cards are handled by:

```text
scraper/cards.py
```

The application identifies relevant business results and processes them for further extraction.

---

### 5. Business details are extracted

Detailed business information is handled through:

```text
scraper/details.py
scraper/extractor.py
```

The extracted information is represented using the business model defined in:

```text
models/business.py
```

---

### 6. Data is exported

After the scraping process, the collected information can be exported into structured formats.

### Excel

Handled by:

```text
exporter/excel_export.py
```

### JSON

Handled by:

```text
exporter/json_export.py
```

---

## 📊 Example Workflow

Suppose the user enters:

```text
Restaurants in Bengaluru
```

and the configuration contains:

```python
MAX_BUSINESSES = 10
```

LeadMapAI will:

1. Open Google Maps through Playwright.
2. Search for the requested businesses.
3. Load the available search results.
4. Scroll through the results when required.
5. Extract business information.
6. Store the information using the business model.
7. Export the collected data.
8. Generate an appropriate output filename.

---

## 📁 Output

LeadMapAI supports structured data export in:

### Excel

```text
.xlsx
```

### JSON

```text
.json
```

The output filename can be generated based on the search performed using the utility in:

```text
utils/filename.py
```

Generated output files are intentionally excluded from the Git repository through `.gitignore`.

---


## 🎯 Use Cases

LeadMapAI can be useful for:

* Business lead generation
* Local business research
* Market research
* Competitor research
* Sales prospecting
* Business directory creation
* Data collection
* Exploratory data analysis
* Business intelligence workflows

---

## 🔮 Future Improvements

Potential future enhancements include:

* Advanced search filters
* Duplicate business detection
* Additional export formats
* Database integration
* Better scraping error handling
* Retry mechanisms
* Improved Google Maps selector management
* Search history
* Scraping analytics dashboard
* Cloud deployment
* Scheduled scraping workflows
* Lead scoring and qualification
* Integration with CRM systems

---

## ⚠️ Disclaimer

This project is intended for educational, research, and legitimate business-data use cases.

Users are responsible for ensuring that their use of this project complies with applicable laws, website terms of service, and Google's policies.

Only information that is publicly available through the application should be collected. Users should not attempt to access private, restricted, or protected information.

---

## 👨‍💻 Author

**Manish Kumar**

GitHub:
https://github.com/manishkurps


---
