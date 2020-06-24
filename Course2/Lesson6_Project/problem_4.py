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
      user_name(str): user name/id
      group(class:Group): group to check user membership against
    """

    if user_name in group.get_users():
        print("user_name={} is in group={}".format(user_name, group.name))
        return True

    for group in group.get_groups():
        return is_user_in_group(user_name, group)
    return False


def test_is_user_in_group_1():
    # print("->test_is_user_in_group_1: start")

    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    # case1
    # print("case1-----------------------------------------")
    result = is_user_in_group("sub_child_user", sub_child)
    assert result, "case1: result={}, expected={}".format(result, True)
    # case2
    # print("case2-----------------------------------------")
    result = is_user_in_group("sub_child_user", parent)
    assert result, "case2: result={}, expected={}".format(result, True)
    # case3
    # print("case3-----------------------------------------")
    result = is_user_in_group("NotExisted", parent)
    assert result == False, "case3: result={}, expected={}".format(result, False)
    # print("case4-----------------------------------------")
    result = is_user_in_group("sub_child_user", Group("some_other_group"))
    assert result == False, "case4: result={}, expected={}".format(result, False)

    # print("->test_is_user_in_group_1: is finished...")


def test_is_user_in_group_2():
    # print("->test_is_user_in_group_2: start")

    parent = Group("parent")
    parent.add_user("user1")
    parent.add_user("user4")
    parent.add_user("user7")

    group1 = Group("Gr1")
    group1.add_user("user1")
    group1.add_user("user5")
    group1.add_user("user6")
    group1.add_user("user7")
    group1.add_group(Group("Gr1_1"))
    parent.add_group(group1)

    group2 = Group("Gr2")
    group2.add_group(Group("Gr2_1"))
    group2.add_group(Group("Gr2_2"))
    parent.add_group(group2)
    parent.add_group(Group("Gr3"))
    parent.add_group(Group("Gr4"))

    group5 = Group("Gr5")
    group5.add_user("user1")
    group5.add_user("user12")
    group5.add_user("user8")
    group5.add_user("user7")
    parent.add_group(group5)

    # case1
    # print("case1-----------------------------------------")
    result = is_user_in_group("user7", group5)
    assert result, "case1: result={}, expected={}".format(result, True)
    # case2
    # print("case2-----------------------------------------")
    result = is_user_in_group("user7", parent)
    assert result, "case2: result={}, expected={}".format(result, True)
    # case3
    # print("case3-----------------------------------------")
    result = is_user_in_group("user8", group2)
    assert result == False, "case3: result={}, expected={}".format(result, False)
    # print("case4-----------------------------------------")
    result = is_user_in_group(None, parent)
    assert result == False, "case4: result={}, expected={}".format(result, False)

    # print("->test_is_user_in_group_2: is finished...")


def test():
    test_is_user_in_group_1()
    test_is_user_in_group_2()


test()
