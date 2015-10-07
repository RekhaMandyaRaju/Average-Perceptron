import sys,copy,pickle
import codecs,re

inputfile= sys.argv[1]
main_dict={}
finame=open(inputfile,'rb')
main_dict=pickle.load(finame)
sys.stdin = codecs.getreader('utf8')(sys.stdin.detach(), errors='ignore')

for line in sys.stdin:
  str2=''
  list1=[]
  
  line=''.join(('START ',line.rstrip(), ' END'));
  list1=line.split()
  for i in range(1,len(list1)-1):
   word=list1[i]
   pre="prev_"+list1[i-1]
   cur="cur_"+list1[i]
   nex="nex_"+list1[i+1]
   if(len(list1) > 2):
    suffix3=list1[-3:]
   else:
    suffix3=0
   if(len(list1) > 1):
    suffix2=list1[-2:]
   else:
    suffix2=0
   suf3="suf3_"+str(suffix3)
   suf2="suf2_"+str(suffix2) 
   
   wshape=re.sub('[A-Z]+','A',list1[0])
   wshape=re.sub('[a-z]+','a',wshape)
   wshape=re.sub('[0-9]+','9',wshape)
   wshape=re.sub(r'[^\w_]+','-',wshape)
   ws="wshape_"+wshape  
   
   str1=pre+" "+cur+" "+nex+" "+suf3+" "+suf2+" "+ws
   dict_clas={}
   list2=str1.split()
   for key in main_dict.keys():
    total=0
    for j in range(0,len(list2)):
      if list2[j] in main_dict[key]:
        total+=main_dict[key][list2[j]] 
    dict_clas[key]=total    
   pred_class = max(dict_clas,key=dict_clas.get)
   str2+=word + "/"+ pred_class+' '
  print(str2)
  sys.stdout.flush()        
finame.close()




