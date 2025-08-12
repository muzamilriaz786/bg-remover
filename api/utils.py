from rembg import remove
from PIL import Image
import io

def remove_background_bytes(image_bytes: bytes) -> bytes:
    """
    Takes raw image bytes, removes the background, returns PNG bytes.
    """
    return remove(image_bytes)
