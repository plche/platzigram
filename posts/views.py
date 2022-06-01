"""Posts views."""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime


posts = [
    {
        'name': 'Mont Blac',
        'user': 'Yésica Cortés',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036',
    },
    {
        'name': 'Via Láctea',
        'user': 'C. Vander',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=903',
    },
    {
        'name': 'Nuevo auditorio',
        'user': 'Thespianartist',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1076',
    }
]


def list_posts(request):
    """List existing posts."""
    # posts = [1, 2, 4]
    # return HttpResponse(str(posts))
    content = []
    for post in posts:
        content.append("""
                <p><strong>{name}</strong></p>
                <p><small>{user} - <i>{timestamp}</i></small></p>
                <figure><img src="{picture}"/></figure>
            """.format(**post))
        # **post es equivalente a name=post['name']...etc, es decir, desempaquetamos el dict post
    return HttpResponse('<br>'.join(content))
