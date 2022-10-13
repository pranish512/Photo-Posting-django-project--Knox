from msilib.schema import tables
from pyexpat import model
from re import template
import django_tables2 as d_table
from .models import PostModel

class PostTable(d_table.Table):
    class meta:
        model = PostModel
        

class TableView(d_table.SingleTableView):
    table_class = PostTable
    template_name = "admin_page-2.html"
    queryset = PostModel.objects.exclude(status__isnull=True).all()
