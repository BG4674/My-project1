class TodoList:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"name": task, "completed": False})

    def complete_task(self, task_name):
        for task in self.tasks:
            if task["name"] == task_name:
                task["completed"] = True
                break

    def delete_task(self, task_name):
        self.tasks = [task for task in self.tasks if task["name"] != task_name]


class TodoApp:
    def __init__(self):
        self.todo_lists = []

    def create_todo_list(self, name):
        self.todo_lists.append(TodoList(name))

    def edit_todo_list_name(self, index, new_name):
        self.todo_lists[index].name = new_name

    def delete_todo_list(self, index):
        del self.todo_lists[index]

    def display_lists(self):
        for i, todo_list in enumerate(self.todo_lists):
            print(f"{i + 1}. {todo_list.name}")

    def display_tasks(self, index):
        todo_list = self.todo_lists[index]
        print(f"To-Do List: {todo_list.name}")
        for task in todo_list.tasks:
            status = "Completed" if task["completed"] else "Incomplete"
            print(f" - {task['name']} ({status})")

    def run(self):
        while True:
            print("\n===== To-Do List App =====")
            print("1. Create a new to-do list")
            print("2. Edit the name of a to-do list")
            print("3. Delete a to-do list")
            print("4. Display to-do lists")
            print("5. Add task to a to-do list")
            print("6. Complete a task")
            print("7. Delete a task")
            print("8. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter the name for your new to-do list: ")
                self.create_todo_list(name)

            elif choice == "2":
                self.display_lists()
                index = int(input("Enter the index of the to-do list to edit: ")) - 1
                new_name = input("Enter the new name for the to-do list: ")
                self.edit_todo_list_name(index, new_name)

            elif choice == "3":
                self.display_lists()
                index = int(input("Enter the index of the to-do list to delete: ")) - 1
                self.delete_todo_list(index)

            elif choice == "4":
                self.display_lists()

            elif choice == "5":
                self.display_lists()
                index = int(input("Enter the index of the to-do list to add a task: ")) - 1
                task = input("Enter the task: ")
                self.todo_lists[index].add_task(task)

            elif choice == "6":
                self.display_lists()
                index = int(input("Enter the index of the to-do list to complete a task: ")) - 1
                self.display_tasks(index)
                task_name = input("Enter the name of the task to complete: ")
                self.todo_lists[index].complete_task(task_name)

            elif choice == "7":
                self.display_lists()
                index = int(input("Enter the index of the to-do list to delete a task: ")) - 1
                self.display_tasks(index)
                task_name = input("Enter the name of the task to delete: ")
                self.todo_lists[index].delete_task(task_name)

            elif choice == "8":
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    todo_app = TodoApp()
    todo_app.run()
