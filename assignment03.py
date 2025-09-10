# Function to calculate discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # Apply discount only if 20% or higher
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price  # Return original price if discount is less than 20%

# Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price using the function
final_price = calculate_discount(original_price, discount_percent)

# Display the result
if discount_percent >= 20:
    print(f"Discount applied! The final price is: {final_price}")
else:
    print(f"No discount applied. The original price is: {original_price}")
