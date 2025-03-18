import requests
from time import sleep
from datetime import datetime

BASE_URL = "https://api.blockchair.com/bitcoin/blocks?limit={}"

def fetch_bitcoin_blocks(num_blocks=10):
    url = BASE_URL.format(num_blocks)
    response = requests.get(url)

    if response.status_code != 200:
        print(f"❌ Failed to fetch blocks from Blockchair. Status: {response.status_code}")
        return []

    blocks = response.json().get('data', [])
    all_transactions = []
    block_fees_info = []

    for block in blocks:
        block_ts = datetime.strptime(block['time'], "%Y-%m-%d %H:%M:%S").timestamp()
        block_height = block['id']
        tx_count = block['transaction_count']
        fee_total_btc = block['fee_total'] / 1e8  # Satoshi to BTC
        value_total_btc = block['output_total'] / 1e8

        avg_fee_per_tx = fee_total_btc / tx_count if tx_count else 0
        avg_value_per_tx = value_total_btc / tx_count if tx_count else 0

        # Simulate each transaction
        for _ in range(tx_count):
            tx_data = {
                'value': avg_value_per_tx,
                'fee': avg_fee_per_tx,
                'block_timestamp': block_ts,
                'block_height': block_height
            }
            all_transactions.append(tx_data)

        block_fees_info.append({
            'height': block_height,
            'fee_total_btc': fee_total_btc,
            'tx_count': tx_count
        })

        print(f"✅ Block {block_height}: {tx_count} TXs, {fee_total_btc:.8f} BTC fees")

        sleep(0.2)

    print(f"\n📦 Fetched {len(blocks)} blocks, {len(all_transactions)} simulated transactions.")
    return all_transactions, block_fees_info
