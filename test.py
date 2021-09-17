import aws_nsm_interface

handle = aws_nsm_interface.open_nsm_device('/dev/nsm')

buff_length = 8

string = handle.read(buff_length)
print(repr(string))
