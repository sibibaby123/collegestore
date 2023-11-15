from .models import Department,Purpose


def menu_links(request):
    links = Department.objects.all()
    return dict(links=links)



