# IT Asset Management System

Created by Jamie Pascual

A command-line IT asset inventory application built with Python. The application allows an IT support team to track company equipment, assign assets to users, update asset status, and save inventory records between program runs.

## Features

- Add new IT assets with automatically generated asset tags
- View all assets in the inventory
- Search assets by asset tag, serial number, assigned user, status, type, or location
- Update asset location, status, warranty expiration, and model
- Assign assets to users
- Retire assets while preserving the asset record
- View asset statistics by status
- Save asset records to a JSON file
- Load saved asset records when the program starts
- Input validation for required fields, statuses, and menu selections

## Technologies Used

- Python
- Dictionaries
- Functions
- Loops
- Conditional Statements
- JSON File Storage
- Input Validation
- Error Handling

## How It Works

The application provides a menu-driven interface with the following options:

1. Add Asset
2. View All Assets
3. Search Asset
4. Update Asset
5. Assign Asset
6. Retire Asset
7. View Asset Statistics
8. Exit

## How to Run

1. Install Python 3.

2. Navigate to the project directory:

```bash
cd ITAssetManagementSystem
```

3. Run the application:

```bash
python main.py
```

## Asset Information

Each asset record includes:

- Asset Tag
- Type
- Manufacturer
- Model
- Serial Number
- Location
- Assigned User
- Status
- Purchase Date
- Warranty Expiration

## Asset Statuses

The application uses the following asset statuses:

- Available
- Assigned
- Repair
- Retired
- Lost

## Data Storage

Asset records are saved in:

```text
assets.json
```

This file is created automatically after adding or updating an asset. The file keeps the inventory available even after the program closes.

## Portfolio Value

This project demonstrates how Python can be used to solve a real IT operations problem. It builds on help desk ticket tracking by adding inventory management, persistent storage, searching, updating, and reporting.

## Future Improvements

Potential future improvements include:

- CSV export
- SQLite database integration
- Asset checkout history
- Warranty expiration alerts
- Barcode or QR code lookup
- User authentication
- Graphical user interface
- Web-based version

## Author

Jamie Pascual

IT / Systems & Support Portfolio
