from struct import pack, unpack_from
fmt='<f'
data=b'\xca\x00\x00\x00\xa0A'#A代表ASCII码的A，所以转义之后是65
index=2
x=unpack_from(fmt, data, index)[0]
for i in range(len(data)):
    print(data[i])
print(x)