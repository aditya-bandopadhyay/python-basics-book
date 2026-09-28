"""
ch05_lists.py

Demonstrates list operations: append, remove, iteration and a simple
helper that returns unique items while preserving order.
"""

def unique_items_preserve_order(input_list: list) -> list:
    """Return a list of unique items preserving their original order."""
    seen_items = set()
    unique_list_result = []
    for item in input_list:
        if item not in seen_items:
            unique_list_result.append(item)
            seen_items.add(item)
    return unique_list_result


if __name__ == "__main__":
    sample_list = [1, 2, 3, 2, 1, 4]
    print("Original list:", sample_list)
    unique_res = unique_items_preserve_order(sample_list)
    print("Unique preserving order:", unique_res)
