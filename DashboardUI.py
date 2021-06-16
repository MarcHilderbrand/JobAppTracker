import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
import datetime as dt
from NewJobApplicationUI import NewJobApplicationUI

sampleJobTitles = ["Sample Job %s"%i for i in range(10)]
print(sampleJobTitles)

class DashboardUI(tk.Tk):
    """
    Extension of python's tkinter and functions as the main dashboard

    """

    def __init__(self, jobappmgr=None):
        super().__init__()

        self.appmgr = jobappmgr
        
        self.title("Job Application Tracking System")
        self.geometry("400x400")

        #Button - Add new JobApplication
        #This button should open a new window with a form to add data for a new JobAppData object
        btn_JobApplications = ttk.Button(self, text = "New Job Application", command=self.new_application_form)
        btn_JobApplications.pack(side='top')

        #TreeView - Show list of all JobApplications --==TODO: make this section a class of its own==--
        #
        treeView_JobTable = ttk.Treeview()
        treeView_JobTable['columns']=("Date Applied", "Job Title")
        treeView_JobTable.column('#0', width=0, stretch=False)

        #Date Applied
        treeView_JobTable.column("Date Applied", anchor=CENTER, width=80)
        treeView_JobTable.heading("Date Applied", text="Date Applied")

        #Job Title
        treeView_JobTable.column("Job Title", anchor=CENTER, width=80)
        treeView_JobTable.heading("Job Title", text="Job Title")

        #Insert jobApplications -=TODO=- replace samplejobtitles with _JobApps list from JobApplicationManager
        for i in range(0,len(sampleJobTitles)):
            treeView_JobTable.insert('',0, values=('_ "%s"'%sampleJobTitles[i]))

        treeView_JobTable.pack()

        
    
    def new_application_form(self):
        """
        launches form for filling out job application
        """
        new_jobApplication = NewJobApplicationUI(self.appmgr)
        new_jobApplication.mainloop()



if __name__ == "__main__":
    from JobApplicationManager import JobApplicationManager
    testappmgr = JobApplicationManager()
    testappmgr._JobApps = sampleJobTitles
    GUI = DashboardUI(testappmgr)
    GUI.mainloop()
    
    



