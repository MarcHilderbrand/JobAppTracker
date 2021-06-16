import unittest
from JobApplicationManager import JobApplicationManager
from NewJobApplicationUI import NewJobApplicationUI

#set up sample jobs
sampleJobTitles = ["Sample Job %s"%i for i in range(10)]
print(sampleJobTitles)

appmgr = JobApplicationManager()

class Test_NewJobApplicationUI(unittest.TestCase):
    def setUp(self) -> None:

        #initialize NewJobApplicationUI object
        self.njaUI = NewJobApplicationUI(appmgr)

    # def test_click_addJobApp(self):
    #     for i in range(0,len(sampleJobTitles)):
    #         self.njaUI.click_addJobApp(sampleJobTitles[i])
    #         print(appmgr._JobApps[i]._job_title)
    #         self.assertEqual(sampleJobTitles[i],appmgr._JobApps[i]._job_title)


if __name__ == "__main__":
    unittest.main()