from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
# from django.utils.http import urlquote  # REMOVE this line
from .serializers import ImageUploadSerializer
from .utils import remove_background_bytes
from PIL import Image
import io

class RemoveBackgroundView(APIView):
    def post(self, request):
        serializer = ImageUploadSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        uploaded_image = serializer.validated_data['image']
        img_bytes = uploaded_image.read()

        try:
            Image.open(io.BytesIO(img_bytes)).verify()
        except Exception:
            return Response({"error": "Invalid image file."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Your remove_background_bytes should return PNG bytes with transparency
            result_bytes = remove_background_bytes(img_bytes)
        except Exception as e:
            return Response({"error": f"Background removal failed: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Force download with filename having .png extension
        filename = uploaded_image.name.rsplit('.', 1)[0] + '.png'
        response = HttpResponse(result_bytes, content_type="image/png")
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response
