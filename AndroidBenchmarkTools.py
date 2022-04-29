import subprocess
from subprocess import Popen, PIPE



class AndroidCommands:

    def __init__(self, serial):
        self.serial = serial

    def adb_root(self):

        adbProc = subprocess.Popen("adb -s " + self.serial + " root", stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        print(adbProc.communicate())

    def gfxbench_standard(self, workload_list):


         for i in range(0, len(workload_list)):
          adb_proc = subprocess.Popen('adb -s '+ self.serial + ' shell am  broadcast'
                                    ' -a net.kishonti.testfw.ACTION_RUN_TESTS -n '
                                    'net.kishonti.gfxbench.vulkan.v50000.corporate/'
                                    'net.kishonti.benchui.corporate.CommandLineSession -e test_ids '
                                     + str(workload_list), stdout=subprocess.PIPE, stdin=subprocess.PIPE)

         print(adb_proc.communicate())


class GeekBench5:

    def __init__(self, serial):
        self.serial = serial


    def 
