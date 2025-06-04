import tkinter as tk
from tkinter import messagebox
from bots.discord import DiscordBot


class DiscordBotUI:
    def __init__(self, master):
        self.master = master
        master.title("Discord Bot Controller")

        # General Section
        tk.Label(master, text="General", font=("Arial", 12, "bold")).pack()

        tk.Button(master, text="초대 코드 생성", command=self.create_invite).pack(fill='x')
        tk.Button(master, text="문자열을 채널에 전송", command=self.send_message).pack(fill='x')
        tk.Button(master, text="관리자 권한 부여", command=self.grant_admin).pack(fill='x')
        tk.Button(master, text="회장단 권한 부여", command=self.grant_exec).pack(fill='x')

        # User Section
        tk.Label(master, text="User", font=("Arial", 12, "bold")).pack(pady=(10, 0))

        tk.Button(master, text="유저에 역할 부여", command=self.add_role_to_user).pack(fill='x')
        tk.Button(master, text="유저 역할 제외", command=self.remove_user_from_role).pack(fill='x')

        # SigPig Section
        tk.Label(master, text="SigPig", font=("Arial", 12, "bold")).pack(pady=(10, 0))

        tk.Button(master, text="시그 생성", command=self.create_sig).pack(fill='x')
        tk.Button(master, text="시그 아카이브", command=self.archive_sig).pack(fill='x')

    def create_invite(self):
        result = DiscordBot.create_invite()
        messagebox.showinfo("Invite Code", result)

    def send_message(self):
        DiscordBot.send_message("1234567890", "Hello from UI!")

    def grant_admin(self):
        DiscordBot.grant_admin("1234567890")

    def grant_exec(self):
        DiscordBot.grant_exec("1234567890")

    def add_role_to_user(self):
        DiscordBot.add_role("1234567890", "New Role")

    def remove_user_from_role(self):
        DiscordBot.remove_from_role("1234567890", "Old Role")

    def create_sig(self):
        DiscordBot.create_sig("sig-alpha", ["user1", "user2", "user3"])

    def archive_sig(self):
        DiscordBot.archive_sig("sig-alpha")


if __name__ == "__main__":
    DiscordBot.start()

    root = tk.Tk()
    app = DiscordBotUI(root)
    root.mainloop()

    DiscordBot.run()
