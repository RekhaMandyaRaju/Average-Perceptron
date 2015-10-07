import sys,pickle
import os,re

inputfile= sys.argv[1]
outputfile= sys.argv[2]

finame=open(inputfile,'r')
foname=open(outputfile,'wb')

list1=[]
ftemp=open('training_pos','w')

for line in finame:
  line=''.join(('START/START ',line.rstrip(), ' END/END'));
  list1=line.split()
  for i in range(1,len(list1)-1):
   str1=''.join(list1[i])
   tag_list=str1.split('/')
   str1=''.join(list1[i-1])
   prev_list=str1.split('/')
   pre="prev_"+prev_list[0]
   cur="cur_"+tag_list[0]
   str1=''.join(list1[i+1])
   nex_list=str1.split('/')
   nex="nex_"+nex_list[0]
   if(len(tag_list[0]) > 2):
    suffix3=tag_list[0][-3:]
   else:
    suffix3=0
   if(len(tag_list[0]) > 1):
    suffix2=tag_list[0][-2:]
   else:
    suffix2=0
   suf3="suf3_"+str(suffix3)
   suf2="suf2_"+str(suffix2) 
   
   wshape=re.sub('[A-Z]+','A',tag_list[0])
   wshape=re.sub('[a-z]+','a',wshape)
   wshape=re.sub('[0-9]+','9',wshape)
   wshape=re.sub(r'[^\w_]+','-',wshape)
   ws="wshape_"+wshape  
   str1=tag_list[1] + "  "+pre+" "+cur+" "+nex+" "+suf3+" "+suf2+" "+ws
   ftemp.write(str1)
   ftemp.write('\n')
ftemp.close()   
#os.system('python3 perceplearn.py training_pos MODEL')
finame.close()
foname.close()
 
    
