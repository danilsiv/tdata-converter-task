# Telegram Session to TData Converter

This asynchronous script scans through all `.session` files in the `accounts/` directory and converts each into a `tdata` folder compatible with Telegram Desktop. The converted `tdata` folders are saved inside `output_tdata/`.

The script uses Python’s `asyncio` and creates separate tasks for parallel execution, which significantly speeds up the process for multiple accounts.

> The `accounts/` and `output_tdata/` directories are included in `.gitignore` because they contain private and sensitive account data.

---

## Installation

### Python 3 must be installed.

1. **Clone the repository and open it with your preferred IDE (e.g. PyCharm):**
   ```bash
   git clone https://github.com/danilsiv/tdata-converter-task.git

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

## Directory Structure

You must manually create the `accounts/` folder and place your account data there. The script will automatically detect `.session` files and ignore others.

**Example file structure:**
```bash
   tdata-converter-task/
├── accounts/
│   ├── acc_1/
│   │   ├── 123456789012.session
│   │   └── 123456789012.json
│   ├── acc_2/
│   │   ├── 987654321098.session
│   │   └── 987654321098.json
├── output_tdata/
│   └── tdata_acc_1/
│       ├── D877F783D5D3EF8C/
│       ├── map0
│       ├── key_data
│       └── ...
├── convert_all.py
├── requirements.txt
└── .gitignore
```

## Running the script

   ```bash
   python convert_all.py
   ```
Once the script is launched:
- it locates all `.session` files inside the `accounts/` directory
- it asynchronously converts each of them into a tdata folder
- it saves the results to `output_tdata/tdata_<account_name>/`

**To use a generated tdata folder with Telegram Desktop, copy it into your Telegram Desktop/tdata/ directory. Be sure to back up your existing data beforehand.**
