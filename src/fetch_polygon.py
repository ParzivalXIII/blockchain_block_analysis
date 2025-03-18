import requests
from datetime import datetime
from time import sleep
from src.config import POLYGON_API_KEY

BASE_URL = "https://api.polygonscan.com/api"

def fetch_polygon_blocks(num_blocks=10):
    latest_block_url = f"{BASE_URL}?module=proxy&action=eth_blockNumber&apikey={POLYGON_API_KEY}"
    response = requests.get(latest_block_url)
    latest_block_hex = response.json().get("result")
    latest_block_int = int(latest_block_hex, 16)

    all_transactions = []
    block_fees_info = []

    for block_num in range(latest_block_int, latest_block_int - num_blocks, -1):
        hex_block_num = hex(block_num)
        block_url = f"{BASE_URL}?module=proxy&action=eth_getBlockByNumber&tag={hex_block_num}&boolean=true&apikey={POLYGON_API_KEY}"
        block_resp = requests.get(block_url)

        if block_resp.status_code != 200:
            print(f"❌ Failed to fetch block {block_num}")
            continue

        block_data = block_resp.json().get("result", {})
        block_ts = int(block_data.get("timestamp", "0x0"), 16)
        txs = block_data.get("transactions", [])
        tx_count = len(txs)

        block_fee_total = 0.0
        block_value_total = 0.0

        for tx in txs:
            value = int(tx.get('value', '0x0'), 16) / 1e18
            gas = int(tx.get('gas', '0x0'), 16)
            gas_price = int(tx.get('gasPrice', '0x0'), 16)
            fee = (gas * gas_price) / 1e18

            tx_data = {
                'value': tx.get('value', '0x0'),
                'gas': tx.get('gas', '0x0'),
                'gasPrice': tx.get('gasPrice', '0x0'),
                'block_timestamp': block_ts
            }
            all_transactions.append(tx_data)

            block_fee_total += fee
            block_value_total += value

        block_fees_info.append({
            'height': block_num,
            'fee_total_btc': block_fee_total,  # ETH but using BTC key for consistency
            'tx_count': tx_count
        })

        print(f"✅ Polygon Block {block_num}: {tx_count} TXs, {block_fee_total:.6f} ETH fees")
        sleep(0.2)

    print(f"\n📦 Polygon: {num_blocks} blocks, {len(all_transactions)} transactions")
    return all_transactions, block_fees_info
