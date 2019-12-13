from itertools import groupby

# Function to read memory
def load_image(file):
    with open('../data/' + file, 'r') as f:
        image_data = f.read()
    return image_data

def get_checksum(image_data, wide, tall):
    layer_size = wide * tall

    check_sum = 0
    check_layer_nr = 0
    zero_num_max = 999
    i = 0
    j = 1
    while i + layer_size <= len(image_data):
        image_layer = [int(v) for v in list(image_data[i: i + layer_size])]

        for v, g in groupby(sorted(image_layer)):
            gr_size = len(list(g))
            # print('value: ' + str(v) + ' repeats: ' + str(gr_size))
            if v == 0 and gr_size < zero_num_max:
                zero_num_max = gr_size
                check_layer_data = image_layer
                check_layer_nr = j
                check_sum = 0
            elif v == 0:
                break
            if v == 1:
                check_sum = gr_size
            if v == 2:
                check_sum *= gr_size

        # print('Pointer i: ' + str(i))
        # print('Layer Nr: ' + str(check_layer_nr) + ' Zero Nbr Max: ' + str(zero_num_max) + '. Check Sum = ' + str(check_sum))

        i += layer_size
        j += 1
    return check_layer_nr, check_layer_data, zero_num_max, check_sum



def decode_image(image_data, wide, tall):
    layer_size = wide * tall

    image = [int(v) for v in list(image_data[:layer_size])]
    i = layer_size
    while i + layer_size <= len(image_data):
        image_layer = [int(v) for v in list(image_data[i: i + layer_size])]
        for j in range(len(image)):
            image[j] = image_layer[j] if image[j] == 2 else image[j]
        i += layer_size

    return str(image).replace(', ', '').replace(']', '').replace('[', '')


def draw_image(image, wide):
    # print('-' * wide)
    i = 0
    while i + wide <= len(image):
        print(image[i: i + wide].replace('0', ' ').replace('1', '#'))
        i += wide
    # print('-' * wide)

print("%%% Test 1 %%%")
# Image_Data = load_image("space_image_t1.txt")
Image_Data = '120021450512'
Check_Layer_Nr, Check_Layer_Data, Zero_Num_Max, Check_Sum = get_checksum(Image_Data, 3, 2)

Expected = 1
assert Check_Sum == Expected, "Not expected result."
print('Layer Nr: ' + str(Check_Layer_Nr) + ' Zero Nbr Max: ' + str(Zero_Num_Max) + '. Check Sum = ' + str(Check_Sum))
# print('Layer: ' + str(Check_Layer_Data))



print("%%% RUN %%%")
Image_Data = load_image("space_image.txt")
Wide = 25
Tall = 6
Check_Layer_Nr, Check_Layer_Data, Zero_Num_Max, Check_Sum = get_checksum(Image_Data, Wide, Tall)

Expected = 1206
assert Check_Sum == Expected, "Not expected result."
print('Layer Nr: ' + str(Check_Layer_Nr) + ' Zero Nbr Max: ' + str(Zero_Num_Max) + '. Check Sum = ' + str(Check_Sum))
# print('Layer: ' + str(Check_Layer_Data))

Image = decode_image(Image_Data, Wide, Tall)

draw_image(Image, Wide)
