import customtkinter as ctk

class LoginApp:
    def __init__(self):
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.app = ctk.CTk()
        self.app.geometry("400x400")

        self.create_main_ui()

    def create_main_ui(self):
        label = ctk.CTkLabel(self.app, text="Modern Login System")
        label.pack(pady=20)

        frame = ctk.CTkFrame(master=self.app)
        frame.pack(pady=20, padx=40, fill='both', expand=True)

        label = ctk.CTkLabel(master=frame, text='Modern Login System')
        label.pack(pady=12, padx=10)

        user_entry = ctk.CTkEntry(master=frame, placeholder_text="Username")
        user_entry.pack(pady=12, padx=10)

        user_pass = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
        user_pass.pack(pady=12, padx=10)

        button = ctk.CTkButton(master=frame, text='Login', command=self.login)
        button.pack(pady=12, padx=10)

        checkbox = ctk.CTkCheckBox(master=frame, text='Remember Me')
        checkbox.pack(pady=12, padx=10)

    def login(self):
        print('Login successful!')

    def run(self):
        self.app.mainloop()

if __name__ == "__main__":
    login_app = LoginApp()
    login_app.run()
