# Create your views here.
from django.views import generic
from blogsite.models import BlogPost, Comment
from blogsite.forms import newBlogForm, newCommentForm
from django.shortcuts import get_object_or_404, render_to_response, HttpResponseRedirect

import csv
from django.http import HttpResponse

class Archive(generic.ListView):
    model = BlogPost
    context_object_name = 'posts'
    template_name = 'archive.html'

    def get_context_data(self, **kwargs):
        c = super(Archive, self).get_context_data(**kwargs)
        c['form'] = newCommentForm
        return c

def process_comment(request, post_id):
    form = newCommentForm(request.POST)
    if form.is_valid():
        id = post_id
        tname = form.cleaned_data['name']
        tbody = form.cleaned_data['body']
        c = Comment(name=tname, body = tbody, post_id=id)
        c.save()
        return HttpResponseRedirect(".",{'inv': 'invalid'})#, {"posts" : BlogPost.objects.all(),})
                                              #"form" : form })
    else:
        return HttpResponseRedirect(".",{'inv': 'invalid'})#, {"posts" : BlogPost.objects.all(),
                                             # "form" : form, "inv" : "form invalid" })

class Post(generic.DetailView):
    template_name = "archive.html"
    context_object_name = 'post'
    model = BlogPost
    

def process_form(request):
    if not request.POST:
        post = get_object_or_404(BlogPost)
        form = newBlogForm(post)
        if form.save():
            return render_to_response('posted.html', {'form': form})

#trying to use csv
def to_excel(request):
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=guys.csv'

    writer = csv.writer(response)
    writer.writerow(['date','body'])
    for (post) in BlogPost.objects.all():
        writer.writerow([post.timestamp, post.body])
    return response