# marketCheck
# Warframe Market API Python Client

This is a Python client for the Warframe Market API. It allows you to search for and retrieve listings for items being sold on the Warframe Market platform, and it can notify you when a new listing appears that matches your search criteria.

## Setup

- Clone this repository to your local machine.
- Install the required packages using `pip install -r requirements.txt`.
- Create a `token.json` file with your API key, as described in the API documentation.
- Run `python main.py` to start the program.

## Usage

The program prompts the user to enter a search query for an item, along with a price range. Then, it retrieves listings that match the search query and filters them based on the price range.

The search query should be in the format `item_name price_range`, where `item_name` is the name of the item you're searching for and `price_range` is the maximum price you're willing to pay. For example, if you want to search for an Ivara Prime Set for 300 plat, you would enter `Ivara Prime Set 300`.

If no listings are found that match the search query and price range, the program prompts the user to search again or exit. If listings are found, the program displays them in a table sorted by price.

The program also allows the user to continuously refresh the listings to see if any new ones are created that match the search criteria. If a new listing is found that meets the search criteria, the program displays a notification with the details of the listing.

## File Structure

- `main.py`: The main file that runs the program and handles user input, display of results, and continuous checking for new listings.
- `api.py`: Functions for interacting with the Warframe Market API.
- `listing.py`: Defines functions to represent listings on the Warframe Market platform, including retrieving listings and searching for specific items.
- `database.py`: Handles queried input to pull attributes from listings for further query
- `utils.py`: Utility functions used throughout the program, such as functions for formatting output or parsing user input.

## Credits

This program was created by Seth Groves as a personal project. It uses the Warframe Market API, which is owned and operated by Digital Extremes.
