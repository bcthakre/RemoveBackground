

from rembg import remove

input_path = './input_pictures/reflecting_new.png'
output_path = './output_pictures/reflecting_new.png'

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)

print('Background removed successfully!')