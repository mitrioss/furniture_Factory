from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from workshop.models import Workshop, Worker


class WorkerMixin:
    model = Worker
    fields = '__all__'
    success_url = reverse_lazy('workshop:list_worker')

class WorkshopMixin:
    model = Workshop
    fields = ['name', 'supervisor', 'description']
    success_url = reverse_lazy('workshop:list_workshop')

class WorkshopListView(ListView):
    model = Workshop
    ordering = 'id'
    paginate_by = 10

class WorkshopDetailView(DetailView):
    model = Workshop

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем работников, связанных с текущим цехом
        context['workers'] = self.object.workers.all()  # Это обращение к related_name 'workers'
        context['orders'] = self.object.orders.all()
        return context

class WorkerListView(ListView):
    model = Worker
    ordering = 'id'
    paginate_by = 10

class WorkshopCreateView(WorkshopMixin, CreateView):
    pass

class WorkshopUpdateView(WorkshopMixin, UpdateView):
    pass

class WorkshopDeleteView(WorkshopMixin, DeleteView):
    pass

class WorkerCreateView(WorkerMixin, CreateView):
    pass

class WorkerUpdateView(WorkerMixin, UpdateView):
    pass

class WorkerDeleteView(WorkerMixin, DeleteView):
    pass