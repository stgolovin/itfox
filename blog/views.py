from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, JsonResponse


from .models import News, Comment
from .serializers import NewsSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    
    def get_permissions(self):
        if self.action in ["create"]:
            return [IsAuthenticated()]
        if self.action in ["update", "partial_update", 'destroy']:
            return [IsOwnerOrReadOnly()]
        return []
    

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ["create"]:
            return [IsAuthenticated()]
        if self.action in ["update", "partial_update", 'destroy']:
            return [IsOwnerOrReadOnly()]
        return []


class LikeViewSet(ViewSet):
   
    def create(self, request):
        user = request.user
        if user.is_authenticated: 
            news_id = request.data["news"]
            news = News.objects.get(id=news_id)
            news.likes.add(user)
        else:
            return HttpResponse('Status_code: 403', content_type='text/plain')
        
        return JsonResponse({})

    def destroy(self, request, pk):
        user = request.user
        if user.is_authenticated:
            news_id = pk
            news = News.objects.get(id=news_id)
            news.likes.remove(user)
        else:
            return HttpResponse('Status_code: 403', content_type='text/plain')

        return JsonResponse({})
