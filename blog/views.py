from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Blog
from .serializers import BlogSerializer


class BlogList(APIView):
    def get(self, request, format=None):
        blogs = Blog.objects.all()

        serializer = BlogSerializer(blogs, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = BlogSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )


class BlogDetail(APIView):
    def get_object(self, pk):
        try:
            return Blog.objects.get(id=pk)
        except Blog.DoesNotExist:
            return Response(
                {"errors": "blog does not exist!"}, status=status.HTTP_404_NOT_FOUND
            )

    def get(self, request, pk, format=None):
        serializer = BlogSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        data = request.data
        serializer = BlogSerializer(instance=self.get_object(pk), data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                {"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, pk, format=None):
        blog = self.get_object(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
