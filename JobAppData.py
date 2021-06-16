class JobAppData():
    """
    jobApp object

    Attributes:
    job_Title: String
    date_applied: date
    link_Job_Post: string?
    
    """
    def __init__(self, job_Title=None, date_applied=None, link_Job_Post=None):
        self._job_Title=job_Title
        self._date_applied=date_applied
        self._link_Job_Post=link_Job_Post
