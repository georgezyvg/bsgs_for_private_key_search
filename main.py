from src import KeyFinder


if __name__ == "__main__":
    target_public_key = "02e0a8b039282faf6fe0fd769cfbc4b6b4cf8758ba68220eac420e32b91ddfa673"
    target_address = "1NBC8uXJy1GiJ6drkiZa1WuKn51ps7EPTv"
    start_range_hex = "800000000000000000000000000000000000000"
    end_range_hex = "fffffffffffffffffffffffffffffffffffffff"

    KeyFinder().solve_puzzle(
        target_public_key, target_address, start_range_hex, end_range_hex
    )
