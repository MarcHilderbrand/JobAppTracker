import tkinter
from JobAppData import JobAppData

class NewJobApplicationUI(tkinter.Tk):
    """
    This is a form to fill out fields for a new job application
    """

    def __init__(self, appmgr):
        super().__init__()

        self.appmgr = appmgr

        self.title("New Application Form")
        self.geometry("400x400")

        #This button should call the add_jobApp function in ApplicationManager with all the data from the form
        btn_JobAPP = tkinter.Button(self, text = "New Application", bd=2, command=self.click_addJobApp)
        btn_JobAPP.pack(side='top')

    def click_addJobApp(self):

        #collect data
        testvalue = 1

        self.appmgr.add_jobApp(job_title = testvalue) #put data here

    def closeWindow(self):
        self.destroy



if __name__ == "__main__":
    from JobApplicationManager import JobApplicationManager

    #test add job application
    testappmgr = JobApplicationManager()
    GUI = NewJobApplicationUI(testappmgr)
    GUI.mainloop()

    print(testappmgr._JobApps)