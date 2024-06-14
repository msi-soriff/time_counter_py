import tkinter as tk
from datetime import datetime, timedelta

class TimeCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Time Counter App")
        
        self.start_time = None
        self.running = False
        self.elapsed_time = timedelta(0)
        
        self.time_label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.time_label.pack(pady=20)
        
        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=10)
        
        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.LEFT, padx=10)
        
        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=10)
        
        self.update_clock()
    
    def update_clock(self):
        if self.running:
            now = datetime.now()
            self.elapsed_time = now - self.start_time
            elapsed_str = str(self.elapsed_time).split('.')[0]  # Removing microseconds
            self.time_label.config(text=elapsed_str)
        
        self.root.after(1000, self.update_clock)
    
    def start(self):
        if not self.running:
            self.start_time = datetime.now() - self.elapsed_time
            self.running = True
    
    def stop(self):
        if self.running:
            self.elapsed_time = datetime.now() - self.start_time
            self.running = False
    
    def reset(self):
        self.running = False
        self.elapsed_time = timedelta(0)
        self.time_label.config(text="00:00:00")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimeCounterApp(root)
    root.mainloop()
