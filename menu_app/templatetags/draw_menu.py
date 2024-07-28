from django import template
from django.utils.datastructures import MultiValueDictKeyError

from menu_app.models import MenuItem


register = template.Library()


@register.inclusion_tag('menu_app/draw_menu.html', takes_context=True)
def draw_menu(context, menu):
    items = MenuItem.objects.filter(menu__name=menu)
    item_values = items.values()
    parents = [item for item in item_values.filter(parent=None)]

    try:
        selected_item = items.get(id=context['request'].GET[menu])
        expanded_items_id_list = get_expanded_items_id_list(selected_item)
        for parent in parents:
            if parent['id'] in expanded_items_id_list:
                parent['child_items'] = get_child_items(
                    item_values, parent['id'], expanded_items_id_list
                )
        result_dict = {'items': parents}
    except MultiValueDictKeyError:
        result_dict = {'items': parents}

    result_dict['menu'] = menu
    return result_dict


def get_expanded_items_id_list(parent):
    expanded_items_id_list = []
    while parent:
        expanded_items_id_list.append(parent.id)
        parent = parent.parent
    return expanded_items_id_list


def get_child_items(item_values, current_parent_id, expanded_items_id_list):
    current_parent_child_list = [
        item for item in item_values.filter(parent_id=current_parent_id)
    ]
    for child in current_parent_child_list:
        if child['id'] in expanded_items_id_list:
            child['child_items'] = get_child_items(
                item_values, child['id'], expanded_items_id_list
            )
    return current_parent_child_list
