# Biến lưu trữ danh sách sản phẩm
products = []

def add_product():
    print("\n--- NHẬP HÀNG MỚI ---")
    name = input("Nhập tên sản phẩm: ")
    
    try:
        price = int(input("Nhập giá bán (VNĐ): "))
        quantity = int(input("Nhập số lượng tồn kho: "))

        if price < 0 or quantity < 0:
             print("⚠️ Giá bán và Số lượng không được là số âm. Vui lòng thử lại.")
             return
        
        products.append({
            'name': name,
            'price': price,
            'qty': quantity
        })
        print(f" Đã nhập hàng thành công: {name} (SL: {quantity})")

    except ValueError:
        print(" Lỗi: Giá bán và Số lượng phải là các giá trị số hợp lệ.")

def view_inventory():
    print("\n--- DANH SÁCH TỒN KHO ---")
    if not products:
        print("📦 Kho hàng trống. Vui lòng nhập hàng (Chọn chức năng 1).")
        return

    print(f"{'Tên Sản Phẩm':<20} | {'Giá Bán':>10} | {'Số Lượng':>10}")
    print("-" * 45)

    for product in products:
        price_formatted = f"{product['price']:,}"
        print(f"{product['name']:<20} | {price_formatted:>10} | {product['qty']:>10}")

def check_low_stock():
    pass

def main():
    while True:
        print("\n--- QUẢN LÝ KHO HÀNG ---")
        print("1. Nhập hàng mới")
        print("2. Xem tồn kho")
        print("3. Cảnh báo hết hàng")
        print("4. Thoát")
        
        choice = input("Chọn chức năng: ")
        
        if choice == '1':
            add_product()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            check_low_stock()
        elif choice == '4':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()
