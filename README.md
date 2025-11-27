## Notes which helped to deploy this project on render.
Step. 1 - Created a folder name 'todo'  which is having all the project files and pushed to github.
Step. 2 - removed relative imports and added absolute import(removed '.')
Step. 3 - removed 'todo' from 'todo/static' and 'todo/templates' in main.py and todos.py files , then it worked on render
Step. 4 - on render 'root directory' field put 'todo'
Step. 5 - run command on render - 'uvicorn main:app --host 0.0.0.0 --port 10000'
