from django.shortcuts import render


from stock.models import StockItem
from .models import SearchQuery

def search_view(request):
	query = request.GET.get('q', None)
	user = None
	if request.user.is_authenticated:
		user = request.user
	context = {"query": query}
	if query is not None:
		SearchQuery.objects.create(user=user, query=query)
		stock_list = StockItem.objects.all().search(query=query)
		context['stock_list'] = stock_list
	return render(request, 'searches/view.html', context)


