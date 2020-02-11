class LambdaHelper:
    def __init__(self):
        pass

    @staticmethod
    def for_each_dict(dicts: dict, func):
        if LambdaHelper.is_none_or_empty_dict(dicts):
            return
        for key in dicts.keys():
            func(key)

    @staticmethod
    def for_each_list(items: list, func):
        if LambdaHelper.is_none_or_empty_list(items):
            return
        for item in items:
            func(item)

    @staticmethod
    def is_contains_str(str_list: list, str_element):
        if LambdaHelper.is_none_or_empty_list(str_list):
            return False
        for str_item in str_list:
            if str_item == str_element:
                return True
        return False

    @staticmethod
    def is_none_or_empty_dict(dicts: dict):
        return dicts is None or len(dicts.keys()) == 0

    @staticmethod
    def is_none_or_empty_list(items: list):
        return items is None or len(items) == 0