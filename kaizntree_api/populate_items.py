import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kaizntree_api.settings')
django.setup()

from dashboard.models import Item, Tag  # Replace 'app_name' with your Django app name

# # Create tags
# tags_data = ['Tag1', 'Tag2', 'Tag3']
# tags = []
# for tag_name in tags_data:
#     tag, created = Tag.objects.get_or_create(name=tag_name)
#     tags.append(tag)

# # Create items and associate tags
# items_data = [
#     {"sku": "SKU1", "name": "Item 1", "category": "Category 1", "stock_status": "In Stock", "available_stock": 100, "tags": ["Tag1", "Tag2"]},
#     {"sku": "SKU2", "name": "Item 2", "category": "Category 2", "stock_status": "Out of Stock", "available_stock": 0, "tags": ["Tag3"]},
# ]

# for item_data in items_data:
#     item_tags = item_data.pop('tags')
#     item, created = Item.objects.get_or_create(**item_data)
#     item.tags.clear()  # Clear existing tags, if re-running the script
#     for tag_name in item_tags:
#         tag = Tag.objects.get(name=tag_name)
#         item.tags.add(tag)

# Function to create tags
def create_tags(n):
    for i in range(n):
        Tag.objects.get_or_create(name=f"Tag{i}")

# Function to create items
def create_items(n):
    tag_count = Tag.objects.count()
    for i in range(n):
        sku = f"SKU{i}"
        name = f"Item {i}"
        category = f"Category {random.randint(1, 5)}"
        stock_status = random.choice(["In Stock", "Out of Stock", "Backorder"])
        available_stock = random.randint(0, 1000)

        item, created = Item.objects.get_or_create(
            sku=sku,
            name=name,
            category=category,
            stock_status=stock_status,
            available_stock=available_stock,
        )

        # Randomly assign tags to items
        tags = Tag.objects.all()[random.randint(0, tag_count-1):random.randint(0, tag_count-1)]
        item.tags.set(tags)

# Create 100 Tags
create_tags(100)

# Create 1000 Items
create_items(1000)
