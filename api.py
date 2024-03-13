import requests

def get_coin_price(coin_id, api_key):
    try:
        # Make request to CoinGecko API with API key
        response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd&api_key={api_key}')
        # Check if the coin data exists
        if coin_id not in response.json():
            return None

        # Return the live price of the coin
        return response.json()[coin_id]['usd']
    except Exception as e:
        print('Error fetching coin price:', e)
        return None

# Example usage
if __name__ == '__main__':
    coin_id = ['bitcoin', 'ethereum', 'ripple', 'pixels', 'dogecoin', 'eggdog']
    api_key = 'CG-KT2FeukAcS59Tx7SgdbHpEic'
    for coin in coin_id:
        price = get_coin_price(coin, api_key)
        if price is not None:
            print(f'The current price of {coin.capitalize()} is ${price}')
        else:
            print(f'Coin named {coin} not found.')
