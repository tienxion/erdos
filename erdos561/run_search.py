"""Enumerate all possible counterexample hosts for the listed finite instances.
Requires nauty geng and search.cpp compiled to a local executable.
"""
import argparse, json, subprocess, time
from pathlib import Path
P=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--geng',default='/tmp/nauty2_9_3/geng');ap.add_argument('--checker',default='/tmp/erdos561_search');args=ap.parse_args()
cases=[('2,1','2,1'),('3,1','2,1'),('3,2','2,1'),('4,1','2,1'),('4,2','2,1'),('3,2','3,2'),('4,2','3,1'),('4,2','3,2'),('4,3','2,1'),('4,2','4,2'),('2,1,1','2,1,1'),('2,2,1','2,1,1'),('3,2,1','2,2,1')]
out=[]
for a,b in cases:
 A=list(map(int,a.split(',')));B=list(map(int,b.split(',')))
 bound=sum(max(A[i]+B[j]-1 for i in range(len(A)) for j in range(len(B)) if i+j==k) for k in range(len(A)+len(B)-1))
 t=time.time();case={'a':A,'b':B,'conjectured':bound,'by_n':[]};print(a,b,bound,flush=True)
 for n in range(2,2*(bound-1)+1):
  if n*(n-1)//2<bound-1:continue
  gen=subprocess.Popen([args.geng,'-q','-d1',str(n),f'{bound-1}:{bound-1}'],stdout=subprocess.PIPE)
  p=subprocess.run([args.checker,a,b],stdin=gen.stdout,capture_output=True,text=True);gen.stdout.close();gr=gen.wait()
  if gr:raise RuntimeError(f'geng failed {gr}')
  case['by_n'].append({'n':n,'result':p.stdout.strip()})
  if p.returncode:
   case['counterexample']=p.stdout.strip();break
 case['seconds']=time.time()-t;out.append(case)
 print(case,flush=True)
 (P/'results.json').write_text(json.dumps(out,indent=2)+'\n')
 if 'counterexample' in case:break
