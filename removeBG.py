

from rembg import remove

input_path = './input_pictures/thoughtful.png'
output_path = './output_pictures/thoughtful.png'

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)

print('Background removed successfully!')