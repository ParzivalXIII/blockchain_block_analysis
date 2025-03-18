import os
from dotenv import load_dotenv

# This loads API keys from keys.env file located at the project root.
# Format in keys.env:
# POLYGONSCAN_API_KEY=your_key_here
# ETHERSCAN_API_KEY=your_key_here
# BLOCKCHAIR_API_KEY=your_key_here


# Load .env file
load_dotenv('keys.env')

# Access API keys
POLYGON_API_KEY = os.getenv("POLYGONSCAN_API_KEY")
ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")
BLOCKCHAIR_API_KEY = os.getenv("BLOCKCHAIR_API_KEY")  # Optional
