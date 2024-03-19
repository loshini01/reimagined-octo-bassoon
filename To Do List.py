from tkinter import *
from tkinter import messagebox

tasks_list = []
counter = 1

def inputError():
    if enterTaskField.get() == "":
        messagebox.showerror("Input Error", "Please enter a task.")
        return False
    return True

def clear_taskNumberField():
    taskNumberField.delete(0.0, END)

def clear_taskField():
    enterTaskField.delete(0, END)

def insertTask():
    global counter
    if inputError():
        content = enterTaskField.get() + "\n"
        tasks_list.append(content)
        TextArea.insert(END, f"[{counter}] {content}")
        counter += 1
        clear_taskField()

def delete():
    global counter
    if not tasks_list:
        messagebox.showerror("No tasks", "There are no tasks to delete.")
        return

    try:
        task_no = int(taskNumberField.get(1.0, END))
        if 1 <= task_no <= len(tasks_list):
            tasks_list.pop(task_no - 1)
            counter -= 1
            clear_taskNumberField()
            TextArea.delete(1.0, END)
            for i, task in enumerate(tasks_list, start=1):
                TextArea.insert(END, f"[{i}] {task}")
        else:
            messagebox.showerror("Invalid Task Number", "Please enter a valid task number.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid task number.")

if __name__ == "__main__":
    tk = Tk()
    tk.title("To-Do-List App")
    tk.configure(background="light blue")
    tk.geometry("250x300")


    TextArea = Text(tk, height=5, width=25, font="lucida 13")
    enterTask = Label(tk, text="      Enter Your Task     ", bg="light pink")
    enterTaskField = Entry(tk, bg="white")
    Submit = Button(tk, text="SUBMIT", fg="Black", bg="Red", command=insertTask)
   
    taskNumber = Label(tk, text="  Delete Task Number  ", bg="light pink")
    taskNumberField = Text(tk, height=1, width=2, font="lucida 13")
    delete_button = Button(tk, text="DELETE", fg="Black", bg="Red", command=delete)
    Exit = Button(tk, text="EXIT", fg="Black", bg="Red", command=exit)
    TextArea.grid(row=0, column=2, padx=10, sticky=W)
    enterTask.grid(row=1, column=2)
    enterTaskField.grid(row=2, column=2, ipadx=50)
    Submit.grid(row=3, column=2)
    taskNumber.grid(row=4, column=2, pady=5)
    taskNumberField.grid(row=5, column=2)
    delete_button.grid(row=6, column=2, pady=15)
    Exit.grid(row=9, column=2)

    tk.mainloop()
