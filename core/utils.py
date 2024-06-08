# core/utils.py
import qrcode
from io import BytesIO
from django.core.files import File
from django.conf import settings

def generate_qr_code(package_id):
    # Generate the URL that the QR code will point to
    url = f"{settings.SITE_URL}/scan/{package_id}/"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    buffer = BytesIO()
    img.save(buffer)
    filename = f'qr_code_{package_id}.png'
    filebuffer = File(buffer, name=filename)
    
    return filebuffer
