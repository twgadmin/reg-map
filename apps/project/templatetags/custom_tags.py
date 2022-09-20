from django import template
import random 

register = template.Library()

@register.simple_tag
def set_value(value):
    return value

@register.simple_tag
def set_address(v):
    return 2 ** 16

@register.simple_tag
def set_length(registers):
    return len(registers) - 1

@register.simple_tag
def set_hex_from(value):
    if value == 0:
        h = str(hex(value))
    else:
        h = str(hex(value))
    return "0x"+"0"*(4-len(h)+2)+h[2:]

@register.simple_tag
def set_hex_to(value):
    h = str(hex(value - 1))
    return "0x"+"0"*(4-len(h)+2)+h[2:]

@register.simple_tag
def set_next_addr(value, size):
    return  value + int(size)

@register.simple_tag
def set_scale(a, b):
    return  b-a

@register.simple_tag
def calc_delta(a, b):
    return  b- a

@register.simple_tag
def set_last(a, b):
    return  a + b   

@register.simple_tag
def set_reserved_range(fields, ws):
    if len(fields) == 0:
        return ws - 1
    else:
        return fields[len(fields) - 1].range_lower -1

@register.simple_tag
def get_address(registers, index):
    if index == len(registers) - 1:
        if index == 0:
            prev = 0
            next = registers[index].size + 1
        else:
            prev = registers[index - 1].address +registers[index - 1].size
            next = registers[index].address + registers[index].size + 1
    else:
        if index == 0:
            prev = 0
            next = registers[index+1].address
        else:
            prev = registers[index - 1].address +registers[index - 1].size
            next = registers[index + 1].address + 1
    return {"prev": prev, "next": next}

@register.simple_tag
def get_random_number(v):
    return random.randint(0, 9999)