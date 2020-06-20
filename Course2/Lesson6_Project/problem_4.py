"""
TASK4:
Active Directory
In Windows Active Directory, a group can consist of user(s) and group(s) themselves.
We can construct this hierarchy as such. Where User is represented by str representing their ids.

Write a function that provides an efficient look up of whether the user is in a group.
"""


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user_name, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    '''
    users_list = group.get_users()
    print("->is_user_in_group: user_name={}".format(user_name))

    if user_name in users_list:
        return True

    groups_list = group.get_groups()
    for group in groups_list:
        if group.get_users()
    '''

    return False


def test_is_user_in_group_1():
    print("->test_is_user_in_group: start")

    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    '''
    # case1
    result = is_user_in_group("sub_child_user", sub_child)
    assert result, "case1: result={}, expected={}".format(result, True)
    # case2
    result = is_user_in_group("sub_child_user", parent)
    assert result, "case2: result={}, expected={}".format(result, True)
    '''
    print("->test_is_user_in_group: is finished...")


def test():
    test_is_user_in_group_1()


test()
