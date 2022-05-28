import qrcode
from PIL import Image
from PIL.Image import Resampling
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import ImageColorMask
from qrcode.image.styles.moduledrawers import (
    CircleModuleDrawer, RoundedModuleDrawer
)
import matplotlib.pyplot as plt


def show_qr(image):
    plt.figure(figsize=(5, 5))
    plt.imshow(image)
    plt.axis('off')
    plt.show()


logo = Image.open("github.png")

base_width = 100
w_percent = (base_width / float(logo.size[0]))
hsize = int((float(logo.size[1] * float(w_percent))))
logo = logo.resize((base_width, hsize), Resampling.LANCZOS)

qr = qrcode.QRCode(
    version=10,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    mask_pattern=3,
)
qr.add_data('https://github.com/sezRR/qr_code_generator')
qr.make()

path = "images/background-14.jpg"

img = qr.make_image(
    color_mask=ImageColorMask(color_mask_path=path, back_color=(255, 255, 255)),
    image_factory=StyledPilImage,
    module_drawer=CircleModuleDrawer(),
    eye_drawer=RoundedModuleDrawer(radius_ratio=1),
).convert("RGB")

pos = ((img.size[0] - logo.size[0]) // 2,
       (img.size[1] - logo.size[1]) // 2)

img.paste(logo, pos)

img.save("output-2.png")
show_qr(img)
