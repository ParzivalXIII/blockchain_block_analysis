# Blockchain Block Analysis CLI 🔍⛓️

A Python-based CLI tool for fetching and visualizing blockchain block and transaction data from multiple chains (Polygon, Ethereum, Bitcoin). Designed for **on-chain analytics**, **fee trend analysis**, and **transaction insights**.

---

## 📦 Features
- ✅ **Multi-chain support** via CLI:
  - Polygon (via Polygonscan)
  - Ethereum (via Etherscan)
  - Bitcoin (via Blockchair API)
- ✅ **Visualize Transactions**:
  - Scatter plot of **Transaction Value vs Fee**
  - Supports both **ETH** and **BTC**
- ✅ **Bitcoin Fee Trend Analysis**:
  - Line plot of **Total Fees per Block**
  - Histogram of **Fee Distribution**
- ⚙️ Designed for extensibility (modular fetch + visualize logic)

---

## 🚀 Quick Start

### 1. Clone the Repo
```bash
git clone https://github.com/ParzivalXIII/blockchain_block_analysis.git
cd blockchain_block_analysis
```

### 2. Set up Virtual Environment
```bash
python -m venv venv

# Activate:

# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## 🔑 API Key Setup
Create a file named ```keys.env``` in the root directory:
```bash
POLYGON_API_KEY=your_polygon_key_here
ETHEREUM_API_KEY=your_ethereum_key_here
BLOCKCHAIR_API_KEY=your_blockchair_key_here
```

## 🛠️ Usage
CLI Command
```bash
python main.py --chain bitcoin --blocks 10
```
Options:
* ```---chain```: ```polygon```, ```ethereum```, ```bitcoin```
* ```---blocks```: Number of recent blocks to analyze (default: 10)

## 📊 Visual Outputs
***Fee Trends per Block***	    |    ***Fee Distribution Histogram***

## 🗂️ Project Structure
```bash
blockchain_block_analysis/
│
├── main.py
├── keys.env             
├── requirements.txt
├── README.md
├── .gitignore
├── /src/
│   ├── config.py
│   ├── fetch_polygon.py
│   ├── fetch_ethereum.py
│   ├── fetch_bitcoin.py
│   └── visualization.py
└── /screenshots/        # (optional) Save plots here
```

## 📌 Dependencies
* ```requests```
* ```matplotlib```
* ```python-dotenv```
install via:
```bash
pip install -r requirements.txt
```

## 📄 License
MIT license

## 🌐 Author
ParzivalXIII - Data Analyst & Web3 Enthusiast
[GitHub](https://github.com/ParzivalXIII)
```yaml

---

# ✅ What’s Included:
| Feature               | Included ✅       |
|-----------------------|------------------|
| Multi-chain support   | ✅               |
| Fee trends + visuals  | ✅               |
| API loader (`keys.env`)| ✅              |
| Repo polish & links   | ✅               |
| Ready for engagement  | ✅ Discussions   |

```
