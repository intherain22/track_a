import requests

block_num = 2817653

def get_block_hash(block_num):
        url = f"https://api.blockcypher.com/v1/btc/test3/blocks/{block_num}"
        response = requests.get(url)
        response.raise_for_status()
        block_hash = response.json()["hash"]
        return block_hash

block_hash = get_block_hash(block_num)
print(f"The blockhash of {block_num}: {block_hash}")
