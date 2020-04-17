def make_xpath_with_unit_feature(loc):
    key_index = 0
    value_index = 1
    option_index = 2
    list = loc.split(',')
    feature = ""
    if len(list) == 2:
        feature = "contains(@" + list[key_index] + "='" + list[value_index] + "')"
    elif len(list) == 3:
        if list[option_index] == "1":
            feature = "@" + list[key_index] + "='" + list[value_index] + "'"
        elif list[option_index] == "0":
            feature = "contains(@" + list[key_index] + "='" + list[value_index] + "')"
    return feature
def make_xpath_with_feature(loc):
    '''

    loc:单条件输入str
        多条件输入list
    return: xpath字符串
    '''
    feature_start = "//*["
    feature_end = "]"
    feature = ""
    if isinstance(loc,str):
        if loc.startswith("//"):
            return loc
        feature = make_xpath_with_unit_feature(loc)
    else:
        for i in loc:
            feature += make_xpath_with_unit_feature(i) + "and"
    feature = feature.rstrip("and")
    return feature_start + feature +feature_end

def main():
    loc1 = "text,设置,1"
    loc2 = ["text,设置,1","aaa,ab"]
    print(make_xpath_with_feature(loc1))
    print(make_xpath_with_feature(loc2))
if __name__ == '__main__':
    main()