import customtkinter as ctk

def add_todo():
    todo = entry.get()
    
    if entry.checkbox: 
        entry.checkbox.configure(text=todo)
        entry.checkbox = None
    elif todo:  
        create_task(todo)
    
    entry.delete(0, ctk.END)

def create_task(todo):
    frame = ctk.CTkFrame(scrollable_frame, fg_color="#2b2b2b")
    frame.pack(fill="x", pady=5)
    
    checkbox = ctk.CTkCheckBox(frame, text=todo, text_color="#e0e0e0", fg_color="#3b3b3b", border_color="#5a5a5a")
    checkbox.pack(side="left", padx=10)
    
    edit_button = ctk.CTkButton(frame, text="Edit", command=lambda: edit_task(checkbox), fg_color="#4a4a4a", hover_color="#616161")
    edit_button.pack(side="right", padx=10)
    
    delete_button = ctk.CTkButton(frame, text="Delete", command=frame.destroy, fg_color="#ff4444", hover_color="#ff6666")
    delete_button.pack(side="right", padx=10)

def edit_task(checkbox):
    entry.delete(0, ctk.END)
    entry.insert(0, checkbox.cget("text"))
    entry.focus()
    entry.checkbox = checkbox

def on_enter_key(event):
    add_todo()


root = ctk.CTk()
root.geometry("750x450")
root.title("Todo App")


ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("dark-blue")  

title_label = ctk.CTkLabel(root, text="Daily Tasks", font=ctk.CTkFont(size=30, weight="bold"), text_color="#f5f5f5")
title_label.pack(padx=10, pady=(40, 20))


scrollable_frame = ctk.CTkScrollableFrame(root, width=500, height=210, fg_color="#1f1f1f", scrollbar_button_color="#666666")
scrollable_frame.pack(pady=10)

entry = ctk.CTkEntry(root, placeholder_text="Add todo", fg_color="#2b2b2b", text_color="#e0e0e0", placeholder_text_color="#9e9e9e", border_color="#4a4a4a")
entry.pack(fill="x", padx= 160, pady=10)
entry.bind("<Return>", on_enter_key)  
entry.checkbox = None  

add_button = ctk.CTkButton(root, text="Add", command=add_todo, fg_color="#1976d2", hover_color="#1565c0")
add_button.pack(pady=10)

root.mainloop()
