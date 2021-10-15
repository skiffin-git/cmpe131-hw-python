def multiply_list(list):
        result = 1
        for x in list:
            if not isinstance(x, (float, int)):
                return False
            else:
                result *= x
        return result
