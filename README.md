# ZIP Code to State Converter

This project provides a simple tool to convert U.S. ZIP codes into their corresponding state names and two-letter state abbreviations using Python.

---

## Features

- Convert ZIP codes to full U.S. state names
- Get the two-letter state abbreviation for any U.S. ZIP code
---

## Getting Started

Follow these steps to get the project up and running locally using `venv` and `pip`:

### 1. Clone or Download the Repository

Download or clone this repository to your local machine:

```bash
git clone https://github.com/hanifsajid/zipcode-to-state.git
cd zipcode-to-state
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Script
You can now run the ZIP code to state converter script:

```bash
python main.py  --country  --input_file  --output_file   --zipcode_col  --state_code_col --state_col
```
For example: 

```bash
python main.py --country US --input_file Data/dfZip.csv --output_file Data/outputZip.csv --zipcode_col zipcode --state_code_col state_code --state_col state
```

For more advanced usage, see the script’s CLI options using:

```bash
python main.py --help
```

### Powered by pgeocode

This project uses the excellent [pgeocode](https://pypi.org/project/pgeocode/) library.

You can also use it for:

- Calculating distances between ZIP/postal codes
- Geolocation-based lookups
- Querying postal codes in other countries

### License

This project is licensed under the MIT License.
