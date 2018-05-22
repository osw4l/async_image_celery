from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Favorite, Ticket
from weasyprint import HTML, CSS
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.conf import settings


class FavoriteListView(ListView):
	model = Ticket
	template_name = 'favs.html'


class TicketDetailView(DetailView):
	template_name = 'detail.html'
	model = Ticket

	def post(self, request, *args, **kwargs):
		html_string = render_to_string('file.html', {
			'object_list': Ticket.objects.all()
		})

		html = HTML(string=html_string)

		html.write_pdf(target='/tmp/file.pdf')
		fs = FileSystemStorage('/tmp')
		with fs.open('file.pdf') as pdf:
			response = HttpResponse(pdf, content_type='application/pdf')
			response['Content-Disposition'] = 'attachment; filename="file.pdf"'
			return response
		return response

