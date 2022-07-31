# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.

input_file=open('input_data.txt', 'r')
data=input_file.read()
input_file.close()

def compress(data):
    compressed = str()
    count = 1
    data += ' '
    for i in range(1, len(data)):
        if data[i] == data[i-1]:
            count += 1
        else:
            compressed += data[i-1] + str(count)
            count = 1
    return compressed

def uncompress(data):
    uncompressed=str()
    for i in range(1, len(data)):
        if data[i] in '123456789':
            uncompressed+=data[i-1]*int(data[i])
    return uncompressed

output_file=open('output_data.txt', 'w')

for i in range(1, len(data)):
    if data[i] in '123456789':
        output_file.write(uncompress(data))
        break
    else:
        output_file.write(compress(data))
        break

output_file.close()