# 🔳 QR Code Generator (Python)

A simple and efficient **QR Code Generator** built with Python that allows users to generate QR codes from any text, website URL, email address, phone number, or other supported data. The generated QR codes are automatically saved as PNG images for easy sharing and printing.

This project is beginner-friendly and demonstrates the use of Python libraries for image generation, file handling, and modular programming. It is a great project for learning Python while building a practical utility that can be used in everyday situations.

## ✨ Features

* Generate QR codes from text
* Generate QR codes from website URLs
* Save QR codes as PNG images
* Automatic output folder creation
* Custom filename support
* Automatic timestamp-based filenames
* Simple command-line interface
* Clean and modular project structure
* Easy to extend with new features

## 📂 Project Structure

```text
QR-Code-Generator/
│
├── main.py
├── qr_generator.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── output/
    └── Generated QR Codes
```

## 🛠️ Technologies Used

* Python 3.x
* qrcode
* Pillow (PIL)

## 📦 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/QR-Code-Generator.git
   ```

2. Move into the project directory:

   ```bash
   cd QR-Code-Generator
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Usage

Run the application:

```bash
python main.py
```

Choose **Generate QR Code**, enter your text or URL, and the QR code will be saved in the **output/** folder.

## 📸 Example

**Input:**

```
https://github.com/yourusername
```

**Output:**

```
output/github.png
```

## 🚀 Future Improvements

* Tkinter GUI
* Custom QR colors
* Logo inside QR code
* Batch QR code generation
* QR code scanner
* QR code history
* PDF export
* High-resolution image export

## 🎯 Learning Outcomes

This project helps you understand:

* Modular Python programming
* File and folder handling
* Working with external libraries
* Image generation
* Error handling
* Command-line applications

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome. Feel free to fork the repository and submit a pull request.

## 📄 License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, consider giving it a star on GitHub!
