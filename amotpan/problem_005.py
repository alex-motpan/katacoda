# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. 
# Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.
# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
# The following are examples of expected output values:
# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3

def rgb(r, g, b):
    
    #value range check
    r = 0 if r < 0 else 255 if r > 255 else r
    g = 0 if g < 0 else 255 if g > 255 else g
    b = 0 if b < 0 else 255 if b > 255 else b
    
    hexa_dict = {0: '0', 1: '1', 2: '2', 3: '3',
                 4: '4', 5: '5', 6: '6', 7: '7',
                 8: '8', 9: '9', 10: 'A', 11: 'B',
                 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    
    r_1, r_2 = r // 16, r % 16
    g_1, g_2 = g // 16, g % 16
    b_1, b_2 = b // 16, b % 16
    
    return "{}{}{}{}{}{}".format(hexa_dict[r_1],hexa_dict[r_2],hexa_dict[g_1],hexa_dict[g_2],hexa_dict[b_1], hexa_dict[b_2])



#Tests
test_cases = {(255, 255, 255): 'FFFFFF', (255, 255, 300): 'FFFFFF', (0,0,0): '000000', (148,0,211): '9400D3'}
for key, value in test_cases.items():
    x, y, z = key
    if rgb(x,y,z) == value:
        print(f'rgb{key} = {value} -> OK!')
    else:
        print(f'rgb{key} = {value} -> NOT OK!')