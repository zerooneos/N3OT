import time
import tkinter as tk

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        master.title("Pomodoro Timer")

        # 设置工作和休息时间
        self.work_time = 25  # 25 minutes
        self.break_time = 5  # 5 minutes

        # 创建 UI 元素
        self.timer_label = tk.Label(master, font=("Helvetica", 48))
        self.timer_label.pack(pady=20)

        self.buttons_frame = tk.Frame(master)
        self.buttons_frame.pack(pady=20)

        self.start_button = tk.Button(self.buttons_frame, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(self.buttons_frame, text="Stop", command=self.stop_timer)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(self.buttons_frame, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT, padx=10)

        self.is_work_time = True
        self.timer_running = False
        self.remaining_time = self.work_time * 60  # 初始工作时间为 25 分钟

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.timer_loop()

    def stop_timer(self):
        self.timer_running = False

    def reset_timer(self):
        self.timer_running = False
        self.is_work_time = True
        self.remaining_time = self.work_time * 60
        self.update_timer_display()

    def timer_loop(self):
        if self.timer_running:
            self.remaining_time -= 1
            self.update_timer_display()

            if self.remaining_time == 0:
                if self.is_work_time:
                    self.is_work_time = False
                    self.remaining_time = self.break_time * 60
                    print("Time for a break!")
                else:
                    self.is_work_time = True
                    self.remaining_time = self.work_time * 60
                    print("Back to work!")

            self.master.after(1000, self.timer_loop)

    def update_timer_display(self):
        minutes = self.remaining_time // 60
        seconds = self.remaining_time % 60
        self.timer_label.configure(text=f"{minutes:02d}:{seconds:02d}")

root = tk.Tk()
timer = PomodoroTimer(root)
root.mainloop()
