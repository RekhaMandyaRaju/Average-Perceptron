import sys,pickle
import os,re
inputfile= sys.argv[1]
outputfile= sys.argv[2]

finame=open(inputfile,'r',encoding='UTF-8',errors='ignore')
foname=open(outputfile,'w')

list1=[]
ftemp=open('test_ner','w')

for line in finame:
 line=''.join(('START/START/START ',line.rstrip(), ' END/END/END'));
 list1=line.split()
 for i in range(1,len(list1)-1):
  str1=''.join(list1[i])
  tag_list=str1.split('/')
  tag_list2='/'.join(tag_list[:2]), '/'.join(tag_list[2:])
  str1=''.join(list1[i-1])
  pre_tag_list=str1.split('/')
  prev_list='/'.join(pre_tag_list[:2]), '/'.join(pre_tag_list[2:])
  pre="prev_"+prev_list[0]
  cur="cur_"+tag_list2[0]
  str1=''.join(list1[i+1])
  nex_tag_list=str1.split('/')
  nex_list='/'.join(nex_tag_list[:2]), '/'.join(nex_tag_list[2:])
  nex="nex_"+nex_list[0]
  list_new = tag_list2[0].split('/')
  if(len(list_new[0]) > 2):
   suffix3=list_new[0][-3:]
  else:
   suffix3=0
  if(len(list_new[0]) > 1):
   suffix2=list_new[0][-2:]
  else:
   suffix2=0
  suf3="suf3_"+str(suffix3)
  suf2="suf2_"+str(suffix2) 
   
  wshape=re.sub('[A-Z]+','A',list_new[0])
  wshape=re.sub('[a-z]+','a',wshape)
  wshape=re.sub('[0-9]+','9',wshape)
  wshape=re.sub(r'[^\w_]+','-',wshape)
  ws="wshape_"+wshape  

  str1=tag_list2[1] + "  "+pre+" "+cur+" "+nex+" "+suf3+" "+suf2+" "+ws
  ftemp.write(str1)
  ftemp.write("\n")
ftemp.close()   
#os.system('python3 perceplearn.py training_ner.txt MODEL_ner')
  
finame.close()
foname.close()

    
