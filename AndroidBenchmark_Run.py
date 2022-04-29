# -*- coding: utf-8 -*-
"""
Created on Sun Jan 2

@author: John Eric Gdovin
"""



import json
import os
import argparse
import sys
import time
import threading
import AndroidBenchmarkTools as abt


#class AndroidBenchmarkThread(threading.Thread):





def main():



  pathJson = sys.argv[1]


  with open(pathJson) as jsonFile:
    testPlan = json.load(jsonFile)

  outDir = testPlan['outputfolder']

  if not os.path.exists(outDir):
      os.mkdir(outDir)




  handsetSerials = []
  bench_mark_list = []
  workload_list = []

  for handset in testPlan['handsets']:
     if handset['active'] == 'enable':
         handsetSerials.append(handset['serial'])
         print(handsetSerials)

     for testapp in testPlan['testapps']:
          if testapp['active'] == 'enable':
              bench_mark_list.append(testapp['benchmark'])

     for benchmark in bench_mark_list:

          if benchmark == "gfxbench":

              for workload in testPlan['gfxbenchtests']:
                  if workload['active'] == 'enable':
                      workload_list.append(workload['workload'])

  for i in range(0, len(handsetSerials)):

      gfxbench = abt.AndroidCommands(handsetSerials[i])

      for j in range(0, len(workload_list)):

       gfxbench.gfxbench_standard(workload_list[j])
       if workload_list[j] == 'gl_manhattan311_wqhd_off':
        time.sleep(200)










 



if "__main__" == __name__:

 main()
