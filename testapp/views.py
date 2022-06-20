from errno import EADDRINUSE
from django.shortcuts import render
from testapp.models import Employee
from django.http import HttpResponse
from django.db.models import Q
from django.db.models import Avg,Sum,Min,Max,Count
# Create your views here.
def orm_view(request):
    # Django ORM
    """
    # retrieve data from database   
    emp=Employee.objects.all()
    <QuerySet [{'id': 1, 'eno': 1, 'ename': 'raj', 'esal': 8000.0, 'eaddr': 'pune'}, {'id': 2, 'eno': 2, 'ename': 'raju', 
    'esal': 890000.0, 'eaddr': 'mumbai'}, {'id': 3, 'eno': 80000, 'ename': 'Kedar', 'esal': 9000.0, 'eaddr': 'kolkata'}, {'id': 4, 'eno': 90, 'ename': 'sai', 'esal': 4000.0, 'eaddr': 'ooty'}]>
    
    # get only one record
    emp=Employee.objects.get(id=1)
    Employee object (1) <class 'testapp.models.Employee'>

    # how to filter records based on some condition
    emp=Employee.objects.filter(esal__gt=50000)
    <QuerySet [{'id': 2, 'eno': 2, 'ename': 'raju', 'esal': 890000.0, 'eaddr': 'mumbai'}]>

    emp=Employee.objects.filter(esal__gte=4000)
    <QuerySet [{'id': 1, 'eno': 1, 'ename': 'raj', 'esal': 8000.0, 'eaddr': 'pune'}, {'id': 2, 'eno': 2, 'ename': 'raju', 
    'esal': 890000.0, 'eaddr': 'mumbai'}, {'id': 3, 'eno': 80000, 'ename': 'Kedar', 'esal': 9000.0, 'eaddr': 'kolkata'}, {'id': 4, 'eno': 90, 'ename': 'sai', 'esal': 4000.0, 'eaddr': 'ooty'}]>
    
    emp=Employee.objects.filter(id__exact=4).values()
    <QuerySet [{'id': 4, 'eno': 90, 'ename': 'sai', 'esal': 4000.0, 'eaddr': 'ooty'}]>
    
    emp=Employee.objects.filter(id__lt=2).values()
    <QuerySet [{'id': 1, 'eno': 1, 'ename': 'raj', 'esal': 8000.0, 'eaddr': 'pune'}]>
    
    emp=Employee.objects.filter(id__lte=2).values()
    <QuerySet [{'id': 1, 'eno': 1, 'ename': 'raj', 'esal': 8000.0, 'eaddr': 'pune'}, {'id': 2, 'eno': 2, 'ename': 'raju', 
    'esal': 890000.0, 'eaddr': 'mumbai'}]>
  
    emp=Employee.objects.filter(ename__iexact='raj').values()
    <QuerySet [{'id': 1, 'eno': 1, 'ename': 'raj', 'esal': 8000.0, 'eaddr': 'pune'}]>
    
    emp=Employee.objects.filter(ename__contains='ra').values()
    <QuerySet [{'id': 1, 'eno': 1, 'ename': 'raj', 'esal': 8000.0, 'eaddr': 'pune'}, {'id': 2, 'eno': 2, 'ename': 'raju', 
    'esal': 890000.0, 'eaddr': 'mumbai'}]>

    emp=Employee.objects.filter(id__in=[1,3,4]).values()
    <QuerySet [{'id': 1, 'eno': 1, 'ename': 'raj', 'esal': 8000.0, 'eaddr': 'pune'}, {'id': 3, 'eno': 80000, 'ename': 'Kedar', 'esal': 9000.0, 'eaddr': 'kolkata'}, 
    {'id': 4, 'eno': 90, 'ename': 'sai', 'esal': 4000.0, 'eaddr': 'ooty'}]>
    
    emp=Employee.objects.filter(ename__startswith='raj').values()
    <QuerySet [{'id': 1, 'eno': 1, 'ename': 'raj', 'esal': 8000.0, 'eaddr': 'pune'}, {'id': 2, 'eno': 2, 'ename': 'raju', 'esal': 890000.0, 'eaddr': 'mumbai'}]>
    
    emp=Employee.objects.filter(ename__istartswith='raj').values()
    <QuerySet [{'id': 1, 'eno': 1, 'ename': 'raj', 'esal': 8000.0, 'eaddr': 'pune'}, {'id': 2, 'eno': 2, 'ename': 'raju', 'esal': 890000.0, 'eaddr': 'mumbai'}]>
   
    emp=Employee.objects.filter(ename__endswith='aj').values()
    <QuerySet [{'id': 1, 'eno': 1, 'ename': 'raj', 'esal': 8000.0, 'eaddr': 'pune'}]>

    emp=Employee.objects.filter(ename__iendswith='aj').values()
    <QuerySet [{'id': 1, 'eno': 1, 'ename': 'raj', 'esal': 8000.0, 'eaddr': 'pune'}]>
    
    emp=Employee.objects.filter(id__range=(1,3)).values()
    <QuerySet [{'id': 1, 'eno': 1, 'ename': 'raj', 'esal': 8000.0, 'eaddr': 'pune'}, {'id': 2, 'eno': 2, 'ename': 'raju', 
    'esal': 890000.0, 'eaddr': 'mumbai'}, {'id': 3, 'eno': 80000, 'ename': 'Kedar', 'esal': 9000.0, 'eaddr': 'kolkata'}]>
    
    # OR queries 
    emp=(Employee.objects.filter(ename__startswith='ra')|Employee.objects.filter(esal__gt=4000)).values()
    <QuerySet [{'id': 1, 'eno': 1, 'ename': 'raj', 'esal': 8000.0, 'eaddr': 'pune'}, {'id': 2, 'eno': 2, 'ename': 'raju', 
    'esal': 890000.0, 'eaddr': 'mumbai'}, {'id': 3, 'eno': 80000, 'ename': 'Kedar', 'esal': 9000.0, 'eaddr': 'kolkata'}]>
    
    emp=Employee.objects.filter(Q(ename__startswith='ra')|Q(esal__gt=4000)).values()
    <QuerySet [{'id': 1, 'eno': 1, 'ename': 'raj', 'esal': 8000.0, 'eaddr': 'pune'}, {'id': 2, 'eno': 2, 'ename': 'raju', 
    'esal': 890000.0, 'eaddr': 'mumbai'}, {'id': 3, 'eno': 80000, 'ename': 'Kedar', 'esal': 9000.0, 'eaddr': 'kolkata'}]>
    
    # AND Queries
    emp=(Employee.objects.filter(ename__startswith='ra') & Employee.objects.filter(esal__gt=4000)).values()
    <QuerySet [{'id': 1, 'eno': 1, 'ename': 'raj', 'esal': 8000.0, 'eaddr': 'pune'}, {'id': 2, 'eno': 2, 'ename': 'raju', 
    'esal': 890000.0, 'eaddr': 'mumbai'}]>
    
    emp=Employee.objects.filter(ename__startswith='ra',esal__gt=4000).values()
    <QuerySet [{'id': 1, 'eno': 1, 'ename': 'raj', 'esal': 8000.0, 'eaddr': 'pune'}, {'id': 2, 'eno': 2, 'ename': 'raju', 
    'esal': 890000.0, 'eaddr': 'mumbai'}]>
    
    emp=Employee.objects.filter(Q(ename__startswith='ra')  & Q(esal__gt=4000)).values()
    <QuerySet [{'id': 1, 'eno': 1, 'ename': 'raj', 'esal': 8000.0, 'eaddr': 'pune'}, {'id': 2, 'eno': 2, 'ename': 'raju', 
    'esal': 890000.0, 'eaddr': 'mumbai'}]>
    
    # Not queries 
    emp=Employee.objects.exclude(ename__startswith='raj').values()
    <QuerySet [{'id': 3, 'eno': 80000, 'ename': 'Kedar', 'esal': 9000.0, 'eaddr': 'kolkata'}, {'id': 4, 'eno': 90, 'ename': 'sai', 'esal': 4000.0, 'eaddr': 'ooty'}]>
    
    emp=Employee.objects.filter(~Q(ename__startswith='raj')).values()
    <QuerySet [{'id': 3, 'eno': 80000, 'ename': 'Kedar', 'esal': 9000.0, 'eaddr': 'kolkata'}, {'id': 4, 'eno': 90, 'ename': 'sai', 'esal': 4000.0, 'eaddr': 'ooty'}]>
    
    # Union operator
    emp1=Employee.objects.filter(ename__startswith='ra')
    emp2=Employee.objects.filter(esal__gt=4000)
    emp=(emp1.union(emp2)).values()
    <QuerySet [{'id': 1, 'eno': 1, 'ename': 'raj', 'esal': 8000.0, 'eaddr': 'pune'}, {'id': 2, 'eno': 2, 'ename': 'raju', 
    'esal': 890000.0, 'eaddr': 'mumbai'}, {'id': 3, 'eno': 80000, 'ename': 'Kedar', 'esal': 9000.0, 'eaddr': 'kolkata'}]>
    
    # How to select only some columns in the queryset
    emp=Employee.objects.all().values_list('eno','ename','esal','eaddr')
    <QuerySet [(1, 'raj', 8000.0, 'pune'), (2, 'raju', 890000.0, 'mumbai'), (80000, 'Kedar', 9000.0, 'kolkata'), (90, 'sai', 4000.0, 'ooty')]>
    
    emp=Employee.objects.all().values('eno','ename','esal','eaddr')
    <QuerySet [{'eno': 1, 'ename': 'raj', 'esal': 8000.0, 'eaddr': 'pune'}, {'eno': 2, 'ename': 'raju', 'esal': 890000.0, 
    'eaddr': 'mumbai'}, {'eno': 80000, 'ename': 'Kedar', 'esal': 9000.0, 'eaddr': 'kolkata'}, {'eno': 90, 'ename': 'sai', 'esal': 4000.0, 'eaddr': 'ooty'}]>
    
    emp=Employee.objects.all().only('eno','ename','esal','eaddr')
    <QuerySet [{'id': 1, 'eno': 1, 'ename': 'raj', 'esal': 8000.0, 'eaddr': 'pune'}, {'id': 2, 'eno': 2, 'ename': 'raju', 
    'esal': 890000.0, 'eaddr': 'mumbai'}, {'id': 3, 'eno': 80000, 'ename': 'Kedar', 'esal': 9000.0, 'eaddr': 'kolkata'}, {'id': 4, 'eno': 90, 'ename': 'sai', 'esal': 4000.0, 'eaddr': 'ooty'}]> <class 'django.db.models.query.QuerySet'>

    # Aggregate Functions
    emp=Employee.objects.all().aggregate(Avg('esal'))
    {'esal__avg': 227750.0}
    
    emp=Employee.objects.all().aggregate(Max('esal'))
    {'esal__max': 890000.0}
    
    emp=Employee.objects.all().aggregate(Min('esal'))
    {'esal__min': 4000.0}
    
    emp=Employee.objects.all().aggregate(Sum('esal'))
    {'esal__sum': 911000.0}
    
    emp=Employee.objects.all().aggregate(Count('esal'))
    {'esal__count': 4}
    
    # queryset using sorting order
    emp=Employee.objects.all().order_by('eno')
    <QuerySet [{'id': 1, 'eno': 1, 'ename': 'raj', 'esal': 8000.0, 'eaddr': 'pune'}, {'id': 2, 'eno': 2, 'ename': 'raju', 
    'esal': 890000.0, 'eaddr': 'mumbai'}, {'id': 4, 'eno': 90, 'ename': 'sai', 'esal': 4000.0, 'eaddr': 'ooty'}, {'id': 3, 'eno': 80000, 'ename': 'Kedar', 'esal': 9000.0, 'eaddr': 'kolkata'}]>
    
    emp=Employee.objects.all().order_by('-eno')
    <QuerySet [{'id': 3, 'eno': 80000, 'ename': 'Kedar', 'esal': 9000.0, 'eaddr': 'kolkata'}, {'id': 4, 'eno': 90, 'ename': 'sai', 'esal': 4000.0, 'eaddr': 'ooty'}, {'id': 2, 'eno': 2, 'ename': 'raju', 'esal': 890000.0, 'eaddr': 'mumbai'}, 
    {'id': 1, 'eno': 1, 'ename': 'raj', 'esal': 8000.0, 'eaddr': 'pune'}]>
    
    # second higest salary
    emp=Employee.objects.all().order_by('-esal').values()
    print("emp..........",emp[1])
    {'id': 3, 'eno': 80000, 'ename': 'Kedar', 'esal': 9000.0, 'eaddr': 'kolkata'}
    
    emp=Employee.objects.all().order_by('esal').values()
    print("emp..........",emp[1:3])
    <QuerySet [{'id': 1, 'eno': 1, 'ename': 'raj', 'esal': 8000.0, 'eaddr': 'pune'}, 
    {'id': 3, 'eno': 80000, 'ename': 'Kedar', 'esal': 9000.0, 'eaddr': 'kolkata'}]>
    """
    return HttpResponse('<h1>Hello</h1>')