// Exploratory exact search for counterexamples to Erdos problem 561.
// Input: graph6 lines, n <= 62, edges <= 31. Args: comma-separated star sizes.
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
using U=uint32_t; using V=uint64_t;
struct Star {V verts; U edges;};
vector<int> parse(string x) {vector<int>a; stringstream s(x); string t; while(getline(s,t,','))a.push_back(stoi(t)); sort(a.rbegin(),a.rend());return a;}
vector<U> patterns(const vector<int>&sizes,int n,const vector<vector<pair<int,int>>>& adj) {
 vector<vector<Star>> all(sizes.size());
 for(size_t p=0;p<sizes.size();++p)for(int c=0;c<n;++c){int k=sizes[p],d=adj[c].size();if(d<k)continue;
  auto gen=[&](auto&&self,int start,int left,V verts,U edges)->void {
   if(!left){all[p].push_back({verts,edges});return;}
   for(int i=start;i<=d-left;++i)self(self,i+1,left-1,verts|(V(1)<<adj[c][i].first),edges|(U(1)<<adj[c][i].second));
  }; gen(gen,0,k,V(1)<<c,0);
 }
 vector<U> out;
 auto join=[&](auto&&self,int p,V verts,U edges)->void {
  if(p==(int)sizes.size()){out.push_back(edges);return;}
  for(auto st:all[p])if(!(st.verts&verts))self(self,p+1,verts|st.verts,edges|st.edges);
 };join(join,0,0,0);sort(out.begin(),out.end());out.erase(unique(out.begin(),out.end()),out.end());return out;
}
bool avoid(const vector<U>&r,const vector<U>&b,U red,U blue,U universe) {
 while(true){U fr=0,fb=0;
  for(U q:r)if(!(q&blue)){U left=q&~red;if(!left)return false;if(!(left&(left-1)))fb|=left;}
  for(U q:b)if(!(q&red)){U left=q&~blue;if(!left)return false;if(!(left&(left-1)))fr|=left;}
  if((fr&fb)||(fr&blue)||(fb&red))return false;
  if(!fr&&!fb)break;red|=fr;blue|=fb;
 }
 U remaining=universe&~(red|blue);if(!remaining)return true;
 int scores[32]={};bool active=false;
 for(U q:r)if(!(q&blue)){active=true;U x=q&remaining;while(x){int i=__builtin_ctz(x);++scores[i];x&=x-1;}}
 for(U q:b)if(!(q&red)){active=true;U x=q&remaining;while(x){int i=__builtin_ctz(x);++scores[i];x&=x-1;}}
 if(!active)return true;
 int best=__builtin_ctz(remaining);for(int i=0;i<31;++i)if(scores[i]>scores[best])best=i;
 U bit=U(1)<<best;return avoid(r,b,red|bit,blue,universe)||avoid(r,b,red,blue|bit,universe);
}
int main(int argc,char**argv){if(argc!=3)return 2;auto a=parse(argv[1]),b=parse(argv[2]);string line;long long count=0,checked=0;int nvA=a.size(),nvB=b.size();for(int k:a)nvA+=k;for(int k:b)nvB+=k;
 while(getline(cin,line)){if(line.empty()||line[0]=='>')continue;int n=line[0]-63;if(n>62||n<0)return 3;++count;if(n<max(nvA,nvB))continue;
 vector<vector<pair<int,int>>>adj(n);int pos=0,m=0;for(int j=1;j<n;++j)for(int i=0;i<j;++i,++pos)if((line[1+pos/6]-63)&(1<<(5-pos%6))){adj[i].push_back({j,m});adj[j].push_back({i,m++});}
 if(m>31)return 4;int d=0;for(auto &v:adj)d=max(d,(int)v.size());if(d<a[0]+b[0]-2)continue;
 auto r=patterns(a,n,adj),bl=patterns(b,n,adj);if(r.empty()||bl.empty())continue;++checked;
 if(!avoid(r,bl,0,0,(U(1)<<m)-1)){cout<<"RAMSEY_HOST "<<line<<" n="<<n<<" m="<<m<<"\n";return 1;}
 }cout<<"hosts="<<count<<" nontrivial_checked="<<checked<<" no_counterexample\n";
}
