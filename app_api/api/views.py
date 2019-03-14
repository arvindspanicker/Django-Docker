import logging
from datetime import datetime

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models.signals import post_save
from django.dispatch import receiver


from api.models import TestModel
from api.forms import TestForm


logger = logging.getLogger(__name__)

def my_view(request,tenant_name):
	if request.method == "POST":
		form = TestForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
		return HttpResponseRedirect(request.path_info)
	else:
		form = TestForm()
	all_data = TestModel.objects.all()
	context = {'data':{},'form': form}
	for item in all_data:
		try:
			context['data'].append([str(item.id),item.title, str(item.updated_at)])
		except:
			context['data'] = [[str(item.id) ,item.title, str(item.updated_at)]]

	logger.info(context)
	template = loader.get_template('test.html')	
	return HttpResponse(template.render(context,request))

# Signals
# Simply to test whether its saving in the correct database or not
@receiver(post_save, sender=TestModel)
def save_updated_at(sender, instance,created, **kwargs):
	if created:
		current_time = datetime.now()
		instance.updated_at=current_time
		instance.save()