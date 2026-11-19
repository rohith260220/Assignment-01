# Q3: Online Shopping Discount Eligibility

# 1. Accept the order amount and membership status
order_amount = float(input("Enter the order amount (in Rs.): "))
# 2. strip() removes extra spaces and lower() ignores case ("Yes", "YES", "yes")
is_member = input("Are you a member? (yes/no): ").strip().lower()

# 3. Validate the amount: below 0 or above 1,00,000 is invalid
is_invalid_amount = order_amount < 0 or order_amount > 100000

# 4. Decide the discount percentage
if is_invalid_amount:
    print("Invalid order amount. It must be between Rs.0 and Rs.1,00,000.")
else:
    if order_amount >= 5000:
        discount_percent = 15
        status = "Eligible: 15% discount (order of Rs.5,000 or more)"
    elif is_member == "yes" and 2000 <= order_amount < 5000:
        discount_percent = 10
        status = "Eligible: 10% member discount"
    else:
        discount_percent = 0
        status = "Not eligible for any discount"

    # 5. Calculate and display the results
    discount_amount = order_amount * discount_percent / 100
    final_amount = order_amount - discount_amount

    print("Original amount: Rs.", order_amount)
    print("Discount amount: Rs.", discount_amount)
    print("Final payable amount: Rs.", final_amount)
    print("Eligibility status:", status)
