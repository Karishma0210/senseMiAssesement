from django.shortcuts import render
from django.views import View
from .models import Product
from django.conf import settings
# import os
# import json
# Create your views here.


class Home(View):
    def get(self, request):
        products = Product.objects.all()
        media_url = settings.MEDIA_URL
        context = {
            'products': products,
            'media_url': media_url
        }
        return render(request, "index.html", context=context)

    # def post(self, request):

    #     context = {

    #     }
    #     return render(request, 'index.html', context=context)


# def sign_s3(request):
#     S3_BUCKET = os.environ.get('S3_BUCKET')

#     file_name = request.GET.get('file_name')
#     file_type = request.GET.get('file_type')

#     s3 = boto3.client('s3')

#     presigned_post = s3.generate_presigned_post(
#         Bucket=S3_BUCKET,
#         Key=file_name,
#         Fields={"acl": "public-read", "Content-Type": file_type},
#         Conditions=[
#             {"acl": "public-read"},
#             {"Content-Type": file_type}
#         ],
#         ExpiresIn=3600
#     )

#     return json.dumps({
#         'data': presigned_post,
#         'url': 'https://%s.s3.amazonaws.com/%s' % (S3_BUCKET, file_name)
#     })
