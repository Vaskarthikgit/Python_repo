import sys, os, pdb
from Test_module import add, mul
from My_package import Pkg_module as pkg


#pdb.set_trace()  # Debug step by step from here

p_scriptname = sys.argv[0]
p_arguments = sys.argv[1:]

print("Scriptname : ",p_scriptname)
print("Arguments : ", p_arguments)

if len(p_arguments) < 2:
    print("Script required 2 params")
    sys.exit()

p_name = p_arguments[0]
p_age = p_arguments[1]

print(f"Name is {p_name} and age is {p_age}")

print("Addition result from module call: ", add(5,2))
print("Multiplication result from module call: ", mul(5,2))

print("Sum result from pkg call", pkg.f_total(10,15,20))
print("Avg result from pkg call", pkg.f_avg(10,15,20))

with open("Sample.txt",'r',encoding="utf-8") as fh:
    file_data=fh.read()

# with open("D:\Test_file.txt",'w',encoding="utf-8") as fh:
#     fh.write(file_data)

file_path="D:\Test_file.txt"

# if os.path.exists(file_path):
#     os.remove(file_path)
#     print("File has been deleted")
# else:
#     print("File is not exist to delete")
