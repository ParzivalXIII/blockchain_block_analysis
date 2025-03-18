import matplotlib.pyplot as plt
from datetime import datetime

# 🔵 Plot Fee Trends per Block (Line + Histogram)
def plot_fee_trends(fee_info):
    if not fee_info:
        print("⚠️ No block fee data to visualize.")
        return

    block_heights = [b['height'] for b in fee_info]
    total_fees = [b['fee_total_btc'] for b in fee_info]

    # Line Plot — Fee per Block
    plt.figure(figsize=(12, 5))
    plt.plot(block_heights, total_fees, marker='o', linestyle='-', color='blue')
    plt.xlabel("Block Height")
    plt.ylabel("Total Fees")
    plt.title("Total Fees per Block")
    plt.gca().invert_xaxis()  # Show newest block on the left
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Histogram — Fee Distribution
    plt.figure(figsize=(8, 5))
    plt.hist(total_fees, bins=10, color='skyblue', edgecolor='black')
    plt.xlabel("Fee Amount ")
    plt.ylabel("Number of Blocks")
    plt.title("Histogram: Block Fee Distribution")
    plt.tight_layout()
    plt.show()

# 🟢 Visualize Transaction Scatter Plot (All Chains)
def visualize_transactions(transactions, chain='polygon'):
    if not transactions:
        print("⚠️ No transactions to visualize.")
        return

    values = []
    fees = []
    timestamps = []

    for tx in transactions:
        if chain == 'bitcoin' and isinstance(tx['value'], float):
            value = tx['value']
            fee = tx['fee']
        else:
            value = int(tx['value'], 16) / 1e18
            gas_price = int(tx['gasPrice'], 16)
            gas_used = int(tx['gas'], 16)
            fee = (gas_price * gas_used) / 1e18

        block_ts = tx.get('block_timestamp')
        timestamp = datetime.utcfromtimestamp(block_ts) if block_ts else datetime.now()

        values.append(value)
        fees.append(fee)
        timestamps.append(timestamp)

    colors = ['green' if f < 0.0001 else 'orange' if f < 0.001 else 'red' for f in fees]
    max_fee_idx = fees.index(max(fees))

    plt.figure(figsize=(12, 6))
    plt.scatter(timestamps, values, c=colors, edgecolors='k', alpha=0.7)

    plt.scatter(
        [timestamps[max_fee_idx]], [values[max_fee_idx]],
        c='blue', s=150, edgecolors='black',
        label=f"Largest Fee: {fees[max_fee_idx]:.6f} {'BTC' if chain == 'bitcoin' else 'ETH'}"
    )

    plt.xlabel("Timestamp (UTC)")
    plt.ylabel(f"Transaction Value ({'BTC' if chain == 'bitcoin' else 'ETH'})")
    plt.title(f"{chain.capitalize()} Transactions: Value vs Fee")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
