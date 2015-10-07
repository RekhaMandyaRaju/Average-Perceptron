import sys,copy,pickle
inputfile= sys.argv[1]


main_dict={}
finame=open(inputfile,'rb')

main_dict=pickle.load(finame)
for line in sys.stdin:
  feat_cnt={}
  dict_clas={}
  list1=line.split()
   
  for key in main_dict.keys():
    total=0
    for i in range(0,len(list1)):
      if list1[i] in main_dict[key]:
        total+=main_dict[key][list1[i]] 
    dict_clas[key]=total    
  pred_class = max(dict_clas,key=dict_clas.get)
  print(pred_class)
  sys.stdout.flush()        
finame.close()

