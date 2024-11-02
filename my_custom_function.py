import json
from tkinter import StringVar

task_id = 0
task_list = []
task_name = ""
task_dictionary = {}
# console = Console()

def import_tasks_from_file():
    global task_list
    print("importing tasks from backup file")
    try:
        f = open("tasks.json","r")
        task_json = f.read()
        # print("task_json is :")
        # print(task_json)
        f.close()
        if task_json == "":
                # print("task_json is empty")
                task_list = []
        else:
                task_list = json.loads(task_json)
                # print(task_list)
    except FileNotFoundError:
            print("Backup file not found. Starting with an empty task list")
            task_list = []
def save():
    print("updated")
    tasks_json = json.dumps(task_list)
    f = open("tasks.json", "w")
    f.write(tasks_json)
def save_and_exit():
    global task_list
    tasks_json = json.dumps(task_list)
    # print(tasks_json)
    try:
        f = open("tasks.json","w")
        f.write(tasks_json)
        print("file saved successfully")
        f.close()
    except FileNotFoundError:
            print("backup file not found")
    exit()


def add_task(inputedvalue,priority):
    global task_id, task_list,task_name,task_priority
    task_priority = priority
    try:
        # print("Enter the task title:\n ")
        task_name = inputedvalue
        print(f"frome here{task_name}")
        # task_name = input("=> ")
        task_status = 'pending'  
        # add_priority()
        task_id +=1
        new_entry = {"uid":task_id, "title":task_name,"priority":task_priority,"status":task_status}
        # new_entry = {"uid":task_id, "title":task_name,"priority":task_priority,"status":task_status}
        task_list.append(new_entry)
    except ValueError:
        print("Enter the Integer value between 1-5")
        task_priority = 0
        # print(f"task priority  {task_priority}")
    except KeyError:
        print("Please choose with in the range (Shown above)")
        new_entry = {"uid":task_id, "title":task_name,"priority":task_priority,"status":task_status}
        # task_priority = 0
        # add_priority()



# --------------------------------------------- updated task list----------------------------------------------------------------------------
def get_updated_task_list():
    print(task_list)
    return task_list


# ---------------------------------------------Adding Priority----------------------------------------------------------------------------


def add_priority():
    global task_priority
    try:
        print("Enter the task priority: \n")
        task_priority = int(input("=> "))
        if task_priority =="":
            task_priority="0"
        elif task_priority > 5:
            print("Enter value between 1-5")
            task_priority = 0
            add_priority()
        elif task_priority < 0:
            print("Enter value between 1-5")
            task_priority = 0
            add_priority()
        # list_entry = {taskid:{"taskname":taskname,"priority":taskpriority,"status":taskstatus}}
        # print(f"[{taskid}] {taskname}")
        # tasklist.append(list_entry)
        # print(tasklist)
    except ValueError:
        print("Enter a value between 1-5 or Enter 0 to skip ")
    except KeyError:
        print("Please choose with in the range (Shown above)")
        add_priority()

# ---------------------------------------------Adding Priority----------------------------------------------------------------------------  

def gettasklist():
    print("gettting task list")
    print(task_list)
    return task_list