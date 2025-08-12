from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rembg import remove
from PIL import Image
import io
from django.http import HttpResponse

@api_view(['POST'])
def remove_background(request):
    if 'image' not in request.FILES:
        return Response({"error": "No image file provided."}, status=status.HTTP_400_BAD_REQUEST)

    image_file = request.FILES['image']

    try:
        # Read uploaded image file
        input_image = Image.open(image_file)

        # Convert image to RGBA (required by rembg)
        input_image = input_image.convert("RGBA")

        # Remove background using rembg
        output_image = remove(input_image)

        # Save output image to bytes buffer
        buffered = io.BytesIO()
        output_image.save(buffered, format="PNG")
        img_bytes = buffered.getvalue()

        # Return the image as a response with PNG content-type
        return HttpResponse(img_bytes, content_type="image/png")

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
