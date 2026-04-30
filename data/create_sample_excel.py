"""サンプル Excel ファイル (sales_data.xlsx) を生成するスクリプト"""
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "SalesData"

headers = ["OrderID", "Product", "Category", "Quantity", "UnitPrice", "OrderDate"]
ws.append(headers)

data = [
    [1001, "Laptop",    "Electronics", 2,  120000, "2025-01-15"],
    [1002, "Mouse",     "Electronics", 10,   3500, "2025-01-16"],
    [1003, "Desk",      "Furniture",   1,   45000, "2025-02-01"],
    [1004, "Monitor",   "Electronics", 3,   35000, "2025-02-10"],
    [1005, "Chair",     "Furniture",   5,   28000, "2025-03-05"],
    [1006, "Keyboard",  "Electronics", 8,    8000, "2025-03-12"],
    [1007, "Bookshelf", "Furniture",   2,   18000, "2025-04-01"],
    [1008, "Webcam",    "Electronics", 4,   12000, "2025-04-15"],
]

for row in data:
    ws.append(row)

wb.save("sales_data.xlsx")
print("✅ sales_data.xlsx を作成しました")
