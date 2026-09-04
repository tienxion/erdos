"""Independent brute-force validation of the exploratory C++ Ramsey checker."""
import itertools, random, subprocess

def graph6(n, edges):
 E={tuple(sorted(e)) for e in edges};bits=[int((i,j) in E) for j in range(1,n) for i in range(j)];bits += [0]*((-len(bits))%6)
 return chr(n+63)+''.join(chr(63+sum(bits[i+k]<<(5-k) for k in range(6))) for i in range(0,len(bits),6))

def has_forest(adj, sizes, available=None):
 if not sizes:return True
 if available is None:available=set(range(len(adj)))
 d=sizes[0]
 if len(available)<sum(sizes)+len(sizes):return False
 for c in sorted(available):
  for leaves in itertools.combinations(sorted(adj[c]&available),d):
   if has_forest(adj,sizes[1:],available-{c}-set(leaves)):return True
 return False

def brute(n,edges,A,B):
 for mask in range(1<<len(edges)):
  red=[set() for _ in range(n)];blue=[set() for _ in range(n)]
  for k,(u,v) in enumerate(edges):
   adj=red if mask>>k&1 else blue
   adj[u].add(v);adj[v].add(u)
  if not has_forest(red,A) and not has_forest(blue,B):return False
 return True

def cpp(n,edges,A,B):
 p=subprocess.run(['/tmp/erdos561_search',','.join(map(str,A)),','.join(map(str,B))],input=graph6(n,edges)+'\n',text=True,capture_output=True)
 assert p.returncode in (0,1),p
 return p.returncode==1

rng=random.Random(561);count=0
pairs=[([2,1],[2,1]),([3,1],[2,1]),([3,2],[2,1]),([2,1,1],[2,1])]
for A,B in pairs:
 for _ in range(30):
  n=rng.randrange(5,10);full=list(itertools.combinations(range(n),2));edges=rng.sample(full,rng.randrange(3,min(11,len(full))+1))
  expected=brute(n,edges,A,B);actual=cpp(n,edges,A,B)
  assert actual==expected,(n,edges,A,B,actual,expected)
  count+=1
 # Known constructive upper bound, and deleting an edge from that host.
 ls=[max(A[i]+B[j]-1 for i in range(len(A)) for j in range(len(B)) if i+j==k) for k in range(len(A)+len(B)-1)]
 n=0;edges=[]
 for d in ls:
  edges += [(n,n+j) for j in range(1,d+1)];n+=d+1
 for E in (edges,edges[:-1]):
  expected=brute(n,E,A,B);actual=cpp(n,E,A,B);assert expected==actual,(A,B,E);count+=1
print(f'Passed {count} independent brute-force comparisons, including explicit Ramsey hosts.')
