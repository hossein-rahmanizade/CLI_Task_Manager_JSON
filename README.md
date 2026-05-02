# Project: CLI Task Manager (JSON version)

## requirement:

  - [x] Get the user task and show them 
  - [x] Add task to a file
  - [ ] List tasks
  - [ ] Mark done
  - [x] Delete task
  - [x] Store in `tasks.json`
  - [ ] Each task:
        {
          "id": 1,
          "name": "...",
          "done: False,
          "priority": 1-5
        }

## Code cleanup:

- [x] Need to add timestamp to user's input
- [ ] Handle errors in the take_task() for edge case inputs
- [ ] Add main and while to keep getting user's input unless user stops it
- [ ] Add args for faster task taking from terminal, add flags like {"-a":"add task","-d":"delete","-v":"view tasks",...}, so to handle this, I need to have 2 general state for my program, one is like main-command-line mode and the other one interactive mode 
- [x] Handle the "id" in json file
- [ ] Add 2 more ways to delete tasks, based on priority and based on time like a week old task.
- [x] Add descriptive prints at the begining of the code for user to choose.
- [ ] Work on efficient ways to find and delete tasks.
- [ ] Maybe I should combine take_task() with add_task()!
- [x] Add a function for file_exist()
- [ ] Add a smart feature for easier deadline input, like today or tomorrow or weekend or in general how interpret time in the deadline input
- [ ] Add a function for editing the existing tasks
- [ ] I also need to figure out how List the task for user, cause the json format is not clean enough here.

