from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post



# class Home(ListView):
#     template_name = 'blog/home.html'
#     model = Post
#     ordering = ['-date']
#     context_object_name = 'posts'

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         data = queryset[:3]
#         return data


def home(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blog/home.html', {
        'posts': latest_posts,
    })


# class AllPosts(View):
#     template_name = "blog/all-posts.html"
#     model = Post
#     ordering = ['-date']
#     context_object_name = 'all_posts'


def allPosts(request):
    all_posts = Post.objects.all().order_by('-date')
    return render(request, 'blog/all-posts.html', {
        'all_posts': all_posts,
    })


# class SinglePost(View):
#     def get(self, request, slug):
#         post = Post.objects.get(slug=slug)
#         context = {
#             'post': post,
            
#         }
#         return render(request, "blog/post-detail.html", context)


def singlePost(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post-detail.html', {
        'post': identified_post,
        'post_tags': identified_post.tags.all()
    })



def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        data = {
            'name': name,
            'email': email,
            'message': message
        }
        message = """
        ***Contact Form From Site***
        ───────▄████▄─────
        ──────███▄█▀───────
        ─────▐████─────────
        ──────█████▄───────
        ───────▀████▀─────

        Name: {}

        Email: {}

        Message: {}
        """.format(data['name'], data['email'], data['message'])
        send_mail(data['name'], message, '', ['serg2033@gmail.com'])
        return HttpResponseRedirect(reverse("thank_you"))

    return render(request, 'blog/contact.html')


def thank_you(request):
    context = {}
    return render(request, "blog/thank_you.html", context)