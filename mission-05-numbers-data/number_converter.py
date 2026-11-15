"""
Digital Detective - Mission 5
Number Converter Program

This program asks the user to input a positive decimal integer,
then converts and displays it in binary (base 2) and hexadecimal (base 16).
"""

def main():
    print("=" * 40)
    print("    DIGITAL DETECTIVE NUMBER CONVERTER   ")
    print("=" * 40)
    
    user_input = input("Enter a positive decimal number: ").strip()
    
    try:
        # Convert user input string into an integer
        decimal_val = int(user_input)
        
        if decimal_val < 0:
            print("Please enter a positive integer.")
            return

        # Built-in conversions
        binary_val = bin(decimal_val)          # e.g. '0b1010'
        hex_val = hex(decimal_val)             # e.g. '0xa'
        
        # Formatted output showing both raw prefixed and uppercase representation
        print("\n--- Conversion Results ---")
        print(f"Decimal (Base 10):     {decimal_val}")
        print(f"Binary (Base 2):       {binary_val} (Raw: {binary_val[2:]})")
        print(f"Hexadecimal (Base 16): {hex_val.upper()} (Raw: {hex_val[2:].upper()})")
        print("=" * 40)
        
    except ValueError:
        print("Invalid input! Please enter a valid decimal integer.")

if __name__ == "__main__":
    main()
