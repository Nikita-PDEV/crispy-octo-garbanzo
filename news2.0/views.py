from django.views.generic import ListView, DetailView  
from .models import Post  

class NewsListView(ListView):  
    model = Post  
    template_name = 'news_list.html'  # Шаблон для списка новостей  
    context_object_name = 'news_list'  

    def get_queryset(self):  
        return Post.objects.filter(post_type=Post.NEWS).order_by('-created_at')  

class NewsDetailView(DetailView):  
    model = Post  
    template_name = 'news_detail.html'  # Шаблон для детального просмотра новости  
    context_object_name = 'news_detail'  

    def get_context_data(self, **kwargs):  
        context = super().get_context_data(**kwargs)  
        context['formatted_date'] = self.object.created_at.strftime('%d.%m.%Y')  
        return context