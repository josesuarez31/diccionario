from .models import Word
from django.views import generic



class IndexView(generic.ListView):
    template_name = "lsv/index.html"
    context_object_name = "latest_word_list"

    def get_queryset(self):
        """Return the last five published Word."""
        return Word.objects.all()


class DetailView(generic.DetailView):
    model = Word
    template_name = "lsv/detail.html"
