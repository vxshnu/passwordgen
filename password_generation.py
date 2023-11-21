import random
import tkinter

def random_password_gen():
    capi_alpha=['A', 'B', 'C', 'D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    small_alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    special=['!', '#', '$', '%', '&', '(', ')', '*', '+']
    numbers=['1','2','3','4','5','6','7','8','9','0']

    n_ca=random.randint(2,4)
    n_sa=random.randint(2,4)
    n_s=random.randint(2,4)
    n_no=random.randint(2,4)
    a=[]
    print(n_ca)
    print(n_sa)
    print(n_s)
    print(n_no)
    for i in range(n_ca):
        a+=random.choice(capi_alpha)
    for i in range(n_sa):
        a+=random.choice(small_alpha)
    for i in range(n_s):
        a+=random.choice(special)
    for i in range(n_no):
        a+=random.choice(numbers)
    random.shuffle(a)
    result_string = ''.join(a)
    print(result_string)
    password_gen.delete(0,tkinter.END)
    password_gen.insert(0,f"{result_string}")

window=tkinter.Tk()
window.title("Password Generator")
window.geometry("400x400")
window.config(bg="black")
heading=tkinter.Label(text="PASSWORD GENERATOR",font=("timesnewroman 15 bold"),foreground="white",bg="black")
heading.place(x=85,y=10)
gen=tkinter.Button(text="Generate Password",command=random_password_gen,height=0,width=30,bg="red",foreground="black")
gen.place(x=100,y=80)
password_gen=tkinter.Entry(width=30)
password_gen.place(x=115,y=150)
window.mainloop()

