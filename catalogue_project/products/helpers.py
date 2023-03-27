import pandas as pd
import os
from django.conf import settings
from .models import Products

excel_file = os.path.join(settings.BASE_DIR, 'items.xlsx')

def get_excel_values():
    """Helper function to add excels records to database"""

    print(settings.BASE_DIR)
    data = pd.read_excel(excel_file)
    for _, row in data.iterrows():
        item_code = row['Item Code']
        item_name = row['Item Name']
        category_l1 = row['Category L1']
        category_l2 = row['Category L2']
        upc = row['UPC']
        parent_code = row['Parent Code']
        price = row['MRP Price']
        size = row['Size']
        enabled = row['Enabled']
        active = get_active_value(enabled)

        if not Products.objects.filter(item_code=item_code).exists():
            product = Products.objects.create(
                item_code=item_code,
                item_name=item_name,
                category_l1=category_l1,
                category_l2=category_l2,
                upc=upc,
                parent_code=parent_code,
                price=price,
                size=size,
                active=active
            )
            product.save()

def get_active_value(enabled):
    """ A helper function to return boolean equivalent"""

    active = None
    if enabled == "Yes" or enabled == "Y":
        active = 1
    else:
        active = 0
    return active
    

def get_products():
    """To get all the available products"""

    get_excel_values()
    products = Products.objects.all()
    return products

def get_topmost_parent(item_code):
    parent= None
    if Products.objects.filter(item_code=item_code).exists():
        parent_product = Products.objects.get(item_code=item_code)
        while parent_product.parent_code != "nan":
            parent_product = Products.objects.get(item_code=parent_product.parent_code)
        parent = parent_product.item_code
        
    return parent

def get_children(item_code):
    data = None
    if Products.objects.filter(item_code=item_code).exists():
        data = []
        children = Products.objects.filter(parent_code=item_code).order_by('item_code')
        for child in children:
            data.append(child.item_code)
    return data

def count_products():
    data = {"active":0, "inactive" :1}
    data["active"] = Products.objects.filter(active=True).count()
    data["inactive"] = Products.objects.filter(active=False).count()
    return data
        




