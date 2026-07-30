import os 
import qrcode
from datetime import datetime

OUTPUT_FOLDER = "output"

def create_output_folder():
    """Create output folder if it doesn't exist"""
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
def generate_qr(data, filename =None):
    """ Generate a QR code from text or URL.

    Args:
        data (str): Text or URL to encode.
        filename (str): Optional output filename.

    Returns:
        str: Path to the saved QR code."""

    create_output_folder()

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"qr_{timestamp}.png"

    if not filename.lower().endswith(".png"):
        filename += ".png"

    filepath = os.path.join(OUTPUT_FOLDER, filename)

    img.save(filepath)

    return filepath