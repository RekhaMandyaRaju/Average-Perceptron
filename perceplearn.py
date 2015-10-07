import sys,random
import copy,pickle
inputfile= sys.argv[1]
outputfile= sys.argv[2]

dict_main={}
list_dict={}
index=0
Dclass={}
main_list=[]
dict_tot={}
dict_clas={}
 
finame=open(inputfile,'r')
finame2=open(inputfile,'r')
foname=open(outputfile,'wb')
k=0
feat_wgt={}
n=1
for line in finame:
   name=line.split()[0]
   
   if(name not in Dclass): 
       Dclass[name]=index
       index+=1
       
   if(name in Dclass):
       
       list1= line.split()
       for i in range(1,len(list1)):
        if list1[i] not in feat_wgt:
         feat_wgt[list1[i]]=0
   main_list.insert(n,n)
   list_dict[n]=line
   n+=1

for key in Dclass.keys():
  dict_main[key]=copy.deepcopy(feat_wgt)      
finame.close() 

for v in range(0,20):
 random.shuffle(main_list)
 for line in main_list:
   list3=[]
   l=0
   feat_cnt={}
   list2=list_dict[line].split()
   name=list_dict[line].split()[0]
   for i in range(1,len(list2)):
     if list2[i] not in feat_cnt:
       feat_cnt[list2[i]]=1
       list3.insert(l,list2[i])
       l += 1

     elif list2[i] in feat_cnt:
       cnt=feat_cnt[list2[i]]
       cnt+=1
       feat_cnt[list2[i]]=cnt
   
        
     
   for key in dict_main.keys():
    total = 0
    for i in range(1,len(list2)):
     total += dict_main[key][list2[i]]
    dict_tot[key] = total
    pred_class = max(dict_tot,key=dict_tot.get)
   if pred_class != name:
    for i in range(0,len(list3)):   
      wt1=dict_main[pred_class][list3[i]] 
      wt1 -= feat_cnt[list3[i]]
      dict_main[pred_class][list3[i]]=wt1
      wt2=dict_main[name][list3[i]]
      wt2 += feat_cnt[list3[i]]
      dict_main[name][list3[i]]=wt2
 
pickle.dump(dict_main,foname)
finame2.close()
foname.close()

 
 
