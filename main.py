import json
from pathlib import Path


# File used to save asset records between program runs.
DATA_FILE = Path(__file__).with_name("assets.json")

# Master dictionary used to store all IT assets.
assets = {}

# Counter used to generate unique asset tags.
asset_counter = 1000


def load_assets():
    global assets
    global asset_counter

    if not DATA_FILE.exists():
        return

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        assets = data.get("assets", {})
        asset_counter = data.get("asset_counter", 1000)

    except json.JSONDecodeError:
        print("\nWarning: assets.json could not be read. Starting with an empty inventory.")
        assets = {}
        asset_counter = 1000


def save_assets():
    data = {
        "asset_counter": asset_counter,
        "assets": assets
    }

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


# ==============================
# Main menu display function
# ==============================

def display_menu():
    print("\n=================================")
    print("     IT ASSET MANAGEMENT SYSTEM")
    print("=================================")
    print("1. Add Asset")
    print("2. View All Assets")
    print("3. Search Asset")
    print("4. Update Asset")
    print("5. Assign Asset")
    print("6. Retire Asset")
    print("7. View Asset Statistics")
    print("8. Exit")


def get_valid_status(prompt):
    valid_statuses = ["Available", "Assigned", "Repair", "Retired", "Lost"]

    while True:
        status = input(prompt).title()

        if status in valid_statuses:
            return status

        print("Invalid status. Please enter Available, Assigned, Repair, Retired, or Lost.")


def get_required_input(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be blank.")


def display_asset(asset_tag, asset):
    print(f"\nAsset Tag: {asset_tag}")
    print(f"Type: {asset['type']}")
    print(f"Manufacturer: {asset['manufacturer']}")
    print(f"Model: {asset['model']}")
    print(f"Serial Number: {asset['serial_number']}")
    print(f"Location: {asset['location']}")
    print(f"Assigned User: {asset['assigned_user']}")
    print(f"Status: {asset['status']}")
    print(f"Purchase Date: {asset['purchase_date']}")
    print(f"Warranty Expiration: {asset['warranty_expiration']}")
    print("-" * 40)


# ==============================
# Menu option 1 function
# ==============================

def add_asset():
    global asset_counter

    asset_counter += 1
    asset_tag = f"AST{asset_counter}"

    print("\n--- Add New Asset ---")

    asset_type = get_required_input("Enter asset type (Laptop/Desktop/Monitor/Printer/Phone): ").title()
    manufacturer = get_required_input("Enter manufacturer: ")
    model = get_required_input("Enter model: ")
    serial_number = get_required_input("Enter serial number: ").upper()
    location = get_required_input("Enter location: ")
    purchase_date = get_required_input("Enter purchase date (YYYY-MM-DD): ")
    warranty_expiration = get_required_input("Enter warranty expiration (YYYY-MM-DD): ")
    status = get_valid_status("Enter status (Available/Assigned/Repair/Retired/Lost): ")

    assigned_user = "Unassigned"

    if status == "Assigned":
        assigned_user = get_required_input("Enter assigned user: ")

    assets[asset_tag] = {
        "type": asset_type,
        "manufacturer": manufacturer,
        "model": model,
        "serial_number": serial_number,
        "location": location,
        "assigned_user": assigned_user,
        "status": status,
        "purchase_date": purchase_date,
        "warranty_expiration": warranty_expiration
    }

    save_assets()
    print(f"\nAsset added successfully with Asset Tag: {asset_tag}")


# ==============================
# Menu option 2 function
# ==============================

def view_assets():
    if not assets:
        print("\nNo assets found.")
        return

    print("\n--- All IT Assets ---")

    for asset_tag, asset in assets.items():
        display_asset(asset_tag, asset)


# ==============================
# Menu option 3 function
# ==============================

def search_asset():
    if not assets:
        print("\nNo assets found.")
        return

    search_term = input("\nEnter asset tag, serial number, user, or status to search: ").strip().lower()
    matches_found = False

    print("\n--- Search Results ---")

    for asset_tag, asset in assets.items():
        searchable_values = [
            asset_tag,
            asset["serial_number"],
            asset["assigned_user"],
            asset["status"],
            asset["type"],
            asset["location"]
        ]

        for value in searchable_values:
            if search_term in value.lower():
                display_asset(asset_tag, asset)
                matches_found = True
                break

    if not matches_found:
        print("\nNo matching assets found.")


# ==============================
# Menu option 4 function
# ==============================

def update_asset():
    asset_tag = input("\nEnter Asset Tag to update: ").upper()

    if asset_tag not in assets:
        print("\nAsset not found.")
        return

    asset = assets[asset_tag]

    print("\n--- Update Asset ---")
    print("1. Update Location")
    print("2. Update Status")
    print("3. Update Warranty Expiration")
    print("4. Update Model")

    choice = input("\nSelect an option (1-4): ")

    if choice == "1":
        asset["location"] = get_required_input("Enter new location: ")

    elif choice == "2":
        asset["status"] = get_valid_status("Enter new status (Available/Assigned/Repair/Retired/Lost): ")

        if asset["status"] == "Assigned":
            asset["assigned_user"] = get_required_input("Enter assigned user: ")
        elif asset["status"] == "Available":
            asset["assigned_user"] = "Unassigned"

    elif choice == "3":
        asset["warranty_expiration"] = get_required_input("Enter new warranty expiration (YYYY-MM-DD): ")

    elif choice == "4":
        asset["model"] = get_required_input("Enter new model: ")

    else:
        print("\nInvalid selection.")
        return

    save_assets()
    print(f"\nAsset {asset_tag} updated successfully.")


# ==============================
# Menu option 5 function
# ==============================

def assign_asset():
    asset_tag = input("\nEnter Asset Tag to assign: ").upper()

    if asset_tag not in assets:
        print("\nAsset not found.")
        return

    user = get_required_input("Enter assigned user: ")
    location = get_required_input("Enter user location or department: ")

    assets[asset_tag]["assigned_user"] = user
    assets[asset_tag]["location"] = location
    assets[asset_tag]["status"] = "Assigned"

    save_assets()
    print(f"\nAsset {asset_tag} assigned to {user}.")


# ==============================
# Menu option 6 function
# ==============================

def retire_asset():
    asset_tag = input("\nEnter Asset Tag to retire: ").upper()

    if asset_tag not in assets:
        print("\nAsset not found.")
        return

    assets[asset_tag]["status"] = "Retired"
    assets[asset_tag]["assigned_user"] = "Unassigned"

    save_assets()
    print(f"\nAsset {asset_tag} has been retired.")


# ==============================
# Menu option 7 function
# ==============================

def asset_statistics():
    total_assets = len(assets)
    available_assets = 0
    assigned_assets = 0
    repair_assets = 0
    retired_assets = 0
    lost_assets = 0

    for asset in assets.values():
        if asset["status"] == "Available":
            available_assets += 1
        elif asset["status"] == "Assigned":
            assigned_assets += 1
        elif asset["status"] == "Repair":
            repair_assets += 1
        elif asset["status"] == "Retired":
            retired_assets += 1
        elif asset["status"] == "Lost":
            lost_assets += 1

    print("\n--- Asset Statistics ---")
    print(f"Total Assets: {total_assets}")
    print(f"Available Assets: {available_assets}")
    print(f"Assigned Assets: {assigned_assets}")
    print(f"Repair Assets: {repair_assets}")
    print(f"Retired Assets: {retired_assets}")
    print(f"Lost Assets: {lost_assets}")


# ==============================
# Main section of the program that runs the menu loop
# ==============================

def main():
    load_assets()

    while True:
        display_menu()
        choice = input("\nSelect an option (1-8): ")

        if choice == "1":
            add_asset()

        elif choice == "2":
            view_assets()

        elif choice == "3":
            search_asset()

        elif choice == "4":
            update_asset()

        elif choice == "5":
            assign_asset()

        elif choice == "6":
            retire_asset()

        elif choice == "7":
            asset_statistics()

        elif choice == "8":
            print("\nThank you for using the IT Asset Management System.")
            break

        else:
            print("\nInvalid selection. Please choose an option from 1-8.")


if __name__ == "__main__":
    main()
