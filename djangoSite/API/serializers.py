from rest_framework import serializers
from Blogs.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        # fields = ('alis','satis') // belirtilen kisimlari ceker.
        # fields = '__all__' // tum kisimlari ceker.
        fields = '__all__'