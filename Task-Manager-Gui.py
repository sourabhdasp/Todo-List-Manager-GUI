from tkinter import *
import tkinter.messagebox as msgbx

from my_custom_function import import_tasks_from_file, save_and_exit, add_task, get_updated_task_list

import_tasks_from_file()

root = Tk()
root.title("Todo-Manager")
root.wm_iconbitmap("main.ico")
root.geometry("1100x500")
root.minsize(1100, 500)
root.configure(background="#133852")

# Status Bar
status_bar = Frame(root, bg="black")
status_bar_message = Label(status_bar, bg="black", fg="white", text="Welcome to Task Manager", font="ubuntu-mono 8 ")
status_bar.pack(side="bottom", fill=X)
status_bar_message.pack(side="left")

# Sidebar/Menu Bar
sidebar = Frame(root, background="#031e30")
sidebar.pack(side="left", fill=Y)

# Heading
heading = Frame(root, background="yellow")
heading.pack(side="top", fill=X, anchor="center")

# Home Page
home_page = Frame(root, background="#133852")

# Show Container for Adding New Task
show_container_add_new_task = Frame(root, bg="#133852")
frame_title = Frame(show_container_add_new_task, bg="#133852")
frame_priority = Frame(show_container_add_new_task, bg="#133852")
frame_add_task_btn = Frame(show_container_add_new_task, bg="#133852")

# Show All Tasks
show_all_tasks_container = Frame(home_page, background="#133852")

# Create a Canvas and Scrollbar for the Tasks
canvas = Canvas(show_all_tasks_container, bg="#133852")
scrollbar = Scrollbar(show_all_tasks_container, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

# Create a Frame inside the Canvas to hold the task labels
tasks_frame = Frame(canvas, background="#133852")
canvas.create_window((0, 0), window=tasks_frame, anchor="nw")

# Pack the Canvas and Scrollbar
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Variables
user_input = StringVar()
task_priority_level = IntVar()

def add_task_helper():
    add_task(user_input.get(), task_priority_level.get())
    status_bar_message.config(text=f"Task Added: '{user_input.get()}' with priority [{task_priority_level.get()}]")
    show_task_list_ui()

def show_task_list_ui():
    main_heading.config(text="All Task List")
    show_container_add_new_task.pack_forget()
    home_page.pack(fill="both", expand=True)
    show_all_tasks_container.pack(fill="both", expand=True)

    # Clear existing widgets in tasks_frame
    for widget in tasks_frame.winfo_children():
        widget.destroy()

    tasks = get_updated_task_list()
    headers = ["UID", "Title", "Priority", "Status"]
    for col, header in enumerate(headers):
        Label(tasks_frame, text=header, font=('Helvetica', 10, 'bold'), background="white", fg="red").grid(row=0, column=col, padx=20, pady=5)

    for row, task in enumerate(tasks, start=1):
        Label(tasks_frame, text=task.get("uid", "N/A"), background="#133852", fg="white", font=("Arial", 14)).grid(row=row, column=0, padx=20, pady=5)
        Label(tasks_frame, text=task.get("title", "N/A"), background="#133852", fg="white", font=("Arial", 14)).grid(row=row, column=1, padx=20, pady=5)
        Label(tasks_frame, text=task.get("priority", "N/A"), background="#133852", fg="white", font=("Arial", 14)).grid(row=row, column=2, padx=20, pady=5)
        Label(tasks_frame, text=task.get("status", "N/A"), background="#133852", fg="white", font=("Arial", 14)).grid(row=row, column=3, padx=20, pady=5)
    tasks_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def show_task_creation_form():
    main_heading.config(text="Add New Task")
    home_page.pack_forget()
    frame_title.pack(side="top", fill="both", anchor="center", pady=10)
    frame_priority.pack(side="top", fill="both", anchor="center", padx=10, ipadx=50)
    frame_add_task_btn.pack(side="top", fill="both", anchor="center", pady=10)
    show_container_add_new_task.pack(side=TOP, fill=BOTH, anchor=CENTER)
    show_container_add_new_task_label.pack(side=TOP, pady=20, padx=20)
    get_user_input.pack(side="top", ipadx=10, ipady=5, fill=X, padx=40)
    add_task_button.pack(side="top", pady=10, padx=40)

def on_close():
    output = msgbx.askquestion("File not saved", "Do you want to save your file now!")
    if output == "yes":
        save_and_exit()
    root.destroy()

def edit_task_form():
    print("Editing")

def delete_task_form():
    print("Deleting")

def show_complete_task_form():
    print("Showing completed")

def show_pending_task_form():
    print("Showing pending")

def show_priority_task_form():
    print("Showing priority")

def save_exit_form():
    print("Save and exit")

get_user_input = Entry(frame_title, textvariable=user_input, font="lato 20 bold", borderwidth=3)
add_task_button = Button(frame_add_task_btn, text="Add Task", fg="white", bg="purple", padx=50, command=add_task_helper)
show_container_add_new_task_label = Label(frame_title, background="red", fg="white", text="Enter the Task title and priority", font="lucida 10 bold", padx=20)
Label(frame_priority, text="Choose priority from 1-5, else considered as 0", bg="#133852", fg="white", font="lato 10 italic").pack(side="left", padx=10)
Radiobutton(frame_priority, text=1, padx=15, variable=task_priority_level, value=1, bg="#133852", font="lato 15 bold", fg="red").pack(side="left")
Radiobutton(frame_priority, text=2, padx=15, variable=task_priority_level, value=2, bg="#133852", font="lato 15 bold", fg="red").pack(side="left")
Radiobutton(frame_priority, text=3, padx=15, variable=task_priority_level, value=3, bg="#133852", font="lato 15 bold", fg="red").pack(side="left")
Radiobutton(frame_priority, text=4, padx=15, variable=task_priority_level, value=4, bg="#133852", font="lato 15 bold", fg="red").pack(side="left")
Radiobutton(frame_priority, text=5, padx=15, variable=task_priority_level, value=5, bg="#133852", font="lato 15 bold", fg="red").pack(side="left")

main_heading = Label(heading, text="All Task List", bg="yellow", font="lato 30 bold")
main_heading.pack(side="top", padx=20)
Label(sidebar, background="red", fg="white", text="Menu", font="lato 10 bold").grid(row=0, column=1, pady=20)

Button(sidebar, width=15, height=1, text="Add Task", fg="white", bg="purple", padx=20, command=show_task_creation_form).grid(row=1, column=1, pady=10, padx=40)
Button(sidebar, width=15, height=1, text="Show All Task", fg="white", bg="purple", padx=20, command=show_task_list_ui).grid(row=7, column=1, pady=10, padx=40)
Button(sidebar, width=15, height=1, text="Edit Task", fg="white", bg="purple", padx=20, command=edit_task_form).grid(row=2, column=1, pady=10, padx=40)
Button(sidebar, width=15, height=1, text="Delete Task", fg="white", bg="purple", padx=20, command=delete_task_form).grid(row=3, column=1, pady=10, padx=40)
Button(sidebar, width=15, height=1, text="Show Completed Task", fg="white", bg="purple", padx=20, command=show_complete_task_form).grid(row=4, column=1, pady=10, padx=40)
Button(sidebar, width=15, height=1, text="Show Pending Task", fg="white", bg="purple", padx=20, command=show_pending_task_form).grid(row=5, column=1, pady=10, padx=40)
Button(sidebar, width=15, height=1, text="Show Priority Task", fg="white", bg="purple", padx=20, command=show_priority_task_form).grid(row=6, column=1, pady=10, padx=40)
Button(sidebar, width=15, height=1, text="Save & Exit", fg="white", bg="purple", padx=20, command=save_exit_form).grid(row=8, column=1, pady=10, padx=40)

show_task_list_ui()

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
