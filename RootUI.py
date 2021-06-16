import tkinter
from NewJobApplicationUI import NewJobApplicationUI

class RootUI(tkinter.Tk):
    """
    This class is an extension of python's tkinter and handles the user interface.

    """

    def __init__(self, jobappmgr=None):
        super().__init__()

        self.appmgr = jobappmgr
        
        self.title("Job Application Tracking System")
        self.geometry("400x400")

        #Button - Add new JobApplication
        #This button should open a new window with a form to add data for a new ApplicationData object
        btn_JobAPP = tkinter.Button(self, text = "New Job Application", bd=2, command=self.new_application_form)
        btn_JobAPP.pack(side='top')
    
    def new_application_form(self):
        """
        launches form for filling out job application
        """
        new_jobApplication = NewJobApplicationUI(self.appmgr)
        new_jobApplication.mainloop()



if __name__ == "__main__":
    from JobApplicationManager import JobApplicationManager
    testappmgr = JobApplicationManager()
    GUI = RootUI(testappmgr)
    GUI.mainloop()
    


    

