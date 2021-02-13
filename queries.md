from django.contrib.auth.models import User

user1 = User.objects.get(username='admin')  

post = Post(title='Testare 2', category=cat, excerpt='la naiba sa va ia pe toti', image='default.jpg', slug='testere-2',author=admin, content='content in shell', status='published')

post.save()

Post.objects.all().values()

Post.objects.get(id=1)

Post.objects.get(id=1, title='Title')

Post.objects.filter(publish__year=2021)

Post.objects.filter(publish__year=2021).exclude(id=1)

Post.objects.order_by('publish')

Post.objects.order_by('-publish')

post.delete()
