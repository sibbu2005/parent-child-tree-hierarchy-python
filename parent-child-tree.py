
def create_hierarchy_tree(data, hierarchy={}):
    """
    :param data: #Sample data input data as dictionary:
    {
      1: {
        "id": 1,
        "parent_id": 2,
        "Name": "One",
        "children": {

        }
      },
      2: {
        "id": 2,
        "parent_id": 0,
        "Name": "Two",
        "children": {

        }
      },
      3: {
        "id": 3,
        "parent_id": 0,
        "Name": "Three",
        "children": {

        }
      },
      4: {
        "id": 4,
        "parent_id": 2,
        "Name": "Four",
        "children": {

        }
      },
      5: {
        "id": 5,
        "parent_id": 3,
        "Name": "Five",
        "children": {

        }
      },
      6: {
        "id": 6,
        "parent_id": 3,
        "Name": "Six",
        "children": {

        }
      },
      7: {
        "id": 7,
        "parent_id": 1,
        "Name": "Seven",
        "children": {

        }
      }
    }
    :param hierarchy:
    #Output Data as Dictionary:
    :return hierarchy:
    {
      2: {
        "id": 2,
        "parent_id": 0,
        "Name": "Two",
        "children": {
          1: {
            "id": 1,
            "parent_id": 2,
            "Name": "One",
            "children": {
              7: {
                "id": 7,
                "parent_id": 1,
                "Name": "Seven",
                "children": {

                }
              }
            }
          },
          4: {
            "id": 4,
            "parent_id": 2,
            "Name": "Four",
            "children": {

            }
          }
        }
      },
      3: {
        "id": 3,
        "parent_id": 0,
        "Name": "Three",
        "children": {
          5: {
            "id": 5,
            "parent_id": 3,
            "Name": "Five",
            "children": {

            }
          }
        }
      },
      6: {
        "id": 6,
        "parent_id": 3,
        "Name": "Six",
        "children": {

        }
      }
    }
    """
    if not hierarchy:
        for r_id, r_val in data.items():
            if r_val.get('parent_id') == 0:
                r_val['children'] = {}
                hierarchy[r_id] = r_val
    for role_id, role_data in hierarchy.items():
        child_roles, untouched_roles = {}, {}
        for sub_role_id, sub_role_data in data.items():
            if sub_role_data.get('parent_id') == role_id:
                sub_role_data['children'] = {}
                child_roles[sub_role_id] = sub_role_data
            elif sub_role_data.get('parent_id') is not 0:
                untouched_roles[sub_role_id] = sub_role_data
        if child_roles and untouched_roles:
            hierarchy[role_id]['children'] = create_hierarchy_tree(untouched_roles, child_roles)
        elif not untouched_roles and child_roles:
            hierarchy[role_id]['children'] = child_roles
    return hierarchy
