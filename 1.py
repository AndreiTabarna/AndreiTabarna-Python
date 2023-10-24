#1---------------------

def list_operations(a, b):
    intersection = set(a) & set(b)
    union = set(a) | set(b)
    diff_a = set(a) - set(b)
    diff_b = set(b) - set(a)
    return [intersection, union, diff_a, diff_b]

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
result = list_operations(a, b)
print(result)

#2---------------------

def count_characters(text):
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count
    
text = "Ana has apples."
char_count = count_characters(text)
print(char_count)

#3---------------------

def compare_dicts(dict1, dict2):
    if type(dict1) != type(dict2):
        return False
    if isinstance(dict1, dict):
        if len(dict1) != len(dict2):
            return False
        for key in dict1:
            if key not in dict2:
                return False
            if not compare_dicts(dict1[key], dict2[key]):
                return False
        return True
    elif isinstance(dict1, (list, set)):
        if len(dict1) != len(dict2):
            return False
        for val1, val2 in zip(sorted(dict1), sorted(dict2)):
            if not compare_dicts(val1, val2):
                return False
        return True
    else:
        return dict1 == dict2
        
dict1 = {'a': 1, 'b': [1, 2, 3]}
dict2 = {'b': [3, 2, 1], 'a': 1}
print(compare_dicts(dict1, dict2))  

#4---------------------

def build_xml_element(tag, content, **attributes):
    attribute_str = " ".join([f'{key}="{value}"' for key, value in attributes.items()])
    return f'<{tag} {attribute_str}>{content}</{tag}>'
    
xml_element = build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
print(xml_element)

#5---------------------

def validate_dict(rules, d):
    for key, prefix, middle, suffix in rules:
        if key in d:
            value = d[key]
            if not value.startswith(prefix):
                return False
            if not value.endswith(suffix):
                return False
            if middle not in value[1:-1]:
                return False
        else:
            return False  
    return True


rules = [("key1", "", "inside", ""), ("key2", "start", "middle", "winter")]
d = {
    "key1": "come inside, it's too cold out",
    "key3": "this is not valid"
}

result = validate_dict(rules, d)
print(result)

#6---------------------

def count_unique_and_duplicate_elements(lst):
    unique_elements = len(set(lst))
    duplicate_elements = len(lst) - unique_elements
    return unique_elements, duplicate_elements
    
lst = [1, 2, 2, 3, 4, 4, 5]
unique, duplicate = count_unique_and_duplicate_elements(lst)
print(unique, duplicate)

#7---------------------

def set_operations(*sets):
    result = {}
    set_list = list(sets)
    for i in range(len(set_list)):
        for j in range(i + 1, len(set_list)):
            set1 = set_list[i]
            set2 = set_list[j]
            result[f"{set1} | {set2}"] = set1 | set2
            result[f"{set1} & {set2}"] = set1 & set2
            result[f"{set1} - {set2}"] = set1 - set2
            result[f"{set2} - {set1}"] = set2 - set1
    return result
    
set1 = {1, 2}
set2 = {2, 3}
set3 = {3, 4}
result = set_operations(set1, set2, set3)
print(result)

#8---------------------

def loop(mapping):
    visited = set()  
    result = []
    current_key = mapping.get('start', None)

    while current_key and current_key not in visited:
        visited.add(current_key)
        result.append(current_key)
        current_key = mapping.get(current_key, None)

    return result


mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
print(loop(mapping))

#9---------------------

def count_positional_in_keyword_args(*args, **kwargs):
    return sum(arg in kwargs.values() for arg in args)
    
result = count_positional_in_keyword_args(1, 2, 3, 4, x=1, y=2, z=3, w=5)
print(result)

