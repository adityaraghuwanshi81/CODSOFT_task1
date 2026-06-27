from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("To-Do List - CodSoft")
root.geometry("650x650")
root.config(bg="#EAF4FC")

tasks = []

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task = line.strip()
                tasks.append(task)
                listbox.insert(END, task)
    except FileNotFoundError:
        pass


def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


def add_task():
    task = task_entry.get()
    date = date_entry.get()
    time = time_entry.get()

    if task == "" or date == "" or time == "":
        messagebox.showwarning("Warning", "Please fill all fields.")
        return

    full_task = f"{task} | Date: {date} | Time: {time}"

    tasks.append(full_task)
    listbox.insert(END, full_task)

    task_entry.delete(0, END)
    date_entry.delete(0, END)
    time_entry.delete(0, END)

    save_tasks()


def delete_task():
    try:
        index = listbox.curselection()[0]

        listbox.delete(index)
        tasks.pop(index)

        save_tasks()

    except:
        messagebox.showwarning("Warning", "Select a task first.")


def complete_task():
    try:
        index = listbox.curselection()[0]

        if not tasks[index].startswith("✔"):
            tasks[index] = "✔ " + tasks[index]

            listbox.delete(index)
            listbox.insert(index, tasks[index])

            save_tasks()

    except:
        messagebox.showwarning("Warning", "Select a task first.")


def clear_tasks():
    if messagebox.askyesno("Confirm", "Delete all tasks?"):
        tasks.clear()
        listbox.delete(0, END)
        save_tasks()

Label(
    root,
    text="TO-DO LIST",
    font=("Arial", 22, "bold"),
    bg="#EAF4FC",
    fg="navy"
).pack(pady=10)

Label(root, text="Task Name", bg="#EAF4FC", font=("Arial", 11, "bold")).pack()

task_entry = Entry(root, width=40, font=("Arial", 13))
task_entry.pack(pady=5)

Label(root, text="Due Date (DD-MM-YYYY)", bg="#EAF4FC", font=("Arial", 11, "bold")).pack()

date_entry = Entry(root, width=40, font=("Arial", 13))
date_entry.pack(pady=5)

Label(root, text="Due Time (HH:MM AM/PM)", bg="#EAF4FC", font=("Arial", 11, "bold")).pack()

time_entry = Entry(root, width=40, font=("Arial", 13))
time_entry.pack(pady=5)

Button(
    root,
    text="Add Task",
    bg="green",
    fg="white",
    width=20,
    font=("Arial", 12, "bold"),
    command=add_task
).pack(pady=5)

Button(
    root,
    text="Mark Completed",
    bg="blue",
    fg="white",
    width=20,
    font=("Arial", 12, "bold"),
    command=complete_task
).pack(pady=5)

Button(
    root,
    text="Delete Task",
    bg="red",
    fg="white",
    width=20,
    font=("Arial", 12, "bold"),
    command=delete_task
).pack(pady=5)

Button(
    root,
    text="Clear All",
    bg="orange",
    fg="white",
    width=20,
    font=("Arial", 12, "bold"),
    command=clear_tasks
).pack(pady=5)

frame = Frame(root)
frame.pack(pady=15)

scroll = Scrollbar(frame)

listbox = Listbox(
    frame,
    width=70,
    height=15,
    font=("Arial", 11),
    yscrollcommand=scroll.set
)

scroll.config(command=listbox.yview)

scroll.pack(side=RIGHT, fill=Y)
listbox.pack(side=LEFT)

load_tasks()

root.mainloop()