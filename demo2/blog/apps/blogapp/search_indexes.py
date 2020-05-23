from haystack import indexes
# 指明搜索的模型为Article
from .models import Article

# 1 类名必须为 模型名Index
# 2 get_model 必须返回模型
class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    def get_model(self):
        return Article
    def index_queryset(self, using=None):
        return self.get_model().objects.all()
