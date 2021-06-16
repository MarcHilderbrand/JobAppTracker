from JobAppData import JobAppData
from CRUD import CRUD

class JobApplicationManager():
    """
    Handles background application data tasks

    Attriibutes:
        JobApps (list) : list of all ApplicationData objects

    """
    def __init__(self):
        #call CRUD for existing list of AppData objects
        try:
            self._JobApps = CRUD.read()
        except FileNotFoundError:
            self._JobApps = list()


    def add_jobApp(self, job_title=None, date_applied=None, posting_link=None):
        """
        This function constructs new ApplicationData object and appends it to _JobApps list

        Attributes:
            job_title
            date_applied
            posting_link
        """

        self._JobApps.append(JobAppData(job_Title=job_title))
        print(job_title)



    def edit_job(self, index):
        """
        Given the index of the job, allows the user to edit attributes of a job

        Attributes:
            index
        """

    
    

if __name__ == "__main__":

    #try adding a job
    test = JobApplicationManager()
    test.add_jobApp()


