# Project: CLI Task Manager (JSON version)

## requirement:

  - [x] Get the user task and show them 
  - [x] Add task to a file
  - [ ] List tasks
  - [ ] Mark done
  - [ ] Delete task
  - [x] Store in `tasks.json`
  - [ ] Each task:
        {
          "id": 1,
          "name": "...",
          "status: "done",
          "priority": 1-5
        }

## Code cleanup:

- [ ] Need to add timestamp to user's input
- [ ] Handle errors in the take_task() for edge case inputs
- [ ] Add main and while to keep getting user's input unless user stops it
- [ ] Add args for faster task taking from terminal, add flags like {"-a":"add task","-d":"delete","-v":"view tasks",...}
- [ ] Handle the "id" in json file