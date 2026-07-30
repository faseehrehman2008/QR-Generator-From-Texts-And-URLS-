from qr_generator import generate_qr

def print_header():
    print("=" * 45)
    print("        QR Code Generator")
    print("=" * 45)


def main():
    print_header()

    while True:
        print("\nMenu")
        print("1. Generate QR Code")
        print("2. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            data = input("\nEnter text or URL: ").strip()

            if not data:
                print("❌ Input cannot be empty.")
                continue

            filename = input(
                "Enter filename (leave blank for auto-generated): "
            ).strip()

            try:
                saved_path = generate_qr(data, filename if filename else None)

                print("\n✅ QR Code generated successfully!")
                print(f"📁 Saved at: {saved_path}")

            except Exception as e:
                print(f"\n❌ Error: {e}")

        elif choice == "2":
            print("\n👋 Thank you for using QR Code Generator.")
            break

        else:
            print("\n❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()