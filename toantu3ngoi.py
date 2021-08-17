num_check = float(input("nhập số :"))

msg = "Even" if num_check %2 == 0 else "Odd"
print(msg)

msg = ""
if(num_check%2  == 0):
    msg = "Even"
else:
    msg = "Odd"
