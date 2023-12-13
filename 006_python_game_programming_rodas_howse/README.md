# 006_python_game_programming_rodas_howse


**Python_Game_Programming By Example by Alejandro Rodas de Paz, Joseph Howse**


```bash

# go to path
cd /Users/brunoflaven/Documents/03_git/learning_python_for_all/006_python_game_programming_rodas_howse/


# check python version
python3 --version

# Python 3.4.3
# Python 3.7.7
```

```python
# launch tkinter
python3
from tkinter import Tk
root = Tk()
root.title('Hello, Bruno !')
root.mainloop()

# See https://docs.python.org/3/library/tkinter.html
```


```python
# NO OOP programmming
import tkinter as tk
   lives = 3
   root = tk.Tk()
   frame = tk.Frame(root)
   canvas = tk.Canvas(frame, width=600, height=400, bg='#aaaaff')
   frame.pack()
   canvas.pack()
   root.title('Hello, Pong!')
   root.mainloop()

```

### Explaining the __name__ == '__main__'

In the preceding snippet, we introduced the if __name__ == '__main__'
condition, which is present in many Python scripts. This snippet checks the name of the current module that is being executed, and will prevent starting the main loop where this module was being imported from another script. This block is placed at the end of the script, since it requires that the Game class be defined.



