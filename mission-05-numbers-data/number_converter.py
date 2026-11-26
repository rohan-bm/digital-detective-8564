"""Simple decimal-to-binary and decimal-to-hexadecimal converter."""


def convert_decimal() -> None:
    """Prompt the user for a decimal integer and print its binary and hex forms."""
    raw_value = input("Enter a decimal integer: ").strip()
    try:
        decimal_number = int(raw_value)
    except ValueError:
        print("Invalid input: please enter a whole decimal number (e.g., 13).")
        return

    binary_value = bin(decimal_number)
    hex_value = hex(decimal_number)

    print(f"Decimal: {decimal_number}")
    print(f"Binary: {binary_value} (without prefix: {binary_value.replace('0b', '')})")
    print(f"Hexadecimal: {hex_value} (without prefix: {hex_value.replace('0x', '').upper()})")


if __name__ == "__main__":
    convert_decimal()
