# thsis is which i already have in the blog. It shows all the posts.
def post_list(request):
    posts = Post.objects.all()
    data = {}
    data['object_list'] = posts
    return render(request, template_name='Post/post_list.html', data)

#this is to create new post. if the post is created, post is added to the post_list else page gets returned to previous page(post_list), without post being added.
def create_post(request):
    form = PostsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Post:post_list')
    return render(request, template_name='Post/post_form.html', {'form': form})


#this is to update the already written post, if not updated gets returned to previous page.
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostsForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('Post:post_list')
    return render(request, template_name='Post/post_form.html', {'form':form})


#TO delete a post. after deleting returns to post_list.html page
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method=='POST':
        post.delete()
        return redirect('Post:post_list')
    return render(request, template_name='Post/post_delete.html', {'object': post})    