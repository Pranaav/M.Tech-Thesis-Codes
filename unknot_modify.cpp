#include <link/link.h>
#include <bits/stdc++.h>
std::unordered_set<std::string> chek;
std::set<int> refinery(std::set<int> &s, int i, int j){
    std::set<int> s1;
    for(int ind : s){
        if ((ind==i) || (ind==j))
            continue;
        else if((ind > i)  && (ind<j))
            s1.insert(ind-1);
        else if((ind < i) && (ind > j))
            s1.insert(ind-1);
        else if((ind > i) && (ind > j))
            s1.insert(ind -2);
        else
            s1.insert(ind);
    }
    return s1;
}

bool specialGreedyDeep(regina::Link &d, std::set<int> &s, int k){
    std::string strig = d.str();
    for(int i : s){
        strig += " " + std::to_string(i);
    }
    strig += " " + std::to_string(k);
    if(chek.find(strig)!=chek.end()){
        return false;
    }
    chek.insert(strig);
    int n = d.size();
    if(n==0){
        return true;
    }
    if(k<0){
        return false;
    }

    bool greedy = false;
    for(int index = 0;index<n;index++){
        if(s.find(index)!=s.end()){
            continue;
        }
        int next = d.crossing(index)->next(1).crossing()->index();
        if(s.find(next)!=s.end()){
            continue;
        }
        else{
            regina::Link l = regina::Link(d);
            if(l.r2(l.crossing(index), true, true)){
                std::set<int> s1 = refinery(s, index, next);
                greedy = true;
                if(specialGreedyDeep(l, s1, k)){
                    return true;
                }
            }
        }
    }
    if(greedy){
        return false;
    }

    // r2-:
    for(int index : s){
        int next = d.crossing(index)->next(1).crossing()->index();
        if(s.find(next)!=s.end()){
            continue;
        }
        else{
            regina::Link l = regina::Link(d);
            if(l.r2(l.crossing(index), true, true)){
                std::set<int> s1 = refinery(s, index, next);
                if(specialGreedyDeep(l, s1, k)){
                    return true;
                }
            }
        }
    }

    // r1-

    for(int index : s){
        regina::Link l = regina::Link(d);
        if(l.r1(l.crossing(index), true, true)){
            std::set<int> s1 = refinery(s, index, n);
            if(specialGreedyDeep(l, s1, k-1)){
                return true;
            }
        }
    }


    // R1+ :

    for(int index : s){
        for(int i=0;i<2;i++){
            int next = d.crossing(index)->next(i).crossing()->index();
            if(s.find(next)==s.end()){
                continue;
            }
            for(int side=0;side<2;side++){
                regina::Link l = regina::Link(d);
                if(l.r1(l.crossing(index)->next(i), side, 1, true, true)){
                    std::set<int> s1 = s;
                    s1.insert(n);
                    if(specialGreedyDeep(l, s1, k-3)){
                        return true;
                    }
                }
                l = regina::Link(d);
                if(l.r1(l.crossing(index)->next(i), side, -1, true, true)){
                    std::set<int> s1 = s;
                    s1.insert(n);
                    if(specialGreedyDeep(l, s1, k-3)){
                        return true;
                    }
                }
            }
        }
    }

    // R2+ :

    for(int index : s) {
        for(int i=0;i<2;i++){
            int next = d.crossing(index)->next(i).crossing()->index();
            if(s.find(next)==s.end()){
                continue;
            }
            for(int index2 : s){
                // if(index2==index){

                // }
                for(int j=0;j<2;j++){
                    next = (d.crossing(index2)->next(j)).crossing()->index();
                    if(s.find(next)==s.end()){
                        continue;
                    }
                    for(int upside=0;upside<2;upside++){
                        for(int lowside = 0;lowside<2;lowside++){
                            regina::Link l = regina::Link(d);
                            if(l.r2(l.crossing(index)->next(i), upside, l.crossing(index2)->next(j), lowside, true, true)){
                                std::set<int> s1 = s;
                                s1.insert(n);
                                s1.insert(n+1);
                                if(specialGreedyDeep(l, s1, k-4)){
                                    return true;
                                }
                            }
                        }
                        
                        
                    }
                }
            }
        }
    }

    // R3 :
    for(int index : s){
        std::set<int> s1 = s;
        regina::Link l = regina::Link(d);
        if(l.r3(l.crossing(index), 0, true, true)){
            int next = d.crossing(index)->next(1).crossing()->index();
            if(s.find(next)==s.end()){
                continue;
            }
            if(d.crossing(index)->sign()== -1){
                int cros2 = d.crossing(index)->prev(0).crossing()->index();
                if(s.find(cros2)==s.end()){
                    continue;
                }
                if(specialGreedyDeep(l, s1, k-2)){
                    return true;
                }
            }
            else{
                int cros2 = d.crossing(index)->next(0).crossing()->index();
                if(s.find(cros2)==s.end()){
                    continue;
                }
                if(specialGreedyDeep(l, s1, k-2)){
                    return true;
                }
            }
        }
        l = regina::Link(d);
        if(l.r3(l.crossing(index), 1, true, true)){
            int next = d.crossing(index)->next(1).crossing()->index();
            if(s.find(next)==s.end()){
                continue;
            }
            if(d.crossing(index)->sign()== -1){
                int cros2 = d.crossing(index)->next(0).crossing()->index();
                if(s.find(cros2)==s.end()){
                    continue;
                }
                if(specialGreedyDeep(l, s1, k-2)){
                    return true;
                }
            }
            else{
                int cros2 = d.crossing(index)->prev(0).crossing()->index();
                if(s.find(cros2)==s.end()){
                    continue;
                }
                if(specialGreedyDeep(l, s1, k-2)){
                    return true;
                }
            }
        }
    }

    return false;


}


bool specialGreedy(regina::Link D, int k, std::set<int> all_set){
    int n = D.size();
    // call recursion on every combination of sets

    // std::set<int> all_set;

    std::vector<std::set<int>> v;
    v.push_back(all_set);
    std::cout<<"ewhfbdv\n";
    for(std::set<int> s : v){
        std::cout<<"hell\n";
        if(specialGreedyDeep(D, s, k)){
            return true;
        }
    }

    return false;
    




}


int main(){

    int n = 21;

    std::string gauss_code = "1 6 -7 10 11 12 -14 -15 16 -17 -18 -2 3 -4 5 7 -9 -11 17 -21 19 -20 -8 9 -10 18 21 -16 -13 14 20 -1 2 -3 4 -5 -6 8 -12 13 15 -19";
    
    int k = 21;



    regina::Link lnk = regina::Link::fromGauss(gauss_code);
    std::cout<<lnk<<'\n';
    std::set<int> all_set;
    for(int i=0;i<n;i++){
        all_set.insert(i);
    }

    // lnk.r1(lnk.crossing(0), true, false);

    // std::cout<<lnk.Link::simplifyExhaustive(2)<<"\n";

    std::cout<<specialGreedy(lnk, k, all_set);

    
}