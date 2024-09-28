import logging

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone

from blog.forms import CommentForm
from blog.models import Post

logger = logging.getLogger(__name__)


def index(request):
    posts = (
        Post.objects.filter(published_at__lte=timezone.now())
        .select_related("author")
        .order_by("-published_at")
    )

    return render(request, "blog/index.html", {"posts": posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.content = post.content.replace(
        "static/", request.build_absolute_uri("/static/")
    )
    if request.user.is_active and request.user != post.author:
        if request.method == "POST":
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.content_object = post
                comment.creator = request.user
                comment.save()
                logger.info(
                    "Created comment on Post %d for user %s", post.pk, request.user
                )
                return redirect(request.path_info)

        else:
            comment_form = CommentForm()
    else:
        comment_form = None

    return render(
        request, "blog/post-detail.html", {"post": post, "comment_form": comment_form}
    )


def post_table(request):
    return render(
        request, "blog/post-table.html", {"post_list_url": reverse("post-list")}
    )
