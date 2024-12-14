from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from order.models import Order


class OrderMixin:
    model = Order
    fields = '__all__'
    success_url = reverse_lazy('order:list_order')

class OrderListView(ListView):
    model = Order
    ordering = 'id'
    paginate_by = 10

class OrderDetailView(DetailView):
    model = Order
    template_name = "order/order_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Если заказы связаны с конкретным цехом, добавляем это
        context['workshop'] = self.object.workshops
        return context

class OrderCreateView(OrderMixin, CreateView):
    pass

class OrderUpdateView(OrderMixin, UpdateView):
    pass

class OrderDeleteView(OrderMixin, DeleteView):
    pass
