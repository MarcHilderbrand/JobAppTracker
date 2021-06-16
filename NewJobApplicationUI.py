import tkinter as tk
from tkinter import *
from JobAppData import JobAppData

class NewJobApplicationUI(tk.Tk):
    """
    A form to fill out fields for a new job application
    """

    def __init__(self, appmgr):
        super().__init__()

        self.appmgr = appmgr

        self.title("New Application Form")
        self.geometry("400x400")

        #This button should call the add_jobApp function in ApplicationManager with all the data from the form
        self.btn_JobAPP = tk.Button(self, text = "New Application", bd=2, command=self.click_addJobApp)
        self.btn_JobAPP.pack(side='top')

        #Job Title entry 
        self.entry_jobTitle = tk.Entry(self)
        self.entry_jobTitle.place(x=40, y=40)

    def click_addJobApp(self):

        #collect data from form
        job_title = self.entry_jobTitle.get()

        self.appmgr.add_jobApp(job_title=job_title) #put data here

    def closeWindow(self):
        self.destroy



if __name__ == "__main__":
    from JobApplicationManager import JobApplicationManager

    #test add job application
    testappmgr = JobApplicationManager()
    GUI = NewJobApplicationUI(testappmgr)
    GUI.mainloop()

print(testappmgr._JobApps)
