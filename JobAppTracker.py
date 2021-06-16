from DashboardUI import DashboardUI
from JobApplicationManager import JobApplicationManager as appmgr
"""
Script is called when application begins
"""




if __name__ == "__main__":

    
    #instantiate ApplicationManager and pass it into the RootUI
    appmgr = appmgr()
    GUI = DashboardUI(appmgr)
    GUI.mainloop()