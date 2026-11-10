from database import create_database,display_customer
create_database()
customers=display_customer()

print("\n===ERP DATABASE - CUSTOMERS===")
print(f"{'NO':<10}{'NAME':<20}{'EMAIL':<30}{'LOCATION':<15}")
print("-"*75)

for c in customers:
    print(f"{c[0]}:<10}{c[1]:<20}")

