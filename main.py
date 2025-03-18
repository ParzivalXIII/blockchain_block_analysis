import argparse
from src.fetch_polygon import fetch_polygon_blocks
from src.fetch_ethereum import fetch_ethereum_blocks
from src.fetch_bitcoin import fetch_bitcoin_blocks
from src.visualization import visualize_transactions, plot_fee_trends

def main():
    parser = argparse.ArgumentParser(description="Blockchain Data Fetcher CLI")
    parser.add_argument('--chain', type=str, choices=['polygon', 'ethereum', 'bitcoin'], default='polygon',
                        help='Blockchain to fetch data from')
    parser.add_argument('--blocks', type=int, default=10,
                        help='Number of latest blocks to analyze')
    args = parser.parse_args()

    if args.chain == 'polygon':
        print(f"🔗 Fetching {args.blocks} Polygon blocks...")
        transactions, fee_info = fetch_polygon_blocks(args.blocks)
        visualize_transactions(transactions, chain='polygon')
        plot_fee_trends(fee_info)

    elif args.chain == 'ethereum':
        print(f"🔗 Fetching {args.blocks} Ethereum blocks...")
        transactions, fee_info = fetch_ethereum_blocks(args.blocks)
        visualize_transactions(transactions, chain='ethereum')
        plot_fee_trends(fee_info)

    elif args.chain == 'bitcoin':
        print(f"🔗 Fetching {args.blocks} Bitcoin blocks (via Blockchair)...")
        transactions, fee_info = fetch_bitcoin_blocks(args.blocks)
        visualize_transactions(transactions, chain='bitcoin')
        plot_fee_trends(fee_info)

if __name__ == "__main__":
    main()
